import os
from typing import Any

from django.core.exceptions import ImproperlyConfigured

from dotenv import load_dotenv; load_dotenv()


MISSING_VALUE = object()

def get_env_value(env_variable: str, default: Any=MISSING_VALUE) -> str | Any:
    """
    Get the environment variable value or return default value.
    Try only access this from `settings.py` file.
    """
    try:
        return os.environ[env_variable]
    except KeyError:
        if default != MISSING_VALUE:
            return default

        raise ImproperlyConfigured(f'Set {env_variable} env variable or provide default value')