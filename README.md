#Network Analysis using OpenAI - Capstone Project
##Project Description
This tool seeks to assess the feasibility and possible solutions for the implementation 
of OpenAI's GPT models into network automation. 
##Project Structure
```
    - traffic/ # A generator for network traffic written by the capstone sponsor
        - generator.py # The library that generates and filters network traffic from a emulated network
        - trafficgenlib.py # A network emulator, that generates the data to represent a network in time
    - wireshark/ # A collection of network captures that simulate interesting events. 
    - openai/ # OpenAI handler. Manages token usage and appends prompts for context evasion.
        - openaiapi.py # The python file itself. Built as a library.
        - key.txt # (not included in repo) OpenAI API key.
```
##Dependencies
```
json
requests
pandas
time
urllib3
calendar
datetime
math
numpy
collections
warnings
```
##Running the Code
Ensure you have all of the dependencies installed with pip install and run 
`python main.py`