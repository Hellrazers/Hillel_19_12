from typing import Any, List

from lib.response_model import ResponseModel


class ExpensesModel:

    def __init__(self, data: dict):
        self.id: int = data.get("id")
        self.carId: int = data.get("carId")
        self.reportedAt: str = data.get("reportedAt")
        self.mileage = data.get("mileage") #['carBrandId]
        self.liters = data.get("liters")
        self.totalCost = data.get("totalCost")

class ExpenseResponseModel(ResponseModel):
    status_code: int
    response_status: str
    errors: Any
    payload: Any
    resp_obj: Any
    data: ExpensesModel = None

    def __init__(self, resp: ResponseModel):
        self.status_code = resp.status_code
        self.response_status = resp.response_status
        self.errors = resp.error
        self.payload = resp.payload
        self.resp_obj = resp.resp_obj
        if resp.data != None:
            self.data = ExpensesModel(resp.data)


class ExpensesResponseModel(ResponseModel):
    status_code: int
    response_status: str
    errors: Any
    payload: Any
    resp_obj: Any
    data: List[ExpensesModel] = None

    def __init__(self, resp: ResponseModel):
        self.status_code = resp.status_code
        self.response_status = resp.response_status
        self.errors = resp.error
        self.payload = resp.payload
        self.resp_obj = resp.resp_obj
        if resp.data != None:
            self.data = [ExpensesModel(item) for item in resp.data]