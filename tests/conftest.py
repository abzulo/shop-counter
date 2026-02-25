from copy import deepcopy
from pathlib import Path
import sys

import pytest

# Ensure repository root is importable when pytest chooses tests/ as rootdir.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shop_counter.data import products


@pytest.fixture(autouse=True)
def reset_products():
    """Ensure each test gets a clean copy of the in-memory inventory."""
    original = deepcopy(products)
    yield
    products.clear()
    products.update(original)
