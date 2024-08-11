from typing import Protocol
from .dto import UUID4, QCreateAccount, QUpdateAccount
from .dto import XOk, XAccountCreated

class IrepAccount(Protocol):
    
    def get_all_accounts(self) -> list:
        raise NotImplementedError

    def get_account_by_id(self, uid: UUID4) -> dict:
        raise NotImplementedError
    
    def create_account(self, req: QCreateAccount) -> XAccountCreated:
        raise NotImplementedError
    
    def update_account(self, uid: UUID4, req: QUpdateAccount) -> XOk:
        raise NotImplementedError
    
    def delete_account(self, uid: UUID4) -> XOk:
        raise NotImplementedError