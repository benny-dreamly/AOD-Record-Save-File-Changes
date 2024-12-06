import json
import os
import platform
from pathlib import Path

save_file = 'randomizer_save_game.json'

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

    save_file_path = get_save_file_path() / save_file
    with open(save_file_path) as raw_changed_state:
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

def get_save_file_path():
    system = platform.system
    if system == "Windows":
        save_path = Path(os.getenv('LOCALAPPDATA')) / "adventuresofdreamland" / "saves"
    elif system == "Darwin":
        save_path = Path.home() / "Library" / "Application Support" / "adventuresofdreamland" / "saves
    else:
        save_path = Path.home() / ".local" / "share" / "adventuresofdreamland" / "saves"
    save_path.mkdir(parents=True, exist_ok=True)
    return save_path


changed_items = compareSaves(save_file)

print(changed_items)
