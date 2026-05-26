import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import ActivityRecordSerializer


class SAPUploadView(APIView):

    def post(self, request):

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=400
            )

        try:
            df = pd.read_csv(uploaded_file)

        except Exception:
            return Response(
                {"error": "Invalid CSV file"},
                status=400
            )

        tenant, _ = Tenant.objects.get_or_create(
            name="Demo Company"
        )

        batch = UploadBatch.objects.create(
            tenant=tenant,
            source_type="SAP"
        )

        count = 0

        for _, row in df.iterrows():

            raw_record = RawRecord.objects.create(
                batch=batch,
                raw_data=row.to_dict()
            )

            qty = float(row["Qty"])

            activity = ActivityRecord.objects.create(
                raw_record=raw_record,
                activity_type="Fuel",
                quantity=qty,
                unit=row["Unit"],
                scope="Scope1"
            )

            if qty < 0:

                ReviewIssue.objects.create(
                    activity=activity,
                    issue_text="Negative Fuel Quantity"
                )

            count += 1

        return Response({
            "message": f"{count} SAP records uploaded"
        })


class UtilityUploadView(APIView):

    def post(self, request):

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=400
            )

        try:
            df = pd.read_csv(uploaded_file)

        except Exception:
            return Response(
                {"error": "Invalid CSV file"},
                status=400
            )

        tenant, _ = Tenant.objects.get_or_create(
            name="Demo Company"
        )

        batch = UploadBatch.objects.create(
            tenant=tenant,
            source_type="UTILITY"
        )

        count = 0

        for _, row in df.iterrows():

            raw = RawRecord.objects.create(
                batch=batch,
                raw_data=row.to_dict()
            )

            kwh = float(row["kWh"])

            activity = ActivityRecord.objects.create(
                raw_record=raw,
                activity_type="Electricity",
                quantity=kwh,
                unit="kWh",
                scope="Scope2"
            )

            if kwh < 0:

                ReviewIssue.objects.create(
                    activity=activity,
                    issue_text="Negative Electricity Consumption"
                )

            if kwh > 50000:

                ReviewIssue.objects.create(
                    activity=activity,
                    issue_text="Unusually High Electricity Consumption"
                )

            count += 1

        return Response({
            "message": f"{count} utility records uploaded"
        })


class TravelUploadView(APIView):

    def post(self, request):

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=400
            )

        try:
            df = pd.read_csv(uploaded_file)

        except Exception:
            return Response(
                {"error": "Invalid CSV file"},
                status=400
            )

        tenant, _ = Tenant.objects.get_or_create(
            name="Demo Company"
        )

        batch = UploadBatch.objects.create(
            tenant=tenant,
            source_type="TRAVEL"
        )

        count = 0

        for _, row in df.iterrows():

            raw = RawRecord.objects.create(
                batch=batch,
                raw_data=row.to_dict()
            )

            distance = float(row["DistanceKM"])

            activity = ActivityRecord.objects.create(
                raw_record=raw,
                activity_type=row["TravelType"],
                quantity=distance,
                unit="km",
                scope="Scope3"
            )

            if (
                row["TravelType"] == "Flight"
                and distance < 100
            ):

                ReviewIssue.objects.create(
                    activity=activity,
                    issue_text="Suspicious Flight Distance"
                )

            count += 1

        return Response({
            "message": f"{count} travel records uploaded"
        })


class ActivityListView(APIView):

    def get(self, request):

        records = ActivityRecord.objects.all()

        serializer = ActivityRecordSerializer(
            records,
            many=True
        )

        return Response(serializer.data)


class IssueListView(APIView):

    def get(self, request):

        issues = ReviewIssue.objects.all()

        data = []

        for issue in issues:

            data.append({
                "record_id": issue.activity.id,
                "issue": issue.issue_text
            })

        return Response(data)


class ApproveRecordView(APIView):

    def post(self, request, pk):

        try:

            record = ActivityRecord.objects.get(
                id=pk
            )

        except ActivityRecord.DoesNotExist:

            return Response(
                {"error": "Record not found"},
                status=404
            )

        record.status = "APPROVED"
        record.save()

        AuditLog.objects.create(
            activity=record,
            action="APPROVED"
        )

        return Response({
            "message": "Record Approved"
        })


class LockRecordView(APIView):

    def post(self, request, pk):

        try:

            record = ActivityRecord.objects.get(
                id=pk
            )

        except ActivityRecord.DoesNotExist:

            return Response(
                {"error": "Record not found"},
                status=404
            )

        if record.status != "APPROVED":

            return Response(
                {"error": "Approve first"},
                status=400
            )

        record.status = "LOCKED"
        record.save()

        AuditLog.objects.create(
            activity=record,
            action="LOCKED"
        )

        return Response({
            "message": "Record Locked"
        })