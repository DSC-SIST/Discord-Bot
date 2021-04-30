from urllib.request import urlopen

# Credit goes to prakhar1965
# https://github.com/prakhar1965/lyric-scraper/blob/master/lyric_scraper/main.py

def find_lyrics(song_query):
    search_query = song_query.lower()
    # String for performing search query
    search_query = "-".join(search_query.split(' '))
    url = Settings().SECRETS['LYRICS_API'] + search_query

    # To perform search query on AZlyrics.com
    content = urlopen(url)
    html_text = content.read()
    soup = BeautifulSoup(html_text, 'html.parser')
    lyric_found = False

    # To find all the tags which contain lyric link
    for tag in soup.find_all('td', {'class': 'text-left visitedlyr'}):
        if tag.a:
            lyric_found = True
            lyric_url = tag.a['href']
            break

    if not lyric_found:
        # print("lyric couldn't be found for given title")
        return

    lyric_content = urlopen(lyric_url)
    lyric_html = lyric_content.read()
    lyric_soup = BeautifulSoup(lyric_html, 'html.parser')

    for div in lyric_soup.find_all('div', {'class': 'col-xs-12 col-lg-8 text-center'}):
        inner_div = div
        for div in inner_div.find_all('div'):
            if not div.has_attr('class'):
                return div.text
    return
