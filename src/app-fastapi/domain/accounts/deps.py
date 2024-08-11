from fastapi import Depends
from typing import Annotated
from .account_uc import AccountUseCase
from .account_repo import AccountRepo
from .config import get_config

async def account_uc() -> AccountUseCase:
    cfg = get_config()
    repo = AccountRepo(cfg)
    return AccountUseCase(repo)

AAccountUC = Annotated[AccountUseCase, Depends(account_uc)]