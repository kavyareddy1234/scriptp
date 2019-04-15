import re

def is_movie_name(movie_name):
        if re.match("^[a-zA-Z0-9]+$", movie_name) != None:
                return True
        return False