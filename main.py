"""
Data cleaning:
First step: Make sure all 2017 data is from 2017
To do this: Use imdbpy to search for movies based on imdb_id from dataset
Once the id has been retrieved from the api add new column called 'release_date_clean' with the
release date from imdb
"""


# all the packages I'm using
# the as pd just makes it so I can references pandas by only typing out pd to save a couple keystrokes.
import pandas as pd
from imdb import IMDb

# allows head function on dataframe to show more information, can be commented out
pd.set_option('display.max_columns', None)

# loads the csv into a pandas dataframe, while there is a header option it is not required to be used
movie_data = pd.read_csv("test_clean_maybe.csv")

# Starts the connection to imdb
im = IMDb()
# Creating a dictionary (unique key : value pair) to associate a movie id with its release date to make sure there is no
# data mis-match
# imdb_date = []
#
#
# # Uses list comprehension to extract the imdb_id from the dataframe into a stand-alone list
# imdb_list = [imdb_id for imdb_id in movie_data['imdb_id']]
# #
# #
# # This loop will grab the imdb_id from our list called `imdb_list` after getting the idea it'll strip out the beginning
# # 2 characters leaving only the number part
# for movie_id in imdb_list:
#     # this will query the imdb website to get all the information based on that movie id
#     # such as cast, genres, runtimes, year it was released among others
#     # does not include budget
#     imdb_information = (im.get_movie(movie_id[2:]))
#     print(str(movie_id) + " " + str(imdb_information.data['year']) +  " " + imdb_information.data['title'])
#     # in this for loop you can get different information from what the api is returning.
#     # should be able to access any column by doing imdb_information.data['name of column here']
#
#     imdb_date.append(imdb_information.data['year'])

# t = pd.DataFrame(imdb_date)
# t.to_csv('imdb_date.csv')
test = [release for release in movie_data['release_date']]
imdb_date = pd.read_csv('imdb_date.csv')
corrected_date = []
year = [imdb_year for imdb_year in imdb_date['year']]
print("creating new date field")
for (i, z) in zip(test, year):
    print(i[:-4] + str(z))
    corrected_date.append(str(i[:-4]) + str(z))

movie_data['cleaned_year'] = corrected_date

movie_data.to_csv("cleaned_test.csv")
