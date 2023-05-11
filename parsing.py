import requests
from bs4  import BeautifulSoup
YOUTUBE = "https://www.youtube.com/channel/UCLR-0MU-uinEP-ui8FuXEJg"
WEATHER = "https://www.google.com/search?q=weather&oq=wea&aqs=chrome.1.69i57j0i433i512j0i131i433i512j0i512j0i131i433i512j0i512j0i433i512j0i131i433i650j0i512l2.7074j0j15&sourceid=chrome&ie=UTF-8"
EURO_TENGE = "https://www.google.com/search?q=tdhj+d+ntyut&bih=714&biw=1536&hl=ru&ei=2FVBZNOFFZ2D9u8Pjve-kAw&ved=0ahUKEwjT0ZGB37j-AhWdgf0HHY67D8IQ4dUDCA8&uact=5&oq=tdhj+d+ntyut&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIRCAAQgAQQsQMQChAqEEYQggIyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6CggAEEcQ1gQQsAM6DQgAEEcQ1gQQyQMQsAM6CwgAEIoFEJIDELADOg0IABANEIAEELEDEIMBOgcIABANEIAEOgoIABAHEB4QChAqOggIABAHEB4QCjoMCAAQCBAHEB4QChAqOg0IABAIEAcQHhDxBBAKOggIABAFEB4QDToKCAAQBRAeEA0QCjoNCAAQBRAeEA0Q8QQQCjoLCAAQBxAeEPEEEAo6CggAEAUQBxAeEAo6CggAEA0QgAQQsQNKBAhBGABQnwVY1Ddg8jloAnABeACAAZ0BiAGZC5IBBDAuMTCYAQCgAQHIAQnAAQE&sclient=gws-wiz-serp"
DOLLAR_TENGE = "https://www.google.com/search?q=lfkkfh+d+ntyut&bih=714&biw=1536&hl=ru&ei=2FVBZNOFFZ2D9u8Pjve-kAw&ved=0ahUKEwjT0ZGB37j-AhWdgf0HHY67D8IQ4dUDCA8&uact=5&oq=lfkkfh+d+ntyut&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQRxDWBBCwAzINCAAQRxDWBBDJAxCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzILCAAQigUQkgMQsANKBAhBGABQAFgAYNMMaAFwAXgAgAEAiAEAkgEAmAEAyAEJwAEB&sclient=gws-wiz-serp"
RUBL_TENGE = "https://www.google.com/search?q=he%2Ckm+d+ntyut&ei=NlZBZM6YKtnY7_UP8KqloAo&ved=0ahUKEwjOi5Cu37j-AhVZ7LsIHXBVCaQQ4dUDCA8&uact=5&oq=he%2Ckm+d+ntyut&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIRCAAQgAQQsQMQChAqEEYQggIyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6CggAEEcQ1gQQsAM6CQgAEIAEEAoQKjoICAAQFhAeEAo6DQgAEI8BEOoCELQCGAE6DQguEI8BEOoCELQCGAE6CwgAEIoFEAoQARBDOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6BQgAEIAEOhEILhCDARDHARCxAxDRAxCABDoICAAQgAQQsQM6DQgAEIoFEAoQARBDECo6BwguEIoFEEM6CwgAEIoFELEDEIMBOgUILhCABDoJCAAQgAQQChABOgwIABCABBCxAxAKECo6CggAEIoFELEDEEM6DQgAEIoFELEDEIMBEEM6CggAEIAEELEDEAo6DQgAEIAEELEDEIMBEAo6DAgAEIAEEAEQRhCCAjoHCAAQgAQQAUoECEEYAFD1BVjYW2DNXWgMcAF4BIABtgGIAegVkgEEMC4xOJgBAKABAbABCsgBCMABAdoBBAgBGAo&sclient=gws-wiz-serp"                                                                                 
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
def get_currency(url):
    full_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('no data')
    return result
def get_subskr(url):
    full_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("yt-formatted-string", {"id": "subskribe_count"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('no data')
    return result
def get_weather(url):
    full_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "wob_t"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('no data')
    return result
print(get_currency(EURO_TENGE))
print(get_currency(DOLLAR_TENGE))
print(get_currency(RUBL_TENGE))
print(get_subskr(YOUTUBE))
print(get_weather(WEATHER))




