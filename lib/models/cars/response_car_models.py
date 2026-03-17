from typing import Any

from lib.response_model import ResponseModel


class CarsModel:

    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.carBrandId = data.get("carBrandId") #['carBrandId]
        self.carModelId = data.get("carModelId")



class CarResponseModel(ResponseModel):
    status_code: int
    response_status: str
    errors: Any
    payload: Any
    resp_obj: Any
    data: CarsModel = None

    def __init__(self, resp: ResponseModel):
        self.status_code = resp.status_code
        self.response_status = resp.response_status
        self.errors = resp.error
        self.payload = resp.payload
        self.resp_obj = resp.resp_obj
        if resp.data != None:
            self.data = CarsModel(resp.data)
