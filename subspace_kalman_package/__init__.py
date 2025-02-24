import os
import sys
from pathlib import Path

# Add dependencies to Python path
REPO_ROOT = Path(__file__).parent.absolute()
KALMAN_PATH = REPO_ROOT / 'dependencies' / 'KalmanNet'
DCD_PATH = REPO_ROOT / 'dependencies' / 'DCD-MUSIC'

# Add DCD-MUSIC paths
DCD_SRC_PATH = DCD_PATH / 'src'
DCD_METHODS_PATH = DCD_PATH / 'src' / 'methods_pack'
DCD_MODELS_PATH = DCD_PATH / 'src' / 'models_pack'

# Verify paths exist
if not KALMAN_PATH.exists():
    raise ImportError(f"KalmanNet path not found: {KALMAN_PATH}")
if not DCD_PATH.exists():
    raise ImportError(f"DCD-MUSIC path not found: {DCD_PATH}")

# Add all paths to Python path
sys.path.insert(0, str(DCD_MODELS_PATH))  # Highest priority
sys.path.insert(0, str(DCD_METHODS_PATH))
sys.path.insert(0, str(DCD_SRC_PATH))
sys.path.insert(0, str(DCD_PATH))
sys.path.insert(0, str(KALMAN_PATH))

# Import and expose packages
from src.models_pack import *
from src.methods_pack import * 