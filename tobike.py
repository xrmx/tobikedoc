# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Riccardo Magliocchetti (riccardo.magliocchetti@gmail.com)
#
# This file is licensed under the terms of the GNU General Public
# License version 2. This program is licensed "as is" without any
# warranty of any kind, whether express or implied.

import requests
import re

RE = r"{RefreshMap\((?P<data>.*)\)}"

def tobike_bikes(bikes):
    assert len(bikes) == 30

    empty_places = bikes.count('0')
    available_bikes =  bikes.count('4')
    broken_bikes = bikes.count('1') + bikes.count('5')
    filler = bikes.count('x')

    assert empty_places + available_bikes + broken_bikes + filler == 30

    return {
        'empty_places': empty_places,
        'available_bikes': available_bikes,
        'broken_bikes': broken_bikes,
    }

def tobike_to_csv():
    r = requests.get("http://www.tobike.it/frmLeStazioni.aspx")
    r.raise_for_status()

    result = re.search(RE, r.text, re.UNICODE).group("data")
    row = result.split("','")

    ids = row[0].split("|")
    num_votes = row[1].split("|")
    votes = row[2].split("|")
    lats = row[3].split("|")
    lngs = row[4].split("|")
    names = row[5].split("|")
    bikes = row[6].split("|")
    addresses = row[7].split("|")
    statuses = row[8].split("|")

    num_points = len(ids)
    assert num_points == len(num_votes)
    assert num_points == len(votes)
    assert num_points == len(lats)
    assert num_points == len(lngs)
    assert num_points == len(names)
    assert num_points == len(bikes)
    assert num_points == len(addresses)
    assert num_points == len(statuses)

    return [{
        'id': ids[i],
        'num_votes': num_votes[i],
        'vote': votes[i],
        'lat': lats[i],
        'lng': lngs[i],
        'name': names[i],
        'bikes': tobike_bikes(bikes[i]),
        'address': addresses[i],
        'status': statuses[i],
    } for i in range(num_points)]
    
if __name__ == "__main__":
    print(tobike_to_csv())
