import urlparse
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from constance import config


def login_required_if_private(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that redirects the user to the log-in page if the
    site is configured to be private and the user is not logged in.
    """
    actual_decorator = user_passes_test(
        lambda u: (not config.PRIVATE) or u.is_authenticated(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
