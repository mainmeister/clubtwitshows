This object will allow you to access you Club Twit videos in you python code. 
>You need to define an environment variable named `"twitcluburl"` that contains your personal Club Twit url.
```
from clubtwit import ClubTwit

ct = ClubTwit()
# get a list of all the shows
shows = ct.shows
print(f'Using Club Twit URL: {ct.clubtwit}')
for show in shows:
  print(f'{show["Title"]}: {show["Link"]}')
```
#### _Requirments_:
* lxml==5.3.0
* python-dotenv==1.0.1
* requests==2.32.3
