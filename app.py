from config import API_KEY, APP_URL
import requests
import json
from utils import is_movie_name

def search_for_movie(name):
         api_url = "%s?apikey=%s&t=%s" % (APP_URL, API_KEY, name)

         try:

                r = requests.get(api_url)

                if r.status_code == 200:

                        json_rsp = r.json()

                        if json_rsp['Response'] == "True":

                                return json_rsp

                        else:

                                print ("####################")
                                print ("Results not found for given movie name = %s") % (name)
                                print ("####################")

                                exit(1)
                else:
                        print ("####################")
                        print ("Error occured while making the request  to the url = %s") % (api_url)
                        print ("Status_code = %s, message = %s") % (r.status_code, r.text)
                        print ("####################")

         except Exception as e:
                print ("####################")
                print ("Exception occured = %s") %str(e)
                print ("####################")


if __name__ == "__main__":

        import sys

        if len(sys.argv) == 2:

                name = sys.argv[1]
                if is_movie_name(name):
                        search_result = search_for_movie(name)
                        print ("####################")
                        print ("Details of the movie =%s") %(name)
                        print ("####################")
                        for item in search_result.keys():
                                print ("%s = %s") % (item, search_result[item])
                        print ("####################")
                else:
                        print ("####################")
                        print ("Invalid movie name entered = %s, please enter valid movie name") % (name)
                        print ("####################")

                        exit(1)
        else:
                print ("####################")
                print ("Please enter the valid number of arguments, e.g python app.py Indra")
                print ("####################")
                exit(1)