from os import listdir
import json
from ui.window_component import Window_Component

def get_window() -> Window_Component:
    if "foxfm_config.json" not in listdir():
        with open("foxfm_config.json", 'w') as f:
            config_pattern = {
                "appearance" : "System",
                "color_theme" : "blue"
            }

            f.write(json.dumps(config_pattern, indent=2))

    with open("foxfm_config.json", 'r') as f:
        config_file = json.loads(f.read())

    window = Window_Component(config_file.get("appearance"), config_file.get("color_theme"))

    return window