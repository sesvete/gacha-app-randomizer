import random
from datetime import datetime

pulls = []

class PulledUnit:
    def __init__(self, date, from_banner, num_of_pulls, unit_name):
        self.date = date
        self.from_banner = from_banner
        self.num_of_pulls = num_of_pulls
        self.unit_name = unit_name

    def __str__(self):
        """
        Returns a user-friendly string representation of the PulledUnit.
        """
        return f"Pulled '{self.unit_name}' on {self.date} won 50/50 '{self.from_banner}' (after {self.num_of_pulls} pulls)."

    def __repr__(self):
        """
        Returns a string representation that can be used to recreate the object.
        """
        return (f"PulledUnit(date='{self.date}', from_banner='{self.from_banner}', "
                f"num_of_pulls={self.num_of_pulls}, unit_name='{self.unit_name}')")




# https://github.com/sesvete/python_code_laptop_2022-2024/blob/main/genshin_impact_wishing/wishing_simulator.py

# to si malo poglej pa pogruntaj zdaj se mi res ne da

# POTEK FUNKCIJE
# 1) izbral bom mode SQL, NoSQL - SQL bo direk pisala v bazo, NoSQL bo naredila JSON
# 2) izbral bom koliko bo uporabnikov
# 3) Izbral bom koliko pullov se bo naredilo za vsak banner
# 4) funkcija se izvede

# na primer da imamo genshin limited banner
# mora se pobrati koliko je soft pity, koliko je rate za fivestar pull, kolikšen je rate za FromBanner win
# gleda se tudi, če je standard ali limited banner - pri standar bannerju ne gledamo
# guaranteed vedno štarta s False in pull count z 0
# za weapon banner je soft pity 65 win rate pa 0,75

# torej delal se bo loop
# na primer če imamo 50 uporabnikov in 50 pullov
# prvi uporabnik gre na genshin impact limited banner
# vnesejo se spremenljive, izvede se in vpiše se v dictionary
# iterira se za vsak banner za vsako igro in za vsakega uporabnika

# ta je funkcija, ki se izvede, ko dejankso dobim 5 star in izračunamo, če smo zmagal 50/50
def pull_limited_five_star(guaranteed, is_weapon_banner):
    if guaranteed == False:
        win = random.random()
        if is_weapon_banner:
            pull_rate = 0.75
        else:
            pull_rate = 0.5
        if win < pull_rate:
            unit_name = "FROM BANNER"
            from_banner = True
            guaranteed = False
        else:
            unit_name = "STANDARD UNIT"
            from_banner = False
            guaranteed = True
    else:
        unit_name = "FROM BANNER"
        guaranteed = False
        from_banner = True
    return guaranteed, unit_name, from_banner

"""
def full_odds(pull, num_of_pulls, guaranteed, is_weapon_banner):
    if pull < 0.006:
        guaranteed, unit_name, from_banner = pull_limited_five_star(guaranteed, is_weapon_banner)
        pulled_unit = PulledUnit(datetime.now(), guaranteed, num_of_pulls, unit_name)
        pulls.append(pulled_unit)
        keep_pulling = False
    else:
        keep_pulling = True
    return guaranteed, keep_pulling
"""



#single pull without pity
def single_pull(num_of_pulls, guaranteed, is_weapon_banner):
    num_of_pulls += 1
    pull = random.random()
    # if pull < 74 full odds
    # if pull 74 < x < 90 - 32,4%
    # if pull = 90 guarantee
    if num_of_pulls < 75:
        rate = 0.006
    elif 74 < num_of_pulls < 90:
        rate = 0.324
    else:
        rate = 1

    if pull < rate:
        guaranteed, unit_name, from_banner = pull_limited_five_star(guaranteed, is_weapon_banner)
        #tle se mora še izpisat enota
        pulled_unit = PulledUnit(datetime.now(), guaranteed, num_of_pulls, unit_name)
        pulls.append(pulled_unit)
        keep_pulling = False
    else:
        keep_pulling = True
    return num_of_pulls, guaranteed, keep_pulling


#single pull soft pity (32,4%)
# hočem pullad dokler ne dobim 5 star
for amount in range(100):
    num_of_pulls = 0
    keep_pulling = True
    while keep_pulling:
        num_of_pulls, guaranteed, keep_pulling = single_pull(num_of_pulls, False, False)


print(pulls)

for unit in pulls:
    print(unit.num_of_pulls)


#TODO: soft pity (from 75 onward the probability should be around 35 %)
#TODO: guaranteed on 90th pull
#TODO: implement 50/50 guaranteed win