from .dto import UUID4, QCreateAccount, QUpdateAccount
from .dto import XAccount, XAccountCreated, XOk
from .dto import ZAccount, ZAccountList, ZOk, ZError
from .account_irep import IrepAccount

class EmailBusyException(Exception):
    pass

class InvalidUidException(Exception):
    pass

class AccountNotFoundException(Exception):
    pass

class AccountUseCase:
    def __init__(self, repo: IrepAccount) -> None:
        self._repo: IrepAccount = repo

    async def get_all_accounts(self) -> ZAccountList:
        accounts = await self._repo.get_all_accounts()
        items = [ZAccount(**el) for el in accounts]
        return ZAccountList(count=len(accounts), items=items) 

    async def get_account_by_id(self, uid: UUID4) -> ZAccount:
        try:
            res: XAccount = await self._repo.get_account_by_id(uid)
        except KeyError:
            raise InvalidUidException("invalid uid")
        except ValueError:
            raise AccountNotFoundException("account not found")
        return ZAccount(
            uid=res.uid,
            email=res.email,
            name=res.name,
            password=res.password
        )

    async def create_account(self, req: QCreateAccount) -> ZAccount:
        try:
            res: XAccountCreated = await self._repo.create_account(req)
        except KeyError:
            raise EmailBusyException("email busy")

        return ZAccount(
            uid=res.uid,
            email=req.email,
            name=req.name,
            password=req.password
        )
    
    async def put_account(self, account_id: UUID4, req: QUpdateAccount) -> ZOk | ZError:
        try:
            res = await self._repo.update_account(account_id, req)
        except KeyError:
            raise InvalidUidException("invalid uid")
        except ValueError:
            raise AccountNotFoundException("account not found")
        return ZOk(message=res.message)

    async def patch_account(self, account_id: UUID4, req: QUpdateAccount) -> ZOk | ZError:
        try:
            res = await self._repo.update_account(account_id, req)
        except KeyError:
            raise InvalidUidException("invalid uid")
        except ValueError:
            raise AccountNotFoundException("account not found")
        return ZOk(message=res.message)

    async def delete_account(self, account_id: UUID4) -> ZOk | ZError:
        try:
            res: XOk = await self._repo.delete_account(account_id)
        except KeyError:
            raise InvalidUidException("invalid uid")
        return ZOk(message=res.message)