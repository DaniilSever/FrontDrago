from fastapi import APIRouter, Path, Body, Query
from fastapi.responses import JSONResponse
from .deps import AAccountUC

from .dto import UUID4, QCreateAccount, QUpdateAccount
from .dto import ZAccount, ZAccountList, ZOk, ZError

prefix = "/api/v1/accounts"
router = APIRouter(prefix=prefix, tags=["accounts"])

@router.get("/")
async def get_all_accounts(uc: AAccountUC): 
    acclist: ZAccountList = await uc.get_all_accounts()
    return acclist

@router.get("/{uid}", response_model=ZAccount)
async def get_account_by_id(uc: AAccountUC, uid: UUID4 = Path(...)):
    acc: ZAccount = await uc.get_account_by_id(uid)
    return acc

@router.post("/", response_model=ZAccount)
async def create_account(uc: AAccountUC, req: QCreateAccount = Body(...)):
    acc: ZAccount = await uc.create_account(req)
    return acc

@router.put("/{uid}", response_model=ZOk)
async def put_account(uc: AAccountUC, uid: UUID4 = Path(...), req: QUpdateAccount = Body(...)):
    res: ZOk = await uc.put_account(uid, req)
    return res

@router.patch("/{uid}", response_model=ZOk)
async def patch_account(uc: AAccountUC, uid: UUID4 = Path(...), req: QUpdateAccount = Body(...)):
    res: ZOk = await uc.patch_account(uid, req)
    return res

@router.delete("/{uid}", response_model=ZOk)
async def delete_account(uc: AAccountUC, uid: UUID4 = Path(...)):
    res: ZOk = await uc.delete_account(uid)
    return res
