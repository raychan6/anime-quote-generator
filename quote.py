import requests

default_path = "https://animechan.xyz/api/random"

print("Welcome to Anime Quote Generator! Would you like to specify a title? If yes, type in the title. If no, press Enter.")

title_input = input()
title_input = title_input.lower().replace(" ", "_")


if requests.get(default_path).status_code == 200:
    if title_input == "":
        response = requests.get(default_path)
        print(response.json()['quote'] + ' -' + response.json()['character'] + ' (' + response.json()['anime'] + ')')
    else:
        new_path = default_path + "/anime?title=" + title_input

        if requests.get(new_path).status_code == 404:
            print("We couldn't find that title. You may have made a typo, or it could be under a different name.")
        else:
            response = requests.get(new_path) 
            print(response.json()['quote'] + ' -' + response.json()['character'] + ' (' + response.json()['anime'] + ')')
else:
    print("Unable to connect to the server. Please try again later.")