from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    supabase_uid = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.supabase_uid:
            # Initialize Supabase client
            from supabase import create_client, Client
            from django.conf import settings
            supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

            # Create or update user in Supabase
            supabase_user = supabase.auth.admin.create_user({
                'email': self.email,
                'email_confirm': True,
                'user_metadata': {
                    'full_name': self.get_full_name(),
                }
            })
            self.supabase_uid = supabase_user.id

        super().save(*args, **kwargs)