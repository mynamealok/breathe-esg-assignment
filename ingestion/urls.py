from django.urls import path
from .views import *

urlpatterns = [

    path(
        "upload/sap/",
        SAPUploadView.as_view()
    ),

    path(
        "records/",
        ActivityListView.as_view()
    ),

    path(
        "issues/",
        IssueListView.as_view()
    ),

    path(
        "approve/<int:pk>/",
        ApproveRecordView.as_view()
    ),
    path(
    "upload/utility/",
    UtilityUploadView.as_view()
    ),
    path(
        "upload/travel/",
        TravelUploadView.as_view()
    ),
    path(
        "lock/<int:pk>/",
        LockRecordView.as_view()
    ),
]