from typing import Literal, Any, Optional

from pydantic import BaseModel

STATUS_TYPES = Literal["success", "error"]


class DefaultResponseModel(BaseModel):
    message: str
    status: STATUS_TYPES
    status_code: int
    error_details: Optional[str] = None
    data: Optional[Any] = None
