import requests #
import pandas as pd
import json

def get_movie_details(movie_title, movie_year, api_key):
    # Base URL for the OMDb API
    base_url = "https://www.omdbapi.com/"
    
    # Constructing query parameters
    params = {
        'apikey': api_key,
        't': movie_title, 
        'y': movie_year
    }
    
    # Send GET request
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json() #
        if data.get("Response") == "True":
            return data
        else:
            return f"Error: {data.get('Error')}"
    else:
        return response.status_code

def main():
    # Usage (Replace 'YOUR_API_KEY' with your actual key)
    MY_KEY = "5d2c498"

    # get excel names as list 
    diary = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary.csv')

    film_names = diary.drop_duplicates(subset=['Name'])
    film_names = film_names.drop(columns=['Date','Rating','Rewatch','Tags','Watched Date','Letterboxd URI','Like'])
    # film_names = film_names['Name'].unique()
    # print((film_names))

    movie_csv = []

    count=0

    # loop though list and pass as movie title
    for title, year in zip(film_names['Name'], film_names['Year']): 
    # for title in film_names:

        # 
        if title == "Spider-Man: Homecoming" or title =="Hannah Montana: The Movie" or title =="Wizards of Waverly Place: The Movie" or title =="Bring It On: All or Nothing":
            movie_data = get_movie_details(title, year, MY_KEY)

        elif title == "Glee: The Concert Movie":
            result = title.split(": ")
            print(result)
            movie_data = get_movie_details(result[0], year, MY_KEY)

        elif title == "Z-O-M-B-I-E-S":
            movie_data = get_movie_details("Zombies", year, MY_KEY)

        elif title == "Twelve Monkeys":
            movie_data = get_movie_details("12 Monkeys", year, MY_KEY)

        elif title == "The 5 Seconds of Summer Show (Live & Backstage In Amsterdam)":
            result = title.split(" (")
            print(result)
            movie_data = get_movie_details(result[0], year, MY_KEY)

        elif title == "A Nice Indian Boy":
            movie_data = get_movie_details(title, "2025", MY_KEY)
                    
        elif ": " in title:
            result = title.split(": ")
            print(result)
            movie_data = get_movie_details(result[1], year, MY_KEY)

        else:
            movie_data = get_movie_details(title, year, MY_KEY)
            # continue
        # print(movie_data)

        # printing specific details
        # print(f"Title: {movie_data['Title']}")
        # print(f"Year: {movie_data['Year']}")
        # print(f"Genre: {movie_data['Genre']}")
        # print(f"Director: {movie_data['Director']}")
        # print(f"Actors: {movie_data['Actors']}")
        # print(f"IMDb Rating: {movie_data['imdbRating']}")

        if isinstance(movie_data, dict):
            movie_csv.append(movie_data)
        else:
            print(f"Skipping '{title}' — returned {type(movie_data).__name__}: {movie_data}")

        # count+=1
        # if count == 5:
        #     break

    # print(movie_csv)
    # Title,Year,Rated,Released,Runtime,Genre,Director,Writer,Actors,Plot,Language,Country,Awards,Poster,Ratings,Metascore,imdbRating,imdbVotes,imdbID,Type,DVD,BoxOffice,Production,Website,Response
    df = pd.DataFrame(movie_csv)
    # print(df.columns.to_list())

    # , columns=['Title', 'Year', 'Runtime', 'Genre','Director','Actors','imdbRating'])
    df2 = df[['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'imdbRating']]


    df2.to_csv("test.csv", index=False)

main()