from typing import Protocol
from pydantic import UUID4
from dto import QCreateAccount, QUpdateAccount
from dto import ZOk, ZError

class IrepAccount(Protocol):
    
    def get_all_accounts(self) -> list:
        raise NotImplementedError

    def get_account_by_id(self, account_id: UUID4) -> dict:
        raise NotImplementedError
    
    def create_account(self, req: QCreateAccount) -> ZOk | ZError:
        raise NotImplementedError
    
    def update_account(self, account_id: UUID4, req: QUpdateAccount) -> ZOk | ZError:
        raise NotImplementedError
    
    def delete_account(self, account_id: UUID4) -> ZOk | ZError:
        raise NotImplementedError