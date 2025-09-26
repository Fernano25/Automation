import pytest
import logging

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Setup basic logging configuration for tests"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )