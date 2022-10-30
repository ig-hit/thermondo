import base64
import datetime
import os
import pathlib
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = pathlib.Path(__file__).resolve().parent

APPLICATION_STAGE = os.environ.get("APPLICATION_STAGE", "dev")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#+&wo)*z!b2wsf3xk62pzfu15$s1nzkyzkm68lrvpx+h-v5q$z"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = APPLICATION_STAGE == "dev"

ALLOWED_HOSTS = ["0.0.0.0"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "taggit",
    "rest_framework",
    "rest_framework_simplejwt",
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "notes.apps.NotesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "service.urls"
WSGI_APPLICATION = "service.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DATABASE_NAME", "thermondo"),
        "USER": os.environ.get("DATABASE_USER", "postgres"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "postgres"),
        "HOST": os.environ.get("DATABASE_HOST", "0.0.0.0"),
        "PORT": os.environ.get("DATABASE_PORT", "3602"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("users.auth.TokenAuth",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": (),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "TEST_REQUEST_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.MultiPartRenderer",
    ),
}

# https://gist.github.com/ygotthilf/baa58da5c3dd1f69fae9
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "AUTH_HEADER_TYPES": ("JWT", "Bearer"),
    "ALGORITHM": "RS256",
    "SIGNING_KEY": base64.b64decode(
        os.environ.get(
            "JWT_SIGNING_KEY_B64",
            "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlKS1FJQkFBS0NBZ0VBcjdqTXBOckJTQU9GYjdZL0VRMGUyalRYMjMxeDMzRVJZVGZ0aWZnRDNtVExwcVpzCld1Rk1TQUpSNlRCejJIb0d4eVBoeTNibTduRnhJb2Z4U05xOHhZVFg2dUtMWDJodW1TcTYvSnRibldnRDBST0wKcXM3alF6MFgwWkxaUFFUa3YvbEJjdzNiSmw2NVJybkR2WGFaNWVHelJDbFd1L1lBaHhOZzhwYVRCVmk5ZmROTwpZSFQwUHlNTkM5Smk4V3NpbVAvckxWcjhqOFUyUCtMZ0huTjVXMmhKMytHT24vQUFlTHJtYjdzT0t4SU9YdmZMClo1USs1Nlk0MWF5VGR6VWxFSVE5MmUvaEFrOENIQllPWC9yY2tvejBXSUtYRmNSZys3T1VweUExeEhSdmVtOGkKTkUwN0tjNVl6My8zbm55M3ZIZ21kRDBocVNMU1pWS2Z5NTBuN1JTdmZTU3RWK3VlbVJKQnRWNFprUXpLdDgxQwoyYmxTQmljVHRXZVhEUWw5U2pvdXN4U3U1ZGlPZ3VKbHFGYjFtTkpsMktZRDM1QVYrK1BMMzJtRlZ2VlZGTVB1CndiT3BRTDdtc0sxYjE5WW5OdjlaWCtFazQyN2tDT2k2NGd6ZmdOZzZXNit1NllDUnJaOGFSMGc2ZGdCcHZMWjkKYno0Y3htNENpTDcyODFtdEoxTjZDMUxjVGN5aVlpZUcwY0p2akdpbVgxNCtDZHgzemdYQVJGMVNVZE94NTZzRAordnpnd1BJZThWYUZsYUxUa20xT0p0VFIrd2pRVzNCeEVWZmJ1RFJvd1JRMy9aclpXYXR2eFFYTmFHZEJRVGhSCnlsTHd5RlZNeUJmdm9ITWFTQ0JIWXlSdWZ4UjY1MWhBZFdZbXFRMFNOYjYzUTk0cVIrSGh1L010dE5jQ0F3RUEKQVFLQ0FnQk8yYjM2dTY2L2dkVCtxK2pnM2VKYVNCd1VnZFgzVGVWZW1wb2NydzROWFcyRSttamszdlE3Mjg2bAp0UGhHeTNyL0lUclE4aW51RlRtUEpURkFYK2NWT3Vjb256K3JNRkZ3cVp2K2ZqZytDYzZzb3ZpcFRPenQzeHd4CkRwUXNyV1Y0UDREKy85aTIvd3Bra2pjamJYVGhrc1crY0U1YlNhZ3k5SjhzUENUODRUVW1vUXNxZlZDY2hEMzIKY0JHMkF6MGpLck45UnJiT1ROQnJHb00zSnRudUNuNGIyRHNIeWNwc1luSEU4VXNLU0svcUxZYzRrMjBteFkvNwpVZFZhU0o2NUtwNFdqVzJLZTZtV3NNOENncTgzazhpUmJ3Z2MzR0lva0F6RWNjK3V1QkROLzlCNVo2NkVzL05tCktTWVVHQ0xhajQreDJUeWhpTjZnV05NYnF3bWV1a1dmTzNpZGVpZ0FPckpHelZuYSsxT3hQaW5ubkpmL24wRWYKbTBadWhuaDBUOHVWeFptSlIvNjFPUFpiOUpVTGdDS253NGNOWVVPNnN1cEJTTVdKczZ2ZnlwRHR1UklJNVZUSgptNllRUDNVK2FycmdpQ1Jtd0d6bHRDbjQ4WVhiaVBnNzFIbjdRUmJUR1lnUVF4SUJMNEl6SjJJbWZiQm9VU1VMCmRGQmRMR2phQmpzMHUvMnhWMFNYZnJrTWNUbXBwYjNMdlRtb3FrbE5uSmdSOHJqOFBhbkxlNjlPYloxTHEvZWMKNkljSUlzakVrQ1pnTnpvQittUkZCU05hYUE5TjZUZWFQUlI1Uyt1K2haMnI3VzdBbXpTcCtPWFRZN3Z4dVUwaApLVWlkdmllNWlLZ1lHbFlnTVMvc0JsdTVTMlY2bkdQNzhnZlhENFlhNmhnNk93Qm1BUUtDQVFFQTRweFlhSUlpCkdIcDFGSlIxWW9xNm1lTmY2RjFocEFXQXlVTnFBdFB6VjlaUThHRlV4a2Z5Tjd6eFJxTTdmMzNGclpQczhMQWYKdUgyQkw4ZkpablhOeGpmSndZeXpXSTY5a1J0aUkrUTRhVk56M09WcHl6bXRaQkdrMVBQWERJR3hUOGo5Wm9Gegp3eW5EekpYRDNWcFY0MGNodWpYUmFTSERURjZaRy9kTVZobUNYY0d0N3FXNnljQ2pMRU1ncGdBMWNFbnd0bjhECnpiVVJnVVJCZGVuajRzTktvcHo2OE4vT3FPc1ZzOFc1bjZ3dC81bEhJdEJPckYrUWFpYncrb3VVcFEwWnA3ZjgKbnNGNm10d1U0SVJWZnhZY0R0NjlSTDZiQ2tnVFFPUTd0RURXWFdTL1FjZzlmNmdsb3NvYzRvaDRxcytmTGVEOAord3NDNG5uOW5jZmZHUUtDQVFFQXhvTG5jUWNPOE9aWkxGQjVwZ2gvV2tNbzhLTm1NdFIrTXkvYURLNzFYazBMCkMyZWs2VzNKUmUvMDJYL3g1bHpOcXErV3NVeGNDMEp3TXY5MEFEYzFySThPWFpzNmozbkRtaXp6M0ZmRFQ4OEwKajdWVFlNODVueUFPakltbEZoclhlM1R5cGs1NDJOT0tzSk14Sk8rd0hqaFBhVXFQV1JsU3lYOTVUaEs0bDNFTAo1YWhBZjFvZFJtSEJ2UUF1cDJLU0IrVlZXV3c5TGMycndKck9LVlVVQytaMGwraHh1a2hSTWcyZUVtdFBRSkc5CldoeWl0ZlRySTQ4cFlERldsY2JrOHNIYlZjN3J6M3FycUcxZlEvbElUZkFMYW43c0dncHZJSy9LN2hTR1pJd1QKZHRMQlpGWVQxVTlNaEtWdEVOeEJvM1RMMjd6Wk5WSzJncmg5UXNmaGJ3S0NBUUJQcXFkcUZsWG1SU2JrRlUwdgpWNVpDZzYwMEE2QlFDWjg5SW5ZaWlHRUVnRlAwTGtPZmNhdTE3TGJtSG56TVZXc3BtdGV4eGpsZ29yN0lEWFRBCmtLbkhCZFhvTlk3WGsxY1JySTdVRDJmRm41RWNGNHNaNXkwT0FTWHh0OGZpbmJXNFZ2Qy9HTU9aMlJUODE2b0UKSjc0S0tQZXlmemtmdkw3c0dsVzVmemRYRGFESFZVL1Fsbk1VZXFUaTZyYVBwWU1qOXRxcFRmNElVNS9UMGlzeApTUWpVcjlPTlY2TGhDODJibFFvTUtYY1lxMitBYkdLVjJxWE44OHJSaHQ4eE5lRU1KWTdmWjg5b0FKMFoxRVdDCnFRTmxxbUF5Mmh1d0QxSnlTdVI1NjhNUm03bkJHNm9oZGtRb25QU2VSbS9oTkJrMzg4WUNXeGFWSzBuWVZRclUKYlhBQkFvSUJBUUN5WVhFdURRU3REcUQxQkQrOEpnaWlpSlVpWUFKM0RLRjJ4N291Q1kzdHRsZUZZUlk4dUczVQpEY005S3c2cFRaMTJrcUJjSTl6V05WWnpUVC9rN2JlcW4wWnVjUTNYWGJpYU0yalRDSDQybWp1dVlHZFRLQU9FCmJSOEZ4SzUzUlpsNmsrVno4akgvelYva09mQkFXNjRzQ2JlNlNzaXpiT0VLdGlUQU5teHZrYUw2TlEzNEluY0sKQnRBOFVReWJWeVVZT1VsUHVNYmxBTnNra1RkT3h1ZmpwYXdCMFZ0WTVLRXAxRGpHSG0yeC9RUmxGRFJXUTRhRQpocUhNa2FsWG44bWVKdnM4aVZzM0x1bFB5VENBK1dHeXYxRFMyc2k0d2NXSVhzK0F6eXJROFZxUVBPU1JrQlAwCmEzUzhBWmNYUG9VeEo4UUVhaGZaSmNGaGgvenZaSU83QW9JQkFRRFlZa29KZnlHL294OGxoWFZoQ1FudGtTSGwKSlgxOFRXRGtrODFwRWhaekdEWDkweFNxL01wSVpYUk9LNlFFbUl2c2cvQkxXODlqaFQ0QzBnSUI3bEZ4L0x6MgpoSmt0QVZiNG1Ud3ZZQ1lscjNOampsd3VxNDNNWXVRalpIeW5LOG5JSVpZZ0JGemNnQUo3S3hVYk5PTDRPVlA0Clg0THZlZ2U3QSs1eU0xT1N6b29CSFJCaXBtS1UwbnhJVFNaejMxMjg4ZTJOdDNrWjNSTTRmcjUxeUxrTnpWdHYKM1VpcTFPVTVyT2ZOYUxnWFZaSC9IZXFadGkwNE04Zmg1Y0c5YzNLTXBVbmo3aXRvbkg1NmR6MXd4UVVuVnB4bgpGYUpISFpFY0dIMVkrbjFZaDcreENQQlNQc3pMcFJHK05ESWNPV2ZKQU9rNUVJOEFBN2xTWHFHVkwwdHgKLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0=",  # noqa
        ).encode()
    ),
    "VERIFYING_KEY": base64.b64decode(
        os.environ.get(
            "JWT_VERIFYING_KEY_B64",
            "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFyN2pNcE5yQlNBT0ZiN1kvRVEwZQoyalRYMjMxeDMzRVJZVGZ0aWZnRDNtVExwcVpzV3VGTVNBSlI2VEJ6MkhvR3h5UGh5M2JtN25GeElvZnhTTnE4CnhZVFg2dUtMWDJodW1TcTYvSnRibldnRDBST0xxczdqUXowWDBaTFpQUVRrdi9sQmN3M2JKbDY1UnJuRHZYYVoKNWVHelJDbFd1L1lBaHhOZzhwYVRCVmk5ZmROT1lIVDBQeU1OQzlKaThXc2ltUC9yTFZyOGo4VTJQK0xnSG5ONQpXMmhKMytHT24vQUFlTHJtYjdzT0t4SU9YdmZMWjVRKzU2WTQxYXlUZHpVbEVJUTkyZS9oQWs4Q0hCWU9YL3JjCmtvejBXSUtYRmNSZys3T1VweUExeEhSdmVtOGlORTA3S2M1WXozLzNubnkzdkhnbWREMGhxU0xTWlZLZnk1MG4KN1JTdmZTU3RWK3VlbVJKQnRWNFprUXpLdDgxQzJibFNCaWNUdFdlWERRbDlTam91c3hTdTVkaU9ndUpscUZiMQptTkpsMktZRDM1QVYrK1BMMzJtRlZ2VlZGTVB1d2JPcFFMN21zSzFiMTlZbk52OVpYK0VrNDI3a0NPaTY0Z3pmCmdOZzZXNit1NllDUnJaOGFSMGc2ZGdCcHZMWjliejRjeG00Q2lMNzI4MW10SjFONkMxTGNUY3lpWWllRzBjSnYKakdpbVgxNCtDZHgzemdYQVJGMVNVZE94NTZzRCt2emd3UEllOFZhRmxhTFRrbTFPSnRUUit3alFXM0J4RVZmYgp1RFJvd1JRMy9aclpXYXR2eFFYTmFHZEJRVGhSeWxMd3lGVk15QmZ2b0hNYVNDQkhZeVJ1ZnhSNjUxaEFkV1ltCnFRMFNOYjYzUTk0cVIrSGh1L010dE5jQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ==",  # noqa
        )
    ),
}

if "test" in sys.argv:
    from .testing import *  # noqa

# Allow cascading configuration and
# DO NOT PUT ANYTHING BELOW
