# Network Analysis using OpenAI - Capstone Project
## Project Description
This tool seeks to assess the feasibility and possible solutions for the implementation 
of OpenAI's GPT models into network automation. 
## Project Structure
```
    - utils/                    # Utilities
        - prompts/              # A collection of useful prompts that get the openai model to perform tasks reliably
        - generator.py          # The library that generates and filters network traffic from a emulated network
        - trafficgenlib.py      # A network emulator, that generates the data to represent a network in time
        - openaiapi.py          # The OpenAI API handler. Limits querys and handles context prompts
        - key.txt               # (not included in repo) OpenAI API key.
    <!-- - wireshark/           # A collection of network captures that simulate interesting events.  -->
    - main.py                   # The CLI executable
```
## Dependencies
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
tiktoken
openai
```
## Running the Code
Ensure you have all of the dependencies installed with pip install and run 
`python main.py`
## Sources
```
trafficgenlib.py sourced from Nguyen, Son Nam (originally as sands.py)
pcaps sourced from Wireshark 101: Essential Skills for Network Analysis (Chappell University)
```
