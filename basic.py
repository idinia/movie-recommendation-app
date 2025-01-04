print(" Welcome to this kickass movie recommendation app")

favorite_movie = "The Shawshank Redemption"
genre = "drama"
release_year = 1994
duration_in_minutes = 142
imdb_rating = 9.3
lead_actor = "Morgan Freeman"

print(f"My favorite movie is {favorite_movie}, it's a {genre} movie released in {release_year} , with a total duration of {duration_in_minutes} minutes, and a rating of {imdb_rating}" )

user_favorite_movie = input("What is your favorite movie? ")
user_genre = input("What genre is it? ")
user_release_date = int(input("When was is it released? "))
user_duration_in_minutes = input("How long is it? ")
user_imdb_rating = float(input("What is its IMDB rating? "))
user_lead_actor = input("Who is the lead actor or actress? ")

print(f"Your favorite movie is {user_favorite_movie}, it was released in {user_release_date}, and the lead actor, is {user_lead_actor}. What a great movie!")

print(" Now let' try to find you a good movie to watch: ")

age = int(input("How old are you? "))

if age <= 13:
    print(" We recommend an animated movie");
elif age <= 17:
    print(" We recommend a superhero movie");
elif age >= 18:
    print(" We recommend a thriller");
else: 
    print(" We need your age to recommend a valid movie")

