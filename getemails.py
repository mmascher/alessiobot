import sys
import datetime

import django
from webalessio.models import User

if __name__ == '__main__':
    #export DJANGO_SETTINGS_MODULE=alessiobot.settings
    django.setup()
    today = datetime.date.today()
    users_today = []

    for user in User.objects.all():
        if (not user.suspend_from or not user.suspend_until or
            today < user.suspend_from and today > user.suspend_until):
            users_today.append(user)

    if users_today:
        print("To: " + ', '.join([user.email for user in users_today]))
        sys.exit(0)
    else:
        sys.exit(1)
