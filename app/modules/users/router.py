from fastapi import APIRouter

class UserRouter:

    def __init__(self,domain=None) -> None: #, domain: CleanerDomain) -> None:
        self.__domain = domain

    @property
    def router(self):
        api_router = APIRouter(prefix='/users', tags=['Users']) # Optional

        @api_router.get('/{user}')
        def get(  user: str ):

            return {"User":"id"}

            #return self.__formater.format( self.__domain.files( customer )  )

        return api_router
