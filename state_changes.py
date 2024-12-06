import json

save_file = input('save file?')

with open('default_save.json') as raw_default_state:
    default_state = json.load(raw_default_state)

default_state_objects = default_state['game_objects']

default_status = [
    (dic['name'], dic['carried'])
    for dic in default_state_objects
    if 'name' in dic and 'carried' in dic
]

default_item_status = set(default_status)

# print("\n", "default status\n\n", default_item_status, "\n")

def compareSaves(save_file):

    with open(save_file) as raw_changed_state:
        changed_state = json.load(raw_changed_state)

    changed_objects = changed_state['game_objects']

    changed_status = [
        (dic['name'], dic['carried'])
        for dic in changed_objects
        if 'name' in dic and 'carried' in dic
    ]

    changed_item_status = set(changed_status)

    # print('changed status\n\n', changed_item_status, '\n')

    changed_items = changed_item_status - default_item_status

    return changed_items

changed_items = compareSaves(save_file)

print(changed_items)