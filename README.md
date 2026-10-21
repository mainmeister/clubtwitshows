This object will allow you to access your Club Twit videos in your python code. 

## Installation

You can install the package directly from PyPI:

```bash
pip install clubtwitshows
```

Or using `uv`:

```bash
uv add clubtwitshows
```

## Usage

>You need to define an environment variable named `"twitcluburl"` that contains your personal Club Twit url.

```python
from clubtwitshows import ClubTwit

ct = ClubTwit()
print(f'Using Club Twit URL: {ct.clubtwit_url}')
for show in ct.shows:
    print(f"Title: {show['Title']}\n"
          f"Description: {show['Description']}\n"
          f"Link: {show['Link']}\n"
          f"PubDate: {show['PubDate']}\n"
          f"Length: {int(show['Length']/(1024*1024)):,} MB\n")
```

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
