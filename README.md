#Alessiobot
Alessiobot is the best possible emulator of Alessio. It sends out emails in the morning for organizing for lunch and provides a web interface to set up holidays and the daily RSVP.

The assumption is that the basedir is /data/alessiobot

Most of the files are automatically created. What really matter is
webalessio/views.py             #Index (the root page displayed), index\_json (the same info in json format), set\_presence (sets info for a particular user)
webalessio/models.py            #The database model
webalessio/urls.py              #Mapping for the urls.
webalessio/templates/webalessio/daylist.html    #The template for the main form

You might want to google "django tutorial"

Fortunes in italian courtesy of http://www.fortune-it.net/main.html

#Crontab to run the sendmail script
`37 6 * * 1-5 sh -ex /data/alessiobot/mailsender.sh > /data/out 2> /data/err`

#Some commands for updating the db and running the server:
```python
python manage.py runserver 0.0.0.0:8000
python manage.py makemigrations webalessio
python manage.py sqlmigrate webalessio 0001
python manage.py migrate webalessio
```

#How to populate the db:
```python
from webalessio.models import User
users = ['user1@gmail.com', 'user2@gmail.com']
for user_email in users:
    u = User(email=user_email)
    u.save()
#and this is to clean it:
map(User.delete, User.objects.all())
```

N.B.: The above instructions only work if you export the `DJANGO_SETTINGS_MODULE=alessiobot.settings` environment variable.
