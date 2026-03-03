from json import JSONDecodeError
from typing import Optional, Any

from requests import Response


class ResponseModel:
    def __init__(self, resp):
        self.resp_obj: Response = resp
        self.status_code: int = resp.status_code
        self.payload: Optional[Any] = self._get_payload()
        self.error: Optional[Any] = self._extract_error()
        self.data: Optional[Any] = self._get_data()
        self.meta: Optional[Any] = self._get_meta()
        self.linked: Optional[Any] = self._get_linked()
        self.response_status = self._get_response_status()

    def _get_payload(self):
        try:
            return self.resp_obj.json()
        except JSONDecodeError:
            return self.resp_obj.text

    def _get_data(self):
        if isinstance(self.payload, dict):
            return self.payload.get("data")
        return None

    def _get_linked(self):
        if isinstance(self.payload, dict):
            return self.payload.get("linked")
        return None

    def _get_meta(self):
        if isinstance(self.payload, dict):
            return self.payload.get("meta")
        return None

    def _get_response_status(self):
        if isinstance(self.payload, dict):
            return self.payload.get("responseStatus")
        return None

    def _extract_error(self):
        if isinstance(self.payload, dict):
            return self._extract_errors(self.payload)
        return {}

    @staticmethod
    def _extract_errors(payload: dict):
        if payload.get("errors"):
            return payload.get("errors")
        elif payload.get("error"):
            return payload.get("error")
        else:
            return None