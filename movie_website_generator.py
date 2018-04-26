import movie
import fresh_tomatoes

capitain_fantastic = movie.Movie(
  'Captain Fantastic',
  2016,
  'https://upload.wikimedia.org/wikipedia/en/c/c2/Captain_Fantastic_poster.jpg',
  'https://www.youtube.com/watch?v=D1kH4OMIOMc')

gone_girl = movie.Movie(
  'Gone Girl',
  2014,
  'https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg',
  'https://www.youtube.com/watch?v=2-_-1nJf8Vg')

prisoners = movie.Movie(
  'Prisoners',
  2013,
  'https://upload.wikimedia.org/wikipedia/en/6/63/Prisoners2013Poster.jpg',
  'https://www.youtube.com/watch?v=bpXfcTF6iVk')

lotr_fellowship = movie.Movie(
  'The Lord of the Rings: The Fellowship of the Ring',
  2001,
  'https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg',
  'https://www.youtube.com/watch?v=Pki6jbSbXIY')

lotr_two_towers = movie.Movie(
  'The Lord of the Rings: The Two Towers',
  2002,
  'https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg',
  'https://www.youtube.com/watch?v=2dlRvAjU_RI')

lotr_return_king = movie.Movie(
  'The Lord of the Rings: The Return of the King',
  2003,
  'https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg',
  'https://www.youtube.com/watch?v=r5X-hFf6Bwo')

movies = [capitain_fantastic, gone_girl, prisoners, lotr_fellowship, lotr_two_towers, lotr_return_king]

fresh_tomatoes.open_movies_page(movies)