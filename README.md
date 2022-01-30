# SpeechHacks
QHacks 2022 Project- Liam Seagram, Jimmy Lu, Nolan Hepworth, Taylor Fiorelli

## Aim
Using AssemblyAPI to perform text-to-speech and analyze the result.

## Dependencies
To run the python code, here are the required installs:
```
pip install requests
```
```
pip install pytube
```
You will also need to create a vault.py file in the same directory as the python files containing the following code:
```python
from typing import NamedTuple

class keys(NamedTuple):
    authkey = "YOUR-ID-KEY"
```
where authkey is set to your personal ID Key for AssemblyAPI. 