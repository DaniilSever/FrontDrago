from fastapi import APIRouter, Path, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .deps import AAccountUC, InvalidUidException, AccountNotFoundException, EmailBusyException

from .dto import UUID4, QCreateAccount, QUpdateAccount
from .dto import ZAccount, ZAccountList, ZOk, ZError

prefix = "/api/v1/accounts"
router = APIRouter(prefix=prefix, tags=["accounts"])

@router.get("/", response_model=ZAccountList)
async def get_all_accounts(uc: AAccountUC): 
    acclist: ZAccountList = await uc.get_all_accounts()
    return acclist

@router.get(
        "/{uid}", 
        response_model=ZAccount, 
        responses={
            404: {"model": ZError}, 
            422: {"model": ZError}
        }
)
async def get_account_by_id(uc: AAccountUC, uid: UUID4 = Path(...)):
    try:
        acc: ZAccount | ZError = await uc.get_account_by_id(uid)
    except InvalidUidException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=422)
    except AccountNotFoundException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=404)
    return acc

@router.post(
        "/", 
        response_model=ZAccount, 
        responses={400: {"model": ZError}}
)
async def create_account(uc: AAccountUC, req: QCreateAccount = Body(...)):
    try:
        acc: ZAccount = await uc.create_account(req)
    except EmailBusyException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=400)
    return acc

@router.put(
        "/{uid}", 
        response_model=ZOk, 
        responses={
            404: {"model": ZError}, 
            422: {"model": ZError}
        }
)
async def put_account(uc: AAccountUC, uid: UUID4 = Path(...), req: QUpdateAccount = Body(...)):
    try:
        res: ZOk | ZError = await uc.put_account(uid, req)
    except InvalidUidException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=422)
    except AccountNotFoundException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=404)
    return res

@router.patch(
        "/{uid}", 
        response_model=ZOk, 
        responses={
            404: {"model": ZError}, 
            422: {"model": ZError}
        }
)
async def patch_account(uc: AAccountUC, uid: UUID4 = Path(...), req: QUpdateAccount = Body(...)):
    try:
        res: ZOk | ZError = await uc.patch_account(uid, req)
    except InvalidUidException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=422)
    except AccountNotFoundException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=404)
    return res

@router.delete(
        "/{uid}", 
        response_model=ZOk, 
        responses={422: {"model": ZError}}
)
async def delete_account(uc: AAccountUC, uid: UUID4 = Path(...)):
    try:
        res: ZOk | ZError = await uc.delete_account(uid)
    except InvalidUidException as e:
        return JSONResponse(content=jsonable_encoder(ZError(message=str(e))), status_code=422)
    return res
