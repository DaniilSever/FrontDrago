from typing import Protocol
from pydantic import UUID4

class IrepAccount(Protocol):
    
    def get_all_accounts(self) -> list:
        raise NotImplementedError

    def get_account_by_id(self, account_id: UUID4) -> dict:
        raise NotImplementedError
    
    def create_account(self, account_data: dict) -> dict:
        raise NotImplementedError