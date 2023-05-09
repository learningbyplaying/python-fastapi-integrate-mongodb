from fastapi import APIRouter

from .schemas import userEntity, usersEntity
from config.db import conn

class UserRouter:

    def __init__(self,conn) -> None:
        self.__conn = conn

    @property
    def router(self):
        api_router = APIRouter(prefix='/users', tags=['Users']) # Optional

        @api_router.get('/')
        def find_all(  ):
            #print(list(conn.local.user.find()))
            return usersEntity(conn.local.user.find())

        @api_router.get('/{user}')
        def get(  user: str ):

            return {"User":"id"}

            #return self.__formater.format( self.__domain.files( customer )  )

        return api_router
