# SpeechHacks
QHacks 2022 Project- Liam Seagram, Jimmy Lu, Nolan Hepworth, Taylor Fiorelli

## Aim
Using AssemblyAPI to perform text-to-speech and summarize the result.

## Dependencies/Installations
To run the python code located in the scripts folder, here are the required installs:
```
pip install requests
```
```
pip install pytube
```
Next, you will need to install the nltk librairy to make the summarizer work. Here is the method that will work for local machines:
```
pip install nltk
```
Once that is done, run these two commands consecutively in python 3:
```
import nltk
nltk.download()
```
This should open a download window for nltk. More extensive instructions and other methods for installing nltk can be found here:
https://www.nltk.org/data.html

## Vault.py file for API key
You will also need to create a vault.py file in the same directory as the python files containing the following code:
```python
from typing import NamedTuple

class keys(NamedTuple):
    authkey = "YOUR-ID-KEY"
```
where authkey is set to your personal ID Key for AssemblyAPI. 