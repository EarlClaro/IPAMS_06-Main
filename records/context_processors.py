from datetime import datetime, timedelta
from .models import Subscription

def subscription_status(request):
    if request.user.is_authenticated:
        subscription = request.user.get_subscription()
        show_modal = subscription.is_near_end() if subscription else False
        if subscription:
            plan_name = subscription.plan_id.plan_name if subscription.plan_id else 'Free'
        else:
            plan_name = 'Free'
        return {'show_modal': show_modal, 'subscription_plan_name': plan_name}
    return {'show_modal': False, 'subscription_plan_name': 'Free'}

