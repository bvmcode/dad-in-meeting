# Dad in meeting

Super simple dumb app I run this on my raspberry pi so that my family will know if I am in a meeting or not.

No migrations needed.

Just create a superuser
```
python manage.py superuser
```

Then run the server (since this is just a home project i just use nohup)
```
nohup python manage.py runserver 0.0.0.0:8000 > & app.log
```

Then keep the page up while working and update the current instance of Meeting on the admin page.
A check means you are in a meeting. <br>
![](https://github.com/bvmcode/dad-in-meeting/blob/master/meeting.png?raw=true)

The user will go to `http://<ip_address>:8000` and be greeted with your work status as long as they are on the same WiFi.
