from typing import Any, Dict
from pydantic import ValidationError
import json

class Assertions:
    @staticmethod
    def assert_status_code(actual: int, expected: int) -> None:
        assert actual == expected, f"Expected status {expected}, but got {actual}"

    @staticmethod
    def assert_response_time(actual: float, max_time: float) -> None:
        assert actual <= max_time, f"Response time {actual}s exceeds maximum {max_time}s"

    @staticmethod
    def assert_schema(response_data: Dict[str, Any], schema: Any) -> None:
        try:
            schema(**response_data)
        except ValidationError as e:
            raise AssertionError(f"Schema validation failed: {e}")

    @staticmethod
    def assert_json_contains(response_data: Dict[str, Any], expected_data: Dict[str, Any]) -> None:
        for key, value in expected_data.items():
            assert key in response_data, f"Key '{key}' not found in response"
            assert response_data[key] == value, f"Value for '{key}' doesn't match"

    @staticmethod
    def assert_list_length(items: list, expected_length: int) -> None:
        assert len(items) == expected_length, f"Expected {expected_length} items, got {len(items)}"