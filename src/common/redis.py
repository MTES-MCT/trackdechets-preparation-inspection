import redis
from django.conf import settings

redis_client = redis.from_url(settings.REDIS_URL)


def gen_otp_email_key(user):
    return f"otp_email_sent_{user.id}"
