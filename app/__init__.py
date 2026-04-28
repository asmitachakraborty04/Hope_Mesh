from pathlib import Path

# Map legacy `app.*` imports to the existing HopeMesh package tree.
_HOPEMESH_ROOT = Path(__file__).resolve().parent.parent / "HopeMesh"
__path__ = [str(_HOPEMESH_ROOT)]
