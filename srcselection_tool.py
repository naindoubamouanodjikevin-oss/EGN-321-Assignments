"""
selection_tool.py
Main engineering selection tool implementing exact lookup, linear interpolation,
range checks, and refusal logic.
"""

from typing import Dict, Any, Tuple
from src.lookup_tables import LOOKUP_TABLES
from src.interpolation import linear_interpolate


def select_coefficient(valve_family: str, temperature_c: float) -> Dict[str, Any]:
    """
    Selects or interpolates an engineering coefficient for a given valve family and temperature.
    
    Raises:
        ValueError: If valve_family is not supported or if temperature_c is outside 
                   the supported engineering data range.
    """
    # 1. Validate Valve Family
    if valve_family not in LOOKUP_TABLES:
        raise ValueError(f"Unsupported valve_family: {valve_family}")
    
    table = LOOKUP_TABLES[valve_family]
    
    # 2. Determine Supported Range
    min_temp = table[0][0]
    max_temp = table[-1][0]
    supported_range = (min_temp, max_temp)
    
    # 3. Validate Range (Refuse Extrapolation)
    if temperature_c < min_temp:
        raise ValueError(
            f"temperature_c {temperature_c} is below the supported minimum {min_temp}"
        )
    if temperature_c > max_temp:
        raise ValueError(
            f"temperature_c {temperature_c} exceeds the supported maximum {max_temp}"
        )
    
    # 4. Handle Exact Table Matches
    for temp, coeff in table:
        if temp == temperature_c:
            return {
                "valve_family": valve_family,
                "temperature_c": float(temperature_c),
                "coefficient": float(coeff),
                "method": "exact",
                "lower_point": (temp, coeff),
                "upper_point": (temp, coeff),
                "supported_range": supported_range,
            }
            
    # 5. Identify Surrounding Rows & Perform Linear Interpolation
    lower_point: Tuple[float, float] = table[0]
    upper_point: Tuple[float, float] = table[-1]
    
    for i in range(len(table) - 1):
        if table[i][0] <= temperature_c <= table[i + 1][0]:
            lower_point = table[i]
            upper_point = table[i + 1]
            break
            
    x1, y1 = lower_point
    x2, y2 = upper_point
    
    calc_coeff = linear_interpolate(temperature_c, x1, y1, x2, y2)
    
    return {
        "valve_family": valve_family,
        "temperature_c": float(temperature_c),
        "coefficient": round(calc_coeff, 4),
        "method": "interpolation",
        "lower_point": lower_point,
        "upper_point": upper_point,
        "supported_range": supported_range,
    }