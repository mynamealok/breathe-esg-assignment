# Design Decisions

## SAP Source

Chosen format:
CSV export

Reason:
CSV exports are commonly generated from SAP reporting tools and are easy to prototype within four days.

Handled:
- Quantity
- Unit

Ignored:
- Full SAP IDoc structure
- BAPI integrations

---

## Utility Source

Chosen format:
CSV export from utility portals

Reason:
Facilities teams commonly download billing data as CSV.

Handled:
- Consumption (kWh)
- Billing period

Ignored:
- Tariff calculations
- Demand charges

---

## Travel Source

Chosen format:
CSV export representing Concur/Navan data

Reason:
Travel systems often export booking and trip reports as CSV.

Handled:
- Travel type
- Distance

Ignored:
- Live API integrations
- Airport geocoding

---

## Approval Workflow

Reason:
Analysts review records before locking them for audit.

Workflow:

PENDING → APPROVED → LOCKED