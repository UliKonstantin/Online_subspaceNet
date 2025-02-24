import os
from pathlib import Path
import sys
import pytest

# Import our package to initialize paths
import subspace_kalman_package

@pytest.mark.imports
def test_imports():
    # Print current sys.path to see all import locations
    print("\nPython path:")
    for p in sys.path:
        print(f"  {p}")
    
    # Import all required dependencies first
    try:
        import torch
        import numpy as np
        import sklearn
        import scipy
        import matplotlib.pyplot as plt
        import tqdm
    except ImportError as e:
        print(f"\nDependency import failed: {e}")
        print("Please install required dependencies:")
        print("pip install torch numpy scikit-learn scipy matplotlib tqdm")
        raise
    
    # Print KalmanNet directory contents
    kalman_path = Path(__file__).parent.parent / 'dependencies' / 'KalmanNet'
    print("\nKalmanNet directory contents:")
    print(f"Directory exists: {kalman_path.exists()}")
    print("Files:")
    for f in kalman_path.glob('**/*.py'):
        print(f"  {f.relative_to(kalman_path)}")
    
    # Add KalmanNet root to path first
    #sys.path.insert(0, str(kalman_path))
    
    try:
        from KNet.KalmanNet_nn import KalmanNetNN
    except ImportError as e:
        print(f"\nKalmanNet import failed: {e}")
        raise
    
    assert KalmanNetNN is not None

    # Print DCD-MUSIC directory contents
    dcd_path = Path(__file__).parent.parent / 'dependencies' / 'DCD-MUSIC'
    print("\nDCD-MUSIC directory contents:")
    print(f"Directory exists: {dcd_path.exists()}")
    print("Files:")
    for f in dcd_path.glob('**/*.py'):
        print(f"  {f.relative_to(dcd_path)}")
    
    # Add DCD-MUSIC paths
    #sys.path.insert(0, str(dcd_path))
    #sys.path.insert(0, str(dcd_path / 'src'))
    
    try:
        from subspace_kalman_package.models_pack import (
            DCDMUSIC, 
            SubspaceNet, 
            TransMUSIC,
            DeepAugmentedMUSIC,
            DeepRootMUSIC,
            DeepCNN,
            ParentModel
        )
        assert all(x is not None for x in [
            DCDMUSIC, SubspaceNet, TransMUSIC, 
            DeepAugmentedMUSIC, DeepRootMUSIC, 
            DeepCNN, ParentModel
        ])
    except ImportError as e:
        print(f"\nDCD-MUSIC models import failed: {e}")
        raise

    try:
        from subspace_kalman_package.methods_pack import (
            Beamformer,
            CsEstimator,
            ESPRIT,
            MLE,
            MUSIC,
            RootMusic,
            root_music,
            SubspaceMethod
        )
        assert all(x is not None for x in [
            Beamformer, CsEstimator, ESPRIT,
            MLE, MUSIC, RootMusic, root_music,
            SubspaceMethod
        ])
    except ImportError as e:
        print(f"\nDCD-MUSIC methods import failed: {e}")
        raise 