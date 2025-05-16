from fastapi import FastAPI
import models
from database import engine
import user  

models.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)  
