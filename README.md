# Network Analysis using OpenAI - Capstone Project
## Project Description
This tool seeks to assess the feasibility and possible solutions for the implementation 
of OpenAI's GPT models into network automation. It uses the text-davinci-003 model (by default) to read syslog files and analyze individual incidents using the NLP model's abilities. The prompt which it uses to analyze these incidents is called the context prompt, and can be changed at will in the terminal application. There is a web app made with flask and a terminal app made in only python. Dependencies can be found in requirements.txt and apply to both the web and terminal app, the only discrepent package is flask (and it's dependencies), which is only used in the web app. 
## Project Structure
```
    
    - utils/                    # Utilities
        - prompts/              # A collection of useful prompts that get the openai model to perform tasks reliably
        - generator.py          # The library that generates and filters network traffic from a emulated network
        - trafficgenlib.py      # A network emulator, that generates the data to represent a network in time
        - openaiapi.py          # The OpenAI API handler. Limits querys and handles context prompts
        - key.txt               # (not included in repo) OpenAI API key.
    - wireshark/                # A collection of network captures that simulate interesting events.
    - syslog/                   # A collection of syslog files for analysis
        - broadcom              # A syslog file from Broadcom's website, meant to analyze more complicated events.
        - lab                   # A syslog file pulled from a routing lab performed at UW-Stout's Micheels-173 lab.
        - sonnam                # A syslog file generated with trafficgenlib.py
    - templates/                # Flask's templates folder, just a bunch of static site pages.
    - requirements.txt          # The requirements for the project
    - main.py                   # The CLI executable
```
## Running the Code
You can run this project by cloning the repository to your local machine, installing the project requrements with `pip install -r requirements.txt`. Then you can either start up the web interface or the terminal interface with `python app.py` or `python cli.py` respectively. The web app starts on all available interfaces by default, this behavior can be changed at the bottom of app.py, by removing `host='0.0.0.0'`.
## Sources
trafficgenlib.py sourced from Nguyen, Son Nam (originally as sands.py)

pcaps sourced from Wireshark 101: Essential Skills for Network Analysis (Chappell University)

broadcom syslog file sourced from [Broadcom's site](https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/symantec-cloudsoc/cloud/audit-home/barracuda-home/log-formats/syslog-log-sample.html)
