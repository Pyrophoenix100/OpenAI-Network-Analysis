def flushBuffer(lines=32):
    for i in range(lines):
        print("\n")

def conditionalInput(prompt, condition):
    while (True):
        inp = input(prompt)
        if condition(inp) == True:
            return inp
        else:
            print("Please enter a valid option")
            continue


from openaiapi import OpenAI
import os
print("Neural Network Automation =====================")
print("Generating traffic...")
from generator import IncidentGenerator
incidents = IncidentGenerator()
with open(os.getcwd() + "/syslog/sonnam", "w+") as output:
    for i in incidents.incidents:
        output.write(i + "\n")
ai = OpenAI()
flushBuffer()
print("Neural Network Automation =====================")
inp = 0
while (inp != 9):
    print("1: List incidents")
    print("2: Analyze incident")
    print("3: GPT options")
    print("4: Import Syslog file")
    print("9: Quit")
    try:
        inp = int(input("> "))
    except KeyboardInterrupt:
        os._exit(-1)
    except:
        continue

    if (inp == 1): #List Incidents
        incidents.listIncidents()
    elif (inp == 2): #Analyze Incident
        start = int(conditionalInput("Start Incident #: ", lambda x: 0 < int(x) < len(incidents.incidents) - 1))
        end = conditionalInput("End Incident # [single]: ", lambda x: x == "" or start < int(x) < len(incidents.incidents) - 1)
        if end == "":
            end = start
        else:
            end = int(end)
        prompt = incidents.generateIncidentsPrompt( incidents.generateNumberIncidents(start, end) )
        analysis = ai.analyze(prompt)
        print(analysis.choices[0].text)
    elif (inp == 3): #GPT Options
        while (inp != 0):
            print("1: Context Prompt")
            print("2: Max Tokens [" + str(ai.max_generation) + "]")
            print("3: Change Model [" + ai.model_lookup[ai.model] + "]")
            print("0: Quit")
            inp = int(input("> "))
            if (inp == 1): #Context Prompt
                print("Current prompt: " + ai.context_prompt)
                new_prompt = input("New prompt [no change]> ")
                if (new_prompt == ""):
                    continue
                else: 
                    ai.context_prompt = new_prompt
            elif (inp == 2): #Number of tokens
                new_tokens = conditionalInput("Number of tokens (Max 2048) [no change]> ", lambda x: x == "" or 0 < int(x) <= 2048)
                if (new_tokens == ""):
                    continue
                else: 
                    ai.max_generation = int(new_tokens)
            elif (inp == 3):
                for i in ai.model_lookup:
                    print(str(i) + ": " + ai.model_lookup[i])
                new_model = conditionalInput("Select a model [no change]> ", lambda x: 0 <= int(x) < len(ai.model_lookup) )
                if (new_model == ""):
                    continue
                else: 
                    ai.model = int(new_model)
            elif (inp == 0):
                break
            else:
                print("Enter a valid input.")
    elif (inp == 4): #Import Syslog File
        syslogfiles = os.listdir(os.getcwd() + "/syslog")
        for i, j in enumerate(syslogfiles):
            print(str(i+1) + ": " + str(j))
        file = conditionalInput("Select a syslog file [cancel]: ", lambda x: x == "" or 0 < int(x) <= len(syslogfiles))
        if (file == ""):
            continue    
        else:
            with open(os.getcwd() + "/syslog/" + syslogfiles[int(file)-1]) as syslog:
                incidents.loadIncidents(syslog.readlines())
            print("Loaded syslog file successfully!")
    elif (inp == 9):
        pass
    else:
        print("Enter a valid input.")
