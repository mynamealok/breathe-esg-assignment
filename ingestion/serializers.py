from rest_framework import serializers
from .models import ActivityRecord


class ActivityRecordSerializer(serializers.ModelSerializer):

    source = serializers.CharField(
        source="raw_record.batch.source_type",
        read_only=True
    )

    class Meta:
        model = ActivityRecord

        fields = [
            "id",
            "activity_type",
            "quantity",
            "unit",
            "scope",
            "status",
            "source"
        ]