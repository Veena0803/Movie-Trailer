import media
import tv_shows
import json
import fresh_tomatoes
from urllib2 import Request, urlopen, URLError
from itertools import islice

# API request to access movies from the Movies DB API

movies = []
request = Request(
    'https://api.themoviedb.org/3/discover/movie'
    '?api_key=b9c30174215534f1820b08ea1cc7bce5&language=en-US'
    '&sort_by=popularity.desc&include_adult=false&page=1'
    '&append_to_response=videos'
    )

# Request to play youtube videos for the movies

trailer_request = Request(
    'https://api.themoviedb.org/3/movie/263115'
    '?api_key=b9c30174215534f1820b08ea1cc7bce5'
    '&apprend_to_response=videos'
    )
try:
    response = urlopen(request)

    # Convert the response into a JSON object

    json_object = json.load(response)

    # Iterate through the movie results fetched from the API and selecting \
    #  only the first 6 movies from the response fetched

    for movie in islice(json_object['results'], 12):
        trailer_response = urlopen(
            'https://api.themoviedb.org/3/movie/' + str(movie['id']) +
            '/videos?api_key=b9c30174215534f1820b08ea1cc7bce5')
        trailer_object = json.load(trailer_response)
        movies.append(
          media.Movie(
              movie['title'], movie['overview'],
              'http://image.tmdb.org/t/p/w185' + movie['poster_path'],
              'https://www.youtube.com/watch?v=' +
              trailer_object['results'][0]['key'])
             )
except URLError, e:
    print 'No movies. Got an error code:', e

# Creating objects for each TV show

friends = tv_shows.TV(
  'Friends',
  'Sitcom about 6 friends and their life in New York',
  'http://www.gstatic.com/tv/thumb/tvbanners/183931/p183931_b_v8_ac.jpg',
  'https://www.youtube.com/watch?v=bvEnlf9g4co')

stranger_things = tv_shows.TV(
  'Stranger Things',
  'American science horror-fiction television series',
  'https://upload.wikimedia.org/wikipedia/commons/3/38/'
  'Stranger_Things_logo.png',
  'https://www.youtube.com/watch?v=XWxyRG_tckY'
)

got = tv_shows.TV(
  'Game of Thrones',
  'Series anout a deadly game for control of the Seven Kingdoms and sit atop'
  'the Iron Throne',
  'https://upload.wikimedia.org/wikipedia/en/9/92/'
  'Game_of_Thrones_Season_7.png',
  'https://www.youtube.com/watch?v=giYeaKsXnsI')

office = tv_shows.TV(
 'The Office',
 'Mockumentary on a group of office workers and their daily life',
 'https://upload.wikimedia.org/wikipedia/en/b/b6/TheOfficeUSSeason1Cover.jpg',
 'https://www.youtube.com/watch?v=sMXpGBiC6xo'
)

breaking_bad = tv_shows.TV(
    'Breaking Bad',
    'A chemistry teacher and his desperation to earn money because of'
    ' his illness',
    'https://upload.wikimedia.org/wikipedia/en/6/61/'
    'Breaking_Bad_title_card.png',
    'https://www.youtube.com/watch?v=HhesaQXLuRY'
   )

seinfeld = tv_shows.TV(
    'Seinfeld',
    'Show about 4 friends and their life in New York city',
    'https://upload.wikimedia.org/wikipedia/en/c/ce/Seinfeld1%262.jpg',
    'https://www.youtube.com/watch?v=SOsbYJ4CfTA'
    )

# List/Array that stores all the TVshows in a variable named "TVshows"

TVshows = [
    friends,
    stranger_things,
    got,
    office,
    breaking_bad,
    seinfeld,
    ]

# Invokes the function "open_movies_page" from the file "fresh_tomatoes"

fresh_tomatoes.open_movies_page(TVshows, 'TV_shows.html', False)
fresh_tomatoes.open_movies_page(movies, 'index.html', True)
