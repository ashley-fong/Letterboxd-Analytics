import requests #
import pandas as pd
import json

def get_movie_details(movie_title, api_key):
    # Base URL for the OMDb API
    base_url = "https://www.omdbapi.com/"
    
    # Constructing query parameters
    params = {
        'apikey': api_key,
        't': movie_title
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

    film_names = diary['Name'].unique()
    # print(type(film_names))

    movie_csv = []
    # df = pd.DataFrame()
    count=0

    # loop though list and pass as movie title
    for title in film_names:
        movie_data = get_movie_details(title, MY_KEY)
        # print(movie_data)

        # printing specific details
        # print(json.dumps(movie_data, indent=4))

        # print(f"Title: {movie_data['Title']}")
        # print(f"Year: {movie_data['Year']}")
        # print(f"Genre: {movie_data['Genre']}")
        # print(f"Director: {movie_data['Director']}")
        # print(f"Actors: {movie_data['Actors']}")
        # print(f"IMDb Rating: {movie_data['imdbRating']}")

        movie_csv.append(movie_data)
        count+=1
        if count == 10:
            break

    # print(movie_csv)

    df = pd.DataFrame(movie_csv)
    print(df.to_string())


    df.to_csv('test.csv', index=False)





main()