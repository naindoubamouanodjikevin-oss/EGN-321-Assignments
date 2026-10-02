import pytest
from src.interpolation import linear_interpolate

def test_midpoint_interpolation():
    result = linear_interpolate(x=25, x1=20, y1=100, x2=30, y2=140)
    assert result == pytest.approx(120.0)

def test_interpolation_lower_bound_eval():
    result = linear_interpolate(x=20, x1=20, y1=100, x2=30, y2=140)
    assert result == pytest.approx(100.0)