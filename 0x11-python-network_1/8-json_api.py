#!/usr/bin/python3
"""  takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as
a parameter. """

if __name__ == "__main__":
    import requests
    from sys import argv

    arg = ""
    if len(argv) >= 2:
        arg = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': arg})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
