from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos
from starlette.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(todos.router)

# @app.get("/test")
# async def test():
#     return {"message": "main.py is working"}

# #print("TODOS ROUTER:", todos.router.routes)
# print("\n=== APP ROUTES ===")
# for route in app.routes:
#     print(type(route).__name__, route.path,  getattr(route, "methods", None))
