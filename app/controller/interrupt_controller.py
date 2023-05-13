import uuid

from fastapi import UploadFile

from app.models.response.default_response_model import DefaultResponseModel
from app.service.interrupt_service import InterruptService


class InterruptController:

    @staticmethod
    async def upload_file(file: UploadFile) -> DefaultResponseModel:
        try:
            unique_id: str = uuid.uuid4().__str__()
            InterruptService.upload_file(unique_id, file)
            return DefaultResponseModel(
                message="File upload in progress please check status with unique id",
                status="success",
                status_code=200,
                data={
                    "unique_id": unique_id
                }
            )
        except Exception as exception:
            pass
