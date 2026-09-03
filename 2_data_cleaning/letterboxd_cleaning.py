import pandas as pd 

# reading all needed datasets 
diary = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/1_raw_data/letterboxd/diary.csv')
watched = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/1_raw_data/letterboxd/watched.csv')
likes_films = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/1_raw_data/letterboxd/likes/films.csv')

# right merging for all movies watched 
# watched csv has all movies 'watched' (user has clicked watched on letterboxd)
# diary csv only has movies that are logged (user has rated, reviewed, or both)
# watched should have more unique movies 
diary_watched = pd.merge(diary, watched[['Date', 'Name', 'Year','Letterboxd URI']], on=['Date', 'Name', 'Year'], how="right")
diary_watched = diary_watched.drop(columns='Letterboxd URI_x')

# outer join to get all records from diary and watched 
# diary has rewatches, important to retain 
full_d_w = pd.merge(diary[['Date','Name','Year','Rating','Rewatch','Tags','Watched Date']], diary_watched[['Date', 'Name', 'Year','Letterboxd URI_y']], on=['Date', 'Name', 'Year'], how="outer")
# full_d_w = pd.merge(diary[['Date','Name','Year','Rating','Rewatch','Tags','Watched Date']], diary_watched[['Date', 'Name', 'Year','Letterboxd URI_y']], left_on=['Name', 'Year', 'Watched Date'], right_on=['Name','Year','Date'], how="inner")
# full_d_w_2 = pd.merge(full_d_w, diary_watched[['Date', 'Name', 'Year','Letterboxd URI_y']], left_on=['Name', 'Year', 'Watched Date'], right_on=['Name','Year','Date'], how="inner")

# right join to keep Letterboxd URI - like an id
full_d_w_uri = pd.merge(full_d_w[['Date','Name','Year','Rating','Rewatch','Tags','Watched Date']], watched[['Name', 'Letterboxd URI']], on=['Name'], how="right")

# inserting conditional column for Like
# if Letterboxd URI is in likes_films, value = Yes, else = no 
with_likes = full_d_w_uri.copy()
with_likes['Like'] = with_likes['Letterboxd URI'].isin(likes_films['Letterboxd URI'])
with_likes.sort_values(by='Date', ascending=True, inplace=True)

# fill rewatch column with 'No' to have no blanks/NaNs
with_likes.fillna({'Rewatch':'No'}, inplace=True)

# print(with_likes.to_string())

# exporting excel to be used in Power BI
with_likes.to_excel("/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary.xlsx", sheet_name="diary", index=False)
# with_likes.to_csv("/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary.csv", index=False)