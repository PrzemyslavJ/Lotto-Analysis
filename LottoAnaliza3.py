from itertools import combinations
import csv
from random import randint

tickets = []
ticketsFan = ((1,2,3,4,5,6),(1,2,3,4,7,8),(1,2,5,6,7,8),(8,9,10,11,16,17),(8,9,12,13,20,21),(8,9,14,15,18,19),(10,11,12,13,18,19),(10,11,14,15,20,21),(12,13,14,15,16,17),(16,17,18,19,20,21),(22,23,24,25,30,31),(22,23,26,27,34,35),(22,23,28,29,32,33),(24,25,26,27,32,33),(24,25,28,29,34,35),(26,27,28,29,30,31),(30,31,32,33,34,35),(36,37,38,39,44,45),(36,37,40,41,48,49),(36,37,42,43,46,47),(38,39,40,41,46,47),(38,39,42,43,48,49),(40,41,42,43,44,45),(44,45,46,47,48,49))
ticketsRandom = []
option = 2 # 1 = chybil trafil, 2 = plaszczyzny fana
counter = 0
comb_list = list(combinations(range(1, 50), 6))

if option == 1:
    optionName  = "Chybil trafil"
    
    for i in range(24):
        ticketSRandom = comb_list[randint(0,len(comb_list)-1)]
        ticketsRandom.append(ticketSRandom)
    tickets = ticketsRandom
elif option == 2:
    optionName = "Plaszczyzny fana"
    tickets = ticketsFan

 
# csv file name
filename = "WynikiHisDuzyLotto.csv"
 
# initializing the titles and rows list
fields = []
rows = []

Los = []
ListLosses = []


 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile,delimiter=";")
 
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for row in rows:
    # parsing each column of a row
    Los = []
    for col in row:
        Los.append(int(col))

    lostT = tuple(Los)
    ListLosses.append(lostT)

profit_times = 0
profitAll = 0

most_balls_matched = [0 for i in range(0,7)]
winning_tickets = [0 for i in range(0,24)]

number = len(ListLosses)-1
comb = ListLosses[number]

print("Dla losowania nr {} : {} otrzymano następujące wyniki".format(number,comb))

this_max_matches = 0
this_prize_total = 0
this_winning_tickets = 0
for ticket in tickets:
    matches = len(set(comb).intersection(ticket))
    # print("matches for this ticket: {} - {}".format(ticket,matches))
    if matches > 2:
        this_winning_tickets += 1
        if matches == 3:
            this_prize_total += 24
        elif matches == 4:
            this_prize_total += 260
        elif matches == 5:
            this_prize_total += 5000
        elif matches == 6:
            this_prize_total += 2000000

        print("Wygrany los {} wygrał {}".format(ticket,this_prize_total))


        if matches > this_max_matches:
            this_max_matches = matches

most_balls_matched[this_max_matches] += 1
winning_tickets[this_winning_tickets] += 1

label = "strata"
if this_prize_total > 72:
    profit_times += 1
    profitAll += this_prize_total
    label = "zysk"
print(": {} losy wygralo {} zł ({}) ({} przypadkow zysku lacznie).".format(this_winning_tickets,this_prize_total,label,profit_times))

print("Wygrane losy {} ilość trafień losow {} ilość max wygranych od 0 do 6 {}".format(counter,winning_tickets,most_balls_matched))
