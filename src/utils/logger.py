import logging
import json
from typing import Dict, Any

class TestLogger:
    def __init__(self, test_name: str):
        self.logger = logging.getLogger(test_name)
        self.logger.setLevel(logging.DEBUG)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message: str):
        self.logger.info(message)

    def log_debug(self, message: str):
        self.logger.debug(message)

    def log_request(self, url: str, headers: Dict[str, str], payload: Any = None):
        self.log_debug(f"Request URL: {url}")
        self.log_debug(f"Request Headers: {json.dumps(headers, indent=2)}")
        if payload:
            self.log_debug(f"Request Payload: {json.dumps(payload, indent=2)}")

    def log_response(self, status_code: int, response_data: Any):
        self.log_info(f"Status Code: {status_code}")
        self.log_debug(f"Response: {json.dumps(response_data, indent=2)}")