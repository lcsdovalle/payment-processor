from fastapi import APIRouter, File, UploadFile, Depends

from app.handlers.payment_handler import payment_handler
from app.dependencies.auth import get_authenticated_user

router = APIRouter()


@router.post("/payment/bulk/")
async def upload_csv(
    file: UploadFile = File(...), user: dict = Depends(get_authenticated_user)
):
    return await payment_handler.get_result(file=file)
