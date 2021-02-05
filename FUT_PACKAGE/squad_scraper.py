from bs4 import BeautifulSoup
import requests
import re
file = open("data.in", "w")
n = 3
temp = 4756582


#22 columns, first 11 starting(no playing position).
# last 11 final team with playing position
#page = BeautifulSoup("https://www.futbin.com/community/squads/builder?page=" + str(n), features="lxml")
while True:
    page = requests.get("https://www.futbin.com/21/squad/"+ str(n))
    n += 1
    soup = BeautifulSoup(page.content, 'html5lib')
    #print(soup.prettify())

    ###getting formation
    formation = soup.find('div', attrs = {'class': 'container squad-mobile-fix'})
    n = 0
    for i in formation:
        if not n:
            n += 1
            continue
        temp = i
        break
    final_formation = temp["data-formation"]



    ###get players
    for player_id in range(1, 12,1):
        player = soup.find('div', attrs = {'class': 'card cardnum ui-droppable added', 'data-cardid':str(player_id)})
        print(player)
    #formation = temp.find('div', attrs={'data-year="21': '21'}))
    #print(formation.prettify())
    # for i in formation:
    #     temp = formation.find('div', attrs={'data-year="21': '21'})
    #     #if temp is not None:
    #         #print("hhhe")
    #print(formation.prettify())
    #q = []
    # player = 1
    # for i in range(1,12,1):
    #     table = soup.find('div', attrs = {'class': 'card cardnum ui-droppable added', 'data-cardid':str(i)})
    #     nation = table.find('div', attrs = {'class': 'pcdisplay-nation-name hide'})
    #     original_pos = table.find('div', attrs = {'class' : re.compile('pcdisplay ut21*')})
    #     print(table)
        #print(nation)
        #print(table.prettify())
    #for row in table.findAll('div', attrs = {'class' : 'card cardnum ui-droppable added'}):
        #print(row.prettify())


    break
