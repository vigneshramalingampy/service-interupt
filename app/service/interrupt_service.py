from fastapi import UploadFile

from app.database.interrupt_database import InterruptDatabase


class InterruptService:

    @staticmethod
    def upload_file(unique_id: str, file: UploadFile) -> None:
        try:
            InterruptDatabase.upload_file(unique_id, file)
        except Exception as exception:
            pass
