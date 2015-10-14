from webalessio.models import User

for u in User.objects.all():
    u.present = False
    u.save()
