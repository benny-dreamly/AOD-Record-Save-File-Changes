import json

with open('default_state.json') as raw_default_state:
    default_state = json.load(raw_default_state)

default_state_objects = default_state['game_objects']

sample_object = default_state_objects[0]

#print(sample_object)

#print(sample_object['name'])
#print(sample_object['carried'])

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

# for dic in changed_objects:
#     if 'name' in dic and 'carried' in dic:
#         item_name = dic['name']
#         carried_item_status = dic['carried']
#         item_status = [item_name, carried_item_status]
#     changed_status.append(item_status)

changed_item_status = set(changed_status)

print('changed status\n\n', changed_item_status)

changed_items = changed_item_status - default_item_status

print(changed_items)

#print(changed_state)

#pairs = zip(default_state_objects, changed_state)

#print([(default_state_objects, changed_state) for default_state_objects, changed_state in pairs if default_state_objects != changed_state])

# set(default_state_objects).intersection(changed_state)