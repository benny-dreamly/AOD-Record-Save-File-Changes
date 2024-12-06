import json

with open('default_state.json') as raw_default_state:
    default_state = json.load(raw_default_state)

default_state_objects = default_state['game_objects']

default_status = [
    (dic['name'], dic['carried'])
    for dic in default_state_objects
    if 'name' in dic and 'carried' in dic
]

default_item_status = set(default_status)

print("\n", "default status\n\n", default_item_status, "\n")

with open('Scroll.json') as raw_changed_state:
    changed_state = json.load(raw_changed_state)

changed_objects = changed_state['game_objects']

changed_status = [
    (dic['name'], dic['carried'])
    for dic in changed_objects
    if 'name' in dic and 'carried' in dic
]

changed_item_status = set(changed_status)

print('changed status\n\n', changed_item_status)

changed_items = changed_item_status - default_item_status

print(changed_items)