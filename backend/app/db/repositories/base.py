from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
# from api.config.database import get_db

# class BaseRepository:
#     def __init__(self, db: Session = Depends(get_db)) -> None:
#         self.db = db