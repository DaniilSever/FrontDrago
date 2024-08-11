from dto import QAccount, QCreateAccount, QUpdateAccount
from dto import XAccount, XAccountCreated, XOk
from dto import ZAccount, ZAccountList, ZOk, ZError
from account_irep import IrepAccount

class AccountUseCase:
    async def __init__(self, repo: IrepAccount) -> None:
        self._repo: IrepAccount = repo

    async def get_all_accounts(self) -> ZAccountList:
        accounts = self._repo.get_all_accounts()
        items = [ZAccount(**el) for el in accounts]
        return ZAccountList(count=len(accounts), items=items) 

    async def get_account_by_id(self, uid: QAccount) -> ZAccount | ZError:
        try:
            account: XAccount = await self._repo.get_account_by_id(uid)
        except KeyError as e:
            raise ZError(message=str(e))
        except ValueError as e:
            raise ZError(message=str(e))
        return ZAccount(*account)

    async def create_account(self, req: QCreateAccount) -> ZOk | ZError:
        try:
            uid = await self._repo.create_account(req)
        except KeyError as e:
            raise ZError(message=str(e))
        return ZAccount(uid=uid, *req)
    
    async def put_account(self, account_id: QAccount, req: QUpdateAccount) -> ZOk | ZError:
        try:
            res = await self._repo.update_account(account_id, req)
        except KeyError as e:
            raise ZError(message=str(e))
        except ValueError as e:
            raise ZError(message=str(e))
        return ZOk(message=res.message)

    async def patch_account(self, account_id: QAccount, req: QUpdateAccount) -> ZOk | ZError:
        try:
            res = await self._repo.update_account(account_id, req)
        except KeyError as e:
            raise ZError(message=str(e))
        except ValueError as e:
            raise ZError(message=str(e))
        return ZOk(message=res.message)

    async def delete_account(self, account_id: QAccount) -> ZOk | ZError:
        try:
            res: XOk = await self._repo.delete_account(account_id)
        except KeyError as e:
            raise ZError(message=str(e))
        return ZOk(message=res.message)