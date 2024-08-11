from fastapi import APIRouter, Path, Body, Query
from fastapi.responses import JSONResponse

prefix = "/api/v1/accounts"
router = APIRouter(prefix=prefix, tags=["accounts"])

