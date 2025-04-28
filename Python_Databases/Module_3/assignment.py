# This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:

import sqlite3

# connect to the database
conn = sqlite3.connect('C:\\Repos\\python-for-everybody\\Python_Databases\\DB\\trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
                  
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
handle = open('C:\\Repos\\python-for-everybody\\Python_Databases\\Module_3\\tracks\\tracks.csv')

# loop through each line in the file
for line in handle:
    line = line.strip(); # remove whitespace from the beginning and end of the line
    pieces = line.split(',') # split the line into pieces using comma as the delimiter
    if len(pieces) < 6 : continue # skip lines that don't have enough pieces

    # assign each piece to a variable
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # print the variables to check the values
    print(name, artist, album, count, rating, length, genre)

    # insert the artist into the Artist table
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, )) # get the id of the artist
    artist_id = cur.fetchone()[0] # fetch the id of the artist

    # insert the genre into the Genre table
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, )) # get the id of the genre
    genre_id = cur.fetchone()[0] # fetch the id of the genre

    # insert the album into the Album table
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, )) # get the id of the album
    album_id = cur.fetchone()[0] # fetch the id of the album

    # insert the track into the Track table
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count ) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )

    # commit the changes to the database
    conn.commit()
