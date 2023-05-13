from fastapi import APIRouter, UploadFile

from app.controller.interrupt_controller import InterruptController
from app.models.response.default_response_model import DefaultResponseModel

interrupt_router: APIRouter = APIRouter(
    prefix="/interrupt",
    tags=["Interrupt"],
)


@interrupt_router.post(
    "/upload_file",
    response_model=DefaultResponseModel,
    response_model_exclude_none=True,
)
def upload_file(file: UploadFile):
    try:
        response: DefaultResponseModel = InterruptController.upload_file(file)
        return response
    except Exception as exception:
        pass
