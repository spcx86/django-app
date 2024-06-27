import logging
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from supabase import create_client, Client

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    supabase_uid = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.supabase_uid:
            try:
                # Initialize Supabase client
                supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

                # Create or update user in Supabase
                response = supabase.auth.admin.create_user({
                    'email': self.email,
                    'email_confirm': True,
                    'user_metadata': {
                        'full_name': self.get_full_name(),
                    }
                })

                # Log the response to inspect its structure
                logger.debug(f"Supabase user creation response: {response}")

                # Correctly extract the user ID
                if response.user and response.user.id:
                    self.supabase_uid = response.user.id
                else:
                    logger.error(f"Supabase user creation failed: {response}")
                    raise ValueError("Supabase user creation failed.")

            except Exception as e:
                logger.error(f"Error creating Supabase user: {e}")
                raise e  # Reraise the exception to ensure the error is not swallowed

        super().save(*args, **kwargs)
