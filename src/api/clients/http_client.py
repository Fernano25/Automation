import requests
from typing import Dict, Any, Optional
from src.utils.logger import TestLogger
from src.api.endpoints import Endpoints

class HttpClient:
    def __init__(self, base_url: str = Endpoints.BASE_URL.value):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = TestLogger(self.__class__.__name__)

    def _get_full_url(self, endpoint: str) -> str:
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        url = self._get_full_url(endpoint)
        self.logger.log_request(url, self.session.headers, params)
        
        response = self.session.get(url, params=params)
        self.logger.log_response(response.status_code, response.json())
        
        return response

    def post(self, endpoint: str, data: Optional[Dict] = None) -> requests.Response:
        url = self._get_url(endpoint)
        self.logger.log_request(url, self.session.headers, data)
        
        response = self.session.post(url, json=data)
        self.logger.log_response(response.status_code, response.json())
        
        return response

    def put(self, endpoint: str, data: Optional[Dict] = None) -> requests.Response:
        url = self._get_full_url(endpoint)
        self.logger.log_request(url, self.session.headers, data)
        
        response = self.session.put(url, json=data)
        self.logger.log_response(response.status_code, response.json())
        
        return response

    def delete(self, endpoint: str) -> requests.Response:
        url = self._get_full_url(endpoint)
        self.logger.log_request(url, self.session.headers)
        
        response = self.session.delete(url)
        self.logger.log_response(response.status_code, response.json() if response.content else {})
        
        return response