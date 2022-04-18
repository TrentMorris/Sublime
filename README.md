### What plugin does
- Removes null objects from json payload and also converts fields that can be converted to integer from string type. 
- Grabs the bidRequest object within the payload. 
## 
##### Create plugin
- Tools -> Developer -> New Plugin
    - Take contents of json.py and copy over default plugin contents
    - Save file to json.py.

## 
##### Add to Sublime KeyMap bindings.
- Open Key Binding
	- Sublime Text -> Preferences -> Key Bindings

- Add key binding to file with keys you'd like to select. 
```json 

[
	{ "keys": ["ctrl+alt+l"], "command": "json" },

]
```
