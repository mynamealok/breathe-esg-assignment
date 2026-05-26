# Data Model

## Tenant

Represents a client organization.

Fields:
- id
- name

Reason:
Supports multi-tenancy. Multiple companies can use the system.

---

## UploadBatch

Tracks every upload operation.

Fields:
- tenant
- source_type
- uploaded_at

Reason:
Provides source-of-truth tracking and upload history.

---

## RawRecord

Stores original incoming data exactly as received.

Fields:
- batch
- raw_data
- created_at

Reason:
Maintains auditability and preserves source data.

---

## ActivityRecord

Normalized ESG activity data.

Fields:
- activity_type
- quantity
- unit
- scope
- status

Reason:
Creates a common format across SAP, Utility and Travel data.

---

## ReviewIssue

Stores suspicious or invalid records.

Fields:
- activity
- issue_text

Reason:
Allows analyst review before approval.

---

## AuditLog

Tracks workflow actions.

Fields:
- activity
- action
- timestamp

Reason:
Provides audit trail for approvals and locks.

---

## Scope Mapping

SAP Fuel → Scope 1

Electricity → Scope 2

Travel → Scope 3