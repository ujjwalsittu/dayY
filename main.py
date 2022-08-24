from fastapi import FastAPI, Depends
import models
import schemas
from schemas import Users
from database import engine, Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/user')
async def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    # newuser = models.User(id=user.id, name=user.name, email=user.email)
    newuser = models.User(**user.dict())
    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser


@app.get('/users/{id}')
async def get_user(id,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user

#
@app.get('/users')
async def get_all_user(skip: int = 0, db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).all()
