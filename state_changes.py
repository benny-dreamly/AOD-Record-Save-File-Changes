import json
import os
import platform
from pathlib import Path

save_file = 'randomizer_save_game.json'

with open('default_save.json') as raw_default_state:
    default_state = json.load(raw_default_state)

default_state_objects = default_state['game_objects']
default_conditions = {
    ('door_open', default_state['door_open']),
    ('safe_open', default_state['safe_open']),
    ('trapdoor_open', default_state['trapdoor_open']),
    ('fire_lit', default_state['fire_lit']),
    ('fire_extinguished', default_state['fire_extinguished'])
}

default_status = [
    (dic['name'], dic['carried'])
    for dic in default_state_objects
    if 'name' in dic and 'carried' in dic
]

default_item_status = set(default_status)

# print("\n", "default status\n\n", default_item_status, "\n")

def compare_items(save):

    changed_state = open_save(save)

    changed_objects = changed_state['game_objects']
    changed_conditions = (changed_state['door_open'],
                            changed_state['safe_open'],
                            changed_state['trapdoor_open'],
                            changed_state['fire_lit'],
                            changed_state['fire_extinguished'])

    changed_status = [
        (dic['name'], dic['carried'])
        for dic in changed_objects
        if 'name' in dic and 'carried' in dic
    ]

    changed_item_status = set(changed_status)

    # print('changed status\n\n', changed_item_status, '\n')

    difference = changed_item_status - default_item_status

    return difference

def open_save(save):
    save_file_path = get_save_file_path() / save
    with open(save_file_path) as raw_changed_state:
        changed_state = json.load(raw_changed_state)
    return changed_state

def get_save_file_path():
    system = platform.system()
    if system == "Windows":
        save_path = Path(os.getenv('LOCALAPPDATA')) / "adventuresofdreamland" / "saves"
    elif system == "Darwin":
        save_path = Path.home() / "Library" / "Application Support" / "adventuresofdreamland" / "saves"
    else:
        save_path = Path.home() / ".local" / "share" / "adventuresofdreamland" / "saves"
    save_path.mkdir(parents=True, exist_ok=True)
    return save_path

def compare_conditions(save):

    changed_state = open_save(save)

    changed_conditions = {
        ('door_open', changed_state['door_open']),
        ('safe_open', changed_state['safe_open']),
        ('trapdoor_open', changed_state['trapdoor_open']),
        ('fire_lit', changed_state['fire_lit']),
        ('fire_extinguished', changed_state['fire_extinguished'])
    }

    condition_difference = changed_conditions - default_conditions

    return condition_difference if condition_difference else None

changed_items = compare_items(save_file)
changed_condition_state = compare_conditions(save_file)

print(changed_items)
if changed_condition_state is not None:
    print(changed_condition_state)
else:
    pass
