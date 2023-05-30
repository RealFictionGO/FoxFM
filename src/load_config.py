from os import listdir
import json
from ui.window_component import Window_Component

def get_window(get_window:bool) -> Window_Component:
    
    if "foxfm_config.json" not in listdir():
        with open("foxfm_config.json", 'w') as f:
            config_pattern = {
                "appearance" : "dark",
                "color_theme" : "blue"
            }

            f.write(json.dumps(config_pattern, indent=2))

    with open("foxfm_config.json", 'r') as f:
        config_file = json.loads(f.read())


    if config_file.get("appearance") == "dark":
        color_stylesheet = {
            "widgets" : "#454444",
        }
    else:
        color_stylesheet = {
            "widgets" : "#b7b4b4",
        }

    if get_window:
        window = Window_Component(config_file.get("appearance"), config_file.get("color_theme"))
        return window, color_stylesheet
    else:
        return color_stylesheet

color_stylesheet = get_window(False)