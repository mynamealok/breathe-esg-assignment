from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UploadBatch(models.Model):

    SOURCE_CHOICES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL")
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class RawRecord(models.Model):

    batch = models.ForeignKey(
        UploadBatch,
        on_delete=models.CASCADE
    )

    raw_data = models.JSONField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class ActivityRecord(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("LOCKED", "LOCKED")
    ]

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE,
        null= True,
        blank= True
    )

    activity_type = models.CharField(
        max_length=100
    )

    quantity = models.FloatField()

    unit = models.CharField(
        max_length=50
    )

    scope = models.CharField(
        max_length=20
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )


class ReviewIssue(models.Model):

    activity = models.ForeignKey(
        ActivityRecord,
        on_delete=models.CASCADE
    )

    issue_text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class AuditLog(models.Model):

    activity = models.ForeignKey(
        ActivityRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=200
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )