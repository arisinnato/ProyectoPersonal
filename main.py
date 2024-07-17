from fastapi import FastAPI
from database import engine
from typeuser import models as role_models
from users import models as user_models
from typeuser.router import router as roles_router
from users.routers import router as users_router

app = FastAPI()

role_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)

app.include_router(roles_router, prefix="/roles", tags=["roles"])
app.include_router(users_router, prefix="/users", tags=["users"])
