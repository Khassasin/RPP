from django.db import models


class Customers(models.Model):
    phone_number = models.TextField(default='')


class Reasons(models.Model):
    reason_text = models.TextField(default='')


class Calls(models.Model):
    cmr_id = models.ForeignKey(Customers, on_delete=models.CASCADE, db_column='cmr_id')
    call_date = models.DateTimeField(default='')
    issue_resolved = models.BooleanField(default=0)


class Resolutions(models.Model):
    cl_id = models.ForeignKey(Calls, on_delete=models.CASCADE, db_column='cl_id')
    resolution_text = models.TextField(editable=True)


class Call_Reasons(models.Model):
    cl_id = models.ForeignKey(Calls, on_delete=models.CASCADE, db_column='cl_id')
    reason_id = models.ForeignKey(Reasons, on_delete=models.CASCADE, db_column='reason_id')
