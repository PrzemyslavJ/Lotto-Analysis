from itertools import combinations
from random import randint
option = 2 # 1 = chybil trafil, 2 = plaszczyzny fana
comb_list = list(combinations(range(1, 50), 6))
start_index = comb_list.index((1, 2, 3, 4, 5, 6))
counter = 0
optionName = ""

tickets = []
ticketsFan = ((1,2,3,4,5,6),(1,2,3,4,7,8),(1,2,5,6,7,8),(8,9,10,11,16,17),(8,9,12,13,20,21),(8,9,14,15,18,19),(10,11,12,13,18,19),(10,11,14,15,20,21),(12,13,14,15,16,17),(16,17,18,19,20,21),(22,23,24,25,30,31),(22,23,26,27,34,35),(22,23,28,29,32,33),(24,25,26,27,32,33),(24,25,28,29,34,35),(26,27,28,29,30,31),(30,31,32,33,34,35),(36,37,38,39,44,45),(36,37,40,41,48,49),(36,37,42,43,46,47),(38,39,40,41,46,47),(38,39,42,43,48,49),(40,41,42,43,44,45),(44,45,46,47,48,49))
ticketsRandom = []

if option == 1:
    optionName  = "Chybil trafil"
    
    for i in range(24):
        ticketSRandom = comb_list[randint(0,len(comb_list)-1)]
        ticketsRandom.append(ticketSRandom)
    tickets = ticketsRandom
elif option == 2:
    optionName = "Plaszczyzny fana"
    tickets = ticketsFan

print("Losy użyte dla opcji {}".format(optionName))

for i in tickets:
    print(i)

profit_times = 0
profitAll = 0

most_balls_matched = [0 for i in range(0,7)]
winning_tickets = [0 for i in range(0,24)]

for i, comb in enumerate(comb_list[start_index:]):
    #print(f"Draw {i+1}: {comb}", end="")
    counter += 1
    
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

        if matches > this_max_matches:
            this_max_matches = matches

    most_balls_matched[this_max_matches] += 1
    winning_tickets[this_winning_tickets] += 1
    label = "strata"
    if this_prize_total > 72:
        profit_times += 1
        profitAll += this_prize_total
        label = "zysk"
    #print(": {} losy wygralo {} zł ({}) ({} przypadkow zysku).".format(this_winning_tickets,this_prize_total,label,profit_times))

print("Wygrane losy {} ilość trafień {} ilość max wygranych od 0 do 6 {}".format(counter,winning_tickets,most_balls_matched))
print("Dla opcji {} jest {} przypadkow zysku na lacznie {} wszystkich kombinacji co stanowi {} %. Laczny zysk {} zł".format(optionName,profit_times,counter,profit_times/counter*100,profitAll))