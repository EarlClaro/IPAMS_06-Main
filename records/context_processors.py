from datetime import datetime, timedelta
from .models import Subscription

def subscription_status(request):
    if request.user.is_authenticated:
        subscription = request.user.get_subscription()
        show_modal = subscription.is_near_end() if subscription else False
        return {'show_modal': show_modal}
    return {}
