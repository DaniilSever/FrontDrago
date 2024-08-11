from flask import Flask
from .deps import account_uc, AccountUseCase, InvalidUidException, AccountNotFoundException, EmailBusyException

from .dto import UUID4, QCreateAccount, QUpdateAccount
from .dto import ZAccount, ZAccountList, ZOk, ZError

app = Flask(__name__)

@app.endpoint("get_all_accounts")
def get_all_accounts(uc: AccountUseCase = account_uc()): 
    acclist: ZAccountList =  uc.get_all_accounts()
    return acclist.model_dump(mode="json")

@app.endpoint("get_account_by_id")
def get_account_by_id(uid: UUID4, uc: AccountUseCase = account_uc()):
    try:
        acc: ZAccount | ZError =  uc.get_account_by_id(uid)
    except InvalidUidException as e:
        return ZError(message=str(e), status_code=422).model_dump(mode="json")
    except AccountNotFoundException as e:
        return ZError(message=str(e), status_code=404).model_dump(mode="json")
    return acc.model_dump(mode="json")

@app.endpoint("create_account")
def create_account(req: QCreateAccount, uc: AccountUseCase = account_uc()):
    try:
        acc: ZAccount =  uc.create_account(req)
    except EmailBusyException as e:
        return ZError(message=str(e), status_code=400).model_dump(mode="json")
    return acc.model_dump(mode="json")

@app.endpoint("put_account")
def put_account(uid: UUID4, req: QUpdateAccount, uc: AccountUseCase = account_uc()):
    try:
        res: ZOk | ZError =  uc.put_account(uid, req)
    except InvalidUidException as e:
        return ZError(message=str(e), status_code=422).model_dump(mode="json")
    except AccountNotFoundException as e:
        return ZError(message=str(e), status_code=404).model_dump(mode="json")
    return res.model_dump(mode="json")

@app.endpoint("patch_account")
def patch_account(uid: UUID4, req: QUpdateAccount, uc: AccountUseCase = account_uc()):
    try:
        res: ZOk | ZError =  uc.patch_account(uid, req)
    except InvalidUidException as e:
        return ZError(message=str(e), status_code=422)
    except AccountNotFoundException as e:
        return ZError(message=str(e), status_code=422)
    return res.model_dump(mode="json")

@app.endpoint("delete_account")
def delete_account(uid: UUID4, uc = account_uc()):
    try:
        res: ZOk | ZError =  uc.delete_account(uid)
    except InvalidUidException as e:
        return ZError(message=str(e), status_code=422).model_dump(mode="json")
    return res.model_dump(mode="json")
