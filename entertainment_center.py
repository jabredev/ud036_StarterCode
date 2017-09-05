from imdbpie import Imdb
import fresh_tomatoes
import media

# Creating an instance of Imdb to be used to collect data via API
imdb = Imdb()
imdb = Imdb(anonymize=True)

# IMDB Id's to be used to receive info from IMDB using API's
interstellar_id = "tt0816692"
gravity_id = "tt1454468"
passengers_id = "tt1355644"
arrival_id = "tt2543164"
pulpfiction_id = "tt0110912"
contact_id = "tt0118884"

# Creation of movie objects to include required information
interstellar = media.Movie(imdb.get_title_by_id(interstellar_id).title,
                           imdb.get_title_by_id(interstellar_id).plot_outline,
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ",
                           imdb.get_title_by_id(interstellar_id).certification,
                           imdb.get_title_by_id(interstellar_id).rating)

gravity = media.Movie(imdb.get_title_by_id(gravity_id).title,
                           imdb.get_title_by_id(gravity_id).plot_outline,
                           "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                           "https://www.youtube.com/watch?v=OiTiKOy59o4",
                           imdb.get_title_by_id(gravity_id).certification,
                           imdb.get_title_by_id(gravity_id).rating)

passengers = media.Movie(imdb.get_title_by_id(passengers_id).title,
                           imdb.get_title_by_id(passengers_id).plot_outline,
                           "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
                           "https://www.youtube.com/watch?v=7BWWWQzTpNU",
                           imdb.get_title_by_id(passengers_id).certification,
                           imdb.get_title_by_id(passengers_id).rating)

arrival = media.Movie(imdb.get_title_by_id(arrival_id).title,
                           imdb.get_title_by_id(arrival_id).plot_outline,
                           "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                           "https://www.youtube.com/watch?v=tFMo3UJ4B4g",
                           imdb.get_title_by_id(arrival_id).certification,
                           imdb.get_title_by_id(arrival_id).rating)

pulpfiction = media.Movie(imdb.get_title_by_id(pulpfiction_id).title,
                           imdb.get_title_by_id(pulpfiction_id).plot_outline,
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           imdb.get_title_by_id(pulpfiction_id).certification,
                           imdb.get_title_by_id(pulpfiction_id).rating)

contact = media.Movie(imdb.get_title_by_id(contact_id).title,
                           imdb.get_title_by_id(contact_id).plot_outline,
                           "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
                           "https://www.youtube.com/watch?v=SRoj3jK37Vc",
                           imdb.get_title_by_id(contact_id).certification,
                           imdb.get_title_by_id(contact_id).rating)

# Creating a list of movies to pass to the open_movies_page function
movies = [interstellar,gravity,passengers,arrival,pulpfiction,contact]

# Calling open_movies_page function to create the webpage
fresh_tomatoes.open_movies_page(movies)
