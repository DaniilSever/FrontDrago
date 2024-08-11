from dto import QAccount, QCreateAccount, QUpdateAccount
from dto import ZAccount, ZAccountList, ZOk, ZError
from account_irep import IrepAccount

class AccountUseCase:
    
    def __init__(self, repo: IrepAccount) -> None:
        self._repo: IrepAccount = repo

    def get_all_accounts(self) -> ZAccountList:
        pass 

    def get_account_by_id(self, account_id: QAccount) -> dict:
        pass

    def create_account(self, req: QCreateAccount) -> ZOk | ZError:
        pass
    
    def put_account(self, account_id: QAccount, req: QUpdateAccount) -> ZOk | ZError:
        pass

    def patch_account(self, account_id: QAccount, req: QUpdateAccount) -> ZOk | ZError:
        pass

    def delete_account(self, account_id: QAccount) -> ZOk | ZError:
        pass