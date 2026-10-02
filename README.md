# Engineering Valve Coefficient Lookup Tool (EGN321 Module 3)

## Overview
This Python tool replaces an auditing-resistant legacy spreadsheet selection model. It provides linear interpolation between bounded empirical engineering values and strictly refuses out-of-bounds requests.

## Data Source & Supported Families
Data sourced from `VALVE_SELECTION_rev3.xlsx`.

| Valve Family | Supported Range (°C) |
| :--- | :--- |
| **VX-100** | 20°C – 100°C |
| **VX-200** | 10°C – 90°C |

## Operational Logic
1. **Exact Lookup:** If requested temperature exists on a known row, that value is returned directly without interpolation.
2. **Linear Interpolation:** For temperatures bounded inside table limits, interpolation uses:
   $$y = y_1 + \left(\frac{x - x_1}{x_2 - x_1}\right) \times (y_2 - y_1)$$
3. **Refusal Rule:** Attempts to perform extrapolation below the minimum or above the maximum supported limit raise a `ValueError`. Unsupported valve families raise a `ValueError`.

## Running Automated Tests
Run tests using `pytest`:
```bash
pytest -v