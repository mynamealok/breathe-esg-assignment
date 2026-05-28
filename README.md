# Breathe ESG Ingestion Prototype

## Overview
A Django REST + React application for ESG data ingestion, normalization, analyst review and audit approval workflow.

## Features

- SAP CSV Upload
- Utility CSV Upload
- Travel CSV Upload
- Data Normalization
- Scope 1 / 2 / 3 Classification
- Suspicious Record Detection
- Analyst Approval Workflow
- Audit Locking
- Audit Logs
- Multi-Tenant Data Model

## Tech Stack

Backend:
- Django
- Django REST Framework
- SQLite
- Pandas

Frontend:
- React
- Axios

## Workflow

Upload Data
↓
Normalize Records
↓
Detect Issues
↓
Analyst Review
↓
Approve
↓
Lock For Audit

## Run Backend

pip install -r requirements.txt

python manage.py migrate

## Live Links

Frontend:
https://breathe-esg-assignment-k5u2.vercel.app/
Backend API:
https://breathe-esg-assignment-production-5f11.up.railway.app/api/records/

## Run Frontend

npm install

npm run dev
