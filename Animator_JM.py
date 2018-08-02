import fresh_tomatoes
import Movie_JM

toy_story = Movie_JM.Movie("Toy Story", "A story of a boy and his toys that come to life","https://vignette.wikia.nocookie.net/random-ness/images/d/df/Toy-Story-2-image-toy-story-2-36440635-1024-768.jpg/revision/latest?cb=20150722205605", "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
herbie = Movie_JM.Movie("Herbie",
                     "An old volkswagen that can really go fast.",
                     "https://www.google.fr/url?sa=i&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwjH1KLMq8_cAhUFx4UKHY97BPUQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHerbie&psig=AOvVaw2OcWnHBZ0w1kEkXw1nxUzW&ust=1533332707205596",
                     "https://www.youtube.com/watch?v=jhiB_cECkUM")
print(herbie.storyline)
#herbie.show_trailer()

slumdog = Movie_JM.Movie("Slumdog Millionare",
                     "Contestant in Who wants to be a Millionare answers every question correctly, but is accused a cheating",
                     "https://en.wikipedia.org/wiki/File:Slumdog_Millionaire_poster.png", "https://www.youtube.com/watch?v=AIzbwV7on6Q")

#print(slumdog.storyline)
#slumdog.show_trailer()

movies = [toy_story, herbie, slumdog]
fresh_tomatoes.open_movies_page(movies)

