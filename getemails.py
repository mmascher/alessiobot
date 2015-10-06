import sys
import datetime

import django
from webalessio.models import User

##########################################
# Little schema to see when to send emails
# F=from, T=to, TD=today
#
#   ---------------------
#   | F | T |  SEND IF  |
#   |   |   |  always   |
#   | A |   |   TD<A    |
#   |   | A |   TD>A    |
#   | A | B | !A<=TD<=B |
#   ---------------------


if __name__ == '__main__':
    #export DJANGO_SETTINGS_MODULE=alessiobot.settings
    django.setup()
    today = datetime.date.today() #time are UTC !
    users_today = []

    for user in User.objects.all():
        if ((not user.suspend_from and not user.suspend_until) or
           (user.suspend_from and today < user.suspend_from) or
           (user.suspend_until and today > user.suspend_until) or
           (user.suspend_from and user.suspend_until and not
           (user.suspend_from <= today <= user.suspend_until))):
            users_today.append(user)

    if users_today:
        print("To: " + ', '.join([user.email for user in users_today]))
        sys.exit(0)
    else:
        sys.exit(1)
