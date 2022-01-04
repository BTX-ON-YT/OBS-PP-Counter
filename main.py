import requests
import time

uid = input("scoresaber user id: ")
while True:
    time.sleep(10)
    with open("pp.txt", 'r+') as f:
        f.truncate(0)
        f.close()
    # response_API = requests.get('https://scoresaber.com/api/player/76561198307100618/full')
    apiurl = ''
    apiurl = apiurl + "https://scoresaber.com/api/player/" + uid + '/full'

    response_API = requests.get(apiurl)

    # print(response_API.json())

    rank = str(response_API.json())

    rank = rank.replace("{", "")
    rank = rank.replace("'", "")
    rank = rank.replace(":", "")
    rank = rank.replace(",", "")
    rank = rank.replace(" ", " \n")

    prank = rank.split("\n",-46)[-46]


    print("pp\n", prank)

    f = open("pp.txt", "w")
    f.write("pp\n")
    f.write(prank)
    f.close()