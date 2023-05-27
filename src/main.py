from os import listdir
import json
from ui.ui_components import Window_Component


if "foxfm_config.json" not in listdir():
    with open("foxfm_config.json", 'w') as f:
        config_pattern = {
            "appearance" : "System",
            "color_theme" : "blue"
        }

        f.write(json.dumps(config_pattern, indent=2))

f = open("foxfm_config.json", 'r')
config_file = json.loads(f.read())
window = Window_Component(config_file.get("appearance"), config_file.get("color_theme"))
f.close()

window.start()
