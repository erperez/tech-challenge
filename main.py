'''
Data cleaning:
First step: Make sure all 2017 data is from 2017
To do this: Use imdbpy to search for movies based on imdb_id from dataset
Once the id has been retrieved from the api add new column called 'release_date_clean' with the
release date from imdb


'''
import datetime
import time

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
imdb_date = {}

# Uses list comprehension to extract the imdb_id from the dataframe into a stand-alone list
imdb_list = [imdb_id for imdb_id in movie_data['imdb_id']]

# another dictionary I was planning on using to store the converted date time from 01 January 1900 to 01 01 1900
# not currently fully implemented.
release_date = {}

# This loop will grab the imdb_id from our list called `imdb_list` after getting the idea it'll strip out the beginning
# 2 characters leaving only the number part
for id in imdb_list:
    # this will query the imdb website to get all the information based on that movie id
    # such as cast, genres, runtimes, year it was released among others
    # for more information on what it will produce do im.get_movie_infoset()
    imdb_information = (im.get_movie(id[2:]))
    # in this for loop you can get different information from what the api is returning.
    # should be able to access any column by doing imdb_information.data['name of column here']
    for i in imdb_information.data['year']:
        if i['country'] == 'USA\n':
            if len(i) > 2:
                pass
            else:
                imdb_information = i['date']
                break
    imdb_date[id] = imdb_information

# converts date time from 01 January 1900 to 01 01 1900 (not yet implemented completely)
for x in imdb_list:
    release_date.append(datetime.datetime.strptime(x[5:], '%d %B %Y'))
    time.sleep(.5)


