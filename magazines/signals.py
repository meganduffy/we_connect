import arrow
from .models import Purchase
from paypal.standard.models import ST_PP_COMPLETED
from django.contrib import messages


def subscription_created(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status:
        print "payment status is: %s" % ipn_obj.payment_status
        magazine_id = ipn_obj.custom.split('-')[0]
        user_id = ipn_obj.custom.split('-')[1]

        purchase = Purchase.objects.get(user_id=user_id,
                                        magazine_id=magazine_id).first()
        if purchase:
            purchase.subscription_end = arrow.now().replace(weeks=+4).datetime
        else:
            purchase = Purchase.objects.create(magazine_id=magazine_id,
                                               user_id=user_id,
                                               subscription_end=arrow.now().replace(weeks=+4).datetime)
        purchase.save()

    else:  # TODO: what to do if payment status not complete
        assert not ipn_obj.payment_status
        messages.error("Your transaction was not completed")
        print "Payment didn't go through"


def subscription_was_cancelled(sender, **kwargs):
    ipn_obj = sender
    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    purchase = Purchase.objects.get(user_id=user_id, magazine_id=magazine_id)
    purchase.subscription_end = arrow.now().datetime
    purchase.save()
