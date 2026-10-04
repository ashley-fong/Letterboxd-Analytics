import pandas as pd 

# reading all needed datasets 
diary = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/1_raw_data/letterboxd/diary.csv')
watched = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/1_raw_data/letterboxd/watched.csv')
likes_films = pd.read_csv('/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/1_raw_data/letterboxd/likes/films.csv')

# right merging for all movies watched 
# watched csv has all movies 'watched' (user has clicked watched on letterboxd)
# diary csv only has movies that are logged (user has rated, reviewed, or both)
# watched should have more unique movies 

# merging on Date
diary_watched = pd.merge(diary, watched[['Date', 'Name', 'Year','Letterboxd URI']], on=['Date', 'Name', 'Year'], how="right")
diary_watched = diary_watched.drop(columns='Letterboxd URI_x')

# merging on Watched Date
diary_watched_wd = pd.merge(diary, watched[['Date', 'Name', 'Year','Letterboxd URI']], right_on=['Name', 'Year', 'Date'],
    left_on=['Name', 'Year', 'Watched Date'], how="right")
diary_watched_wd = diary_watched_wd.drop(columns='Letterboxd URI_x')

# merging both dfs for all matches
final_diary_watched = pd.merge(diary_watched[['Date', 'Name', 'Year','Rating','Rewatch','Tags','Watched Date','Letterboxd URI_y']], diary_watched_wd[['Name', 'Year', 'Date_y','Letterboxd URI_y']],
    left_on=['Letterboxd URI_y', 'Name', 'Year', 'Date'], right_on=['Letterboxd URI_y','Name', 'Year','Date_y'], how="inner")

# outer join to get all records from diary and watched 
# diary has rewatches, important to retain 
full_d_w = pd.merge(diary, final_diary_watched[['Date','Name','Year','Rating','Rewatch','Tags','Watched Date','Letterboxd URI_y']], 
                    left_on=['Name', 'Year', 'Watched Date'], right_on=['Name', 'Year', 'Watched Date'], how="outer")

# print(full_d_w.to_string())

# filling NAs in Date_y with Watched Date
# some records have (log) Date different than Watched Date 
# merge cannot match if this happens 
# this fixes that problem
full_d_w['Date_y'] = full_d_w['Date_y'].fillna(full_d_w['Watched Date'])

# when dates were not matching, it creates duplicate records 
# need to drop these duplicates based on Date_y (what was just filled)
full_d_w.drop_duplicates(
    subset=['Name', 'Year','Date_y'], 
    keep='first', inplace=True
)
# sort to keep in watched date order 
full_d_w.sort_values(by='Date_y', ascending=True, inplace=True)

# print(full_d_w.to_string())
full_d_w.to_csv("/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary_copy.csv", index=False)

# right join to keep Letterboxd URI - like an id
full_d_w_uri = pd.merge(full_d_w[['Date_x','Name','Year','Rating_x','Rewatch_x','Tags_x','Watched Date','Date_y']], watched[['Name', 'Letterboxd URI']], on=['Name'], how="right")

# when dates were not matching, it creates duplicate records 
# need to drop these duplicates based on Date_y (what was just filled)
full_d_w_uri.drop_duplicates(
    subset=['Name', 'Year','Date_y'], 
    keep='first', inplace=True
)

# full_d_w_uri.to_csv("/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary_copy.csv", index=False)

# print(full_d_w_uri.to_string())

# inserting conditional column for Like
# if Letterboxd URI is in likes_films, value = Yes, else = no 
with_likes = full_d_w_uri.copy()

# when dates were not matching, it creates duplicate records 
# need to drop these duplicates based on Date_y (what was just filled)
# full_d_w.drop_duplicates(
#     subset=['Name', 'Year','Date_y'], 
#     keep='first', inplace=True
# )
with_likes['Like'] = with_likes['Letterboxd URI'].isin(likes_films['Letterboxd URI'])
with_likes.sort_values(by='Date_y', ascending=True, inplace=True)

# fill rewatch column with 'No' to have no blanks/NaNs
with_likes.fillna({'Rewatch':'No'}, inplace=True)

# Date,Name,Year,Rating,Rewatch,Tags,Watched Date,Letterboxd URI,Like
# Date_x,Name,Year,Letterboxd URI,Rating_x,Rewatch_x,Tags_x,Watched Date,Date_y,Rating_y,Rewatch_y,Tags_y,Letterboxd URI_y,Like

# with_likes.drop(columns={'Letterboxd URI','Rating_y','Rewatch_y','Tags_y'}, inplace=True)

with_likes.rename(columns={'Date_x':'Date', 'Rating_x':'Rating', 'Rewatch_x':'Rewatch', 'Tags_x':'Tags' , 'Date_y':'Log Date'}, inplace=True)

# print(with_likes.to_string())


# exporting excel to be used in Power BI
with_likes.to_excel("/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary.xlsx", sheet_name="diary", index=False)
with_likes.to_csv("/Users/ashleyfong/Documents/Letterboxd/Letterboxd-Analytics/2_data_cleaning/cleaned_diary.csv", index=False)