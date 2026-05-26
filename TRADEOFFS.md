# Tradeoffs

## 1. Authentication Not Implemented

Reason:
Focus was placed on ingestion and review workflow.

Future:
Add JWT authentication and role-based access.

---

## 2. Real SAP Integration Not Implemented

Reason:
Prototype uses CSV exports instead of live SAP APIs.

Future:
Connect SAP OData services.

---

## 3. Background Processing Not Implemented

Reason:
Uploads are processed synchronously for simplicity.

Future:
Use Celery and Redis for large files.