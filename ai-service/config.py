from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Rate limiting configuration
limiter = Limiter(
    key_func=get_remote_address,   # identify users by IP
    default_limits=["30 per minute"]  # global limit
)
