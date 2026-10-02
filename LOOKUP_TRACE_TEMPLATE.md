# Lookup Trace Analysis (VALVE_SELECTION_rev3.xlsx)

## Criteria Identification
- **First Lookup Criterion:** `Valve Family` (e.g., VX-100, VX-200)
- **Second Lookup Criterion:** `Operating Temperature` (°C)[cite: 1]

## Data & Logic Inspection
- **Data Location:** Engineering tables are located in the legacy lookup sheets/CSV, mapping temperatures to specific valve family coefficients[cite: 1].
- **Spreadsheet Table Selection:** The legacy spreadsheet uses nested `VLOOKUP`, `INDEX/MATCH`, or deeply nested `IF` statements to route the selection to specific data ranges based on the valve family.
- **Exact Matches:** When the input temperature exactly matches a table row, the spreadsheet returns the corresponding stored coefficient.
- **Between-Row Behavior:** The legacy spreadsheet either rounds to the nearest row or uses manual slope calculations to interpolate between known rows.
- **Outside-Range Behavior:** The legacy workbook may silently extrapolate using the nearest linear trend or fail with unhelpful `#N/A` / incorrect fallback values.

## Refinement Rationale
The legacy spreadsheet buries data ranges, interpolation formulas, and threshold checks inside multi-cell formulas. This makes it difficult to audit and safe usage uncertain. By migrating to a structured Python tool, we cleanly separate table data from execution logic, enforce explicit boundary limits, and guarantee extrapolation refusal[cite: 2, 4].