from .account_uc import AccountUseCase, InvalidUidException, EmailBusyException, AccountNotFoundException
from .account_repo import AccountRepo
from .config import get_config

def account_uc() -> AccountUseCase:
    cfg = get_config()
    repo = AccountRepo(cfg)
    return AccountUseCase(repo)
