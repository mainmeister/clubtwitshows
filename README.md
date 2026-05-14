This object will allow you to access you Club Twit videos in you python code. 
>You need to define an environment variable named `"twitcluburl"` that contains your personal Club Twit url.
```
from clubtwit import ClubTwit

    ct = ClubTwit()
    print(f'Using Club Twit URL: {ct.clubtwit_url}')
    for show in ct.shows:
        print(f"Title: {show['Title']}\n
        Description: {show['Description']}\n
        Link: {show['Link']}\n
        PubDate: {show['PubDate']}\n
        Length: {int(show['Length']/(1024*1024)):,} MB\n")
```
#### _Requirments_:
* lxml==5.3.0
* python-dotenv==1.0.1
* requests==2.32.3
