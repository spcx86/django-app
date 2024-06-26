from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from supabase import create_client, Client
from django.conf import settings


class SupabaseSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        # Initialize Supabase client
        supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

        # Create or update user in Supabase
        supabase_user = supabase.auth.admin.create_user({
            'email': user.email,
            'email_confirm': True,
            'user_metadata': {
                'full_name': user.get_full_name(),
            }
        })

        return user