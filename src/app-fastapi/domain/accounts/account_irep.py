from typing import Protocol
from dto import QAccount, QCreateAccount, QUpdateAccount
from dto import XOk, XError

class IrepAccount(Protocol):
    
    def get_all_accounts(self) -> list:
        raise NotImplementedError

    def get_account_by_id(self, account_id: QAccount) -> dict:
        raise NotImplementedError
    
    def create_account(self, req: QCreateAccount) -> XOk | XError:
        raise NotImplementedError
    
    def update_account(self, account_id: QAccount, req: QUpdateAccount) -> XOk | XError:
        raise NotImplementedError
    
    def delete_account(self, account_id: QAccount) -> XOk | XError:
        raise NotImplementedError