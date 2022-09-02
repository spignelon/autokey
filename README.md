# Autokey
Logging and injecting keystrokes to bypass paste restriction in apps and websites using pynput
---
Autokey consists of two files:
1. ```injector.py``` - Injects keystrokes from a given file to simulate keyboard
2. ```logger.py``` - Keylogger which logs keystrokes into log.txt file
## Setup:
### Cloning the repo:
```
git clone https://github.com/spignelon/autokey.git
cd autokey
```
### Setting up the environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage:
1. ```python injector.py```
2. ```python logger.py```

## Tips:
* injector.py by default uses random.uniform() with range 0 to 0.4, you can edit this range according to your needs, or you can leave it default (will work in most cases). 