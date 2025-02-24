import pytest
import os
import sys
from pathlib import Path

# Add project root to Python path for tests
@pytest.fixture(autouse=True)
def add_project_path():
    project_root = Path(__file__).parent.parent
    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root)) 