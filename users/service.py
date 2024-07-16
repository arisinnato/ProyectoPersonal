from sqlalchemy.orm import Session
from users import models, schemas
from models import Role

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        country=user.country
    )
    cliente_role = db.query(Role).filter(Role.name == "Cliente").first()
    db_user.roles.append(cliente_role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
