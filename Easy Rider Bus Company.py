# Easy Rider is the name of the bus company

import json
import re
from datetime import datetime


def check_documentation():
    """checks if the field match the type and format according to the documentation"""

    errors = 0
    bus_id = 0
    stop_id = 0
    next_stop = 0
    stop_name = 0
    stop_type = 0
    a_time = 0
    for dic in inp:
        if type(dic.get('bus_id')) != int:
            bus_id += 1
            errors += 1
        if type(dic.get('stop_id')) != int:
            stop_id += 1
            errors += 1
        if type(dic.get('next_stop')) != int:
            next_stop += 1
            errors += 1
        if not re.match(r'([A-Z]\w* )+(Street|Avenue|Boulevard|Road)$', dic.get('stop_name')):
            stop_name += 1
            errors += 1
        if dic.get('stop_type') not in ['S', 'O', 'F', '']:
            stop_type += 1
            errors += 1
        if not re.match('([0-1][0-9]|2[0-4]):([0-5][0-9])$', dic.get('a_time')):
            a_time += 1
            errors += 1
    print(f'''Format validation: {errors} errors
bus_id: {bus_id}
stop_id: {stop_id}
stop_name: {stop_name}
next_stop: {next_stop}
stop_type: {stop_type}
a_time: {a_time}
''')


def stops_names_and_types():
    """prints stops types (start, end or transfer) and their names"""

    start_stops = set(bus_id.get('stop_name') for bus_id in inp if bus_id.get('stop_type') == 'S')
    print(f'Start stops: {len(start_stops)} {sorted(start_stops)}')
    stop_names = [bus_id.get('stop_name') for bus_id in inp]
    transfer_stops = []
    for name in stop_names:
        if stop_names.count(name) > 1:
            transfer_stops.append(name)
    transfer_stops = set(transfer_stops)
    print(f'Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}')
    finish_stops = set(bus_id.get('stop_name') for bus_id in inp if bus_id.get('stop_type') == 'F')
    print(f'Finish stops: {len(finish_stops)} {sorted(finish_stops)}')

    print('On demand stops test:')
    on_demand = []
    for dic in inp:
        stop_type = dic.get('stop_type')
        stop_name = dic.get('stop_name')
        if stop_type == 'O' and (stop_name in start_stops or stop_name in finish_stops or stop_name in transfer_stops):
            on_demand.append(stop_name)
    if len(on_demand) == 0:
        print('OK')
    else:
        print(f'Wrong stop type: {sorted(on_demand)}')


def bus_id_times():
    """Print how many stops a bus line have"""

    print("Line names and number of stops:")
    ids = [bus_id.get('bus_id') for bus_id in inp]
    set_ids = set(ids)
    for bus_id in set_ids:
        print(f'bus_id: {bus_id}, stops: {ids.count(bus_id)}')


def start_has_end():
    """checks if a bus line have start and end stops"""

    ids = {}
    p = 0
    for dic in inp:
        ids.setdefault(dic.get('bus_id'), [])
        ids[dic.get('bus_id')].append(dic.get('stop_type'))
    for bus_id in ids.keys():
        if ('F' not in ids.get(bus_id)) or ('S' not in ids.get(bus_id)):
            print(f'There is no start or end stop for the line: {bus_id}.')
            p = 1

    if p == 0:
        stops_names_and_types()


def time_travel():
    """Check that the arrival time for the upcoming stops for a given bus line is increasing."""

    bus_ids = []
    time, p, imed_stop = 0, 0, False
    print('Arrival time test:')
    for dic in inp:
        if dic.get('bus_id') not in bus_ids:
            bus_ids.append(dic.get('bus_id'))
            time = datetime.strptime(dic.get('a_time'), '%H:%M').time()
            imed_stop = False
        else:
            if imed_stop:
                continue
            elif datetime.strptime(dic.get('a_time'), '%H:%M').time() <= time:
                print(f'bus_id line {dic.get("bus_id")}: wrong time on station {dic.get("stop_name")}')
                p = 1
                imed_stop = True
            else:
                time = datetime.strptime(dic.get('a_time'), '%H:%M').time()

    if p == 0:
        print('OK')


inp = json.loads(input())

check_documentation()
time_travel()
start_has_end()
bus_id_times()

example_input = """
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "O",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]"""
