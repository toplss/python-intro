from django.db import models
import rest_framework
from web_toon.views import create_post

# Create your models here.
class Admins(models.Model):
    admin_group_id = models.IntegerField(default=0,null=True)
    manager_id = models.CharField(max_length=45, null=True)
    name = models.CharField(max_length=45, null=True)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    otp_info = models.TextField(default=0)
    personal_access_tokens = models.CharField(max_length=100)
    permission_function = models.TextField()
    permissions_menu = models.TextField()
    permissions_site = models.TextField()
    role_code = models.CharField(max_length=6)
    admin_status_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    password_changed = models.DateTimeField(auto_now=True)
    use_yn = models.CharField(max_length=1)
    note = models.CharField(max_length=45)
    admin_id = models.IntegerField()
    admin_board_noti = models.TextField()
    utc = models.CharField(max_length=10)
    Lang = models.CharField(max_length=2)
    logout_time = models.IntegerField(default=0)

    class Meta:
        db_table = 'admins'