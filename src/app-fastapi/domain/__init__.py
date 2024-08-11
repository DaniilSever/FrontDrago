from .accounts.account_api import router as account_api

routers =[
    account_api,
]

__all__ = [
    routers
]