"""
lookup_tables.py
Contains engineering lookup tables mapping Valve Families and Operating Temperatures (°C)
to their corresponding flow/performance coefficients.
"""

LOOKUP_TABLES = {
    "VX-100": [
        (20, 0.88),
        (40, 0.93),
        (60, 0.99),
        (80, 1.06),
        (100, 1.14),
    ],
    "VX-200": [
        (10, 1.15),
        (30, 1.20),
        (50, 1.27),
        (70, 1.39),
        (90, 1.52),
    ],
}