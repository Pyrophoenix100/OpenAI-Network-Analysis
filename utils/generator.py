import trafficgenlib
import datetime as dt
import json
'''
Rquesting here the trafficgenlib.generate_device_metric_time_range() function to generate data for a period of 30 days, 
with 60 minute frequency, for device PE-4 and specifically for the metric of interest bng_subscribers.
'''
class IncidentGenerator:
    incident_policy = trafficgenlib.generate_incident_policy()
    event_templates = trafficgenlib.generate_event_templates()
    device_inventory = trafficgenlib.generate_device_inventory()
    interface_inventory = trafficgenlib.generate_interface_inventory()
    gpt_input = []
    #Changed frequency to 60 from 5, significantly faster execution
    #Generates the same device with different timestamp/bng_subscribers.
    def __init__(self, num_incidents = 10):
        self.incidents = trafficgenlib.run_incidents_on_events(dt.datetime.now(), self.incident_policy, self.event_templates, 30, self.device_inventory, self.interface_inventory)
        self.gpt_input = []
        #Filtering and processing
        for i, j in enumerate(self.incidents):
            inp = j['source'] + ": " + j['message']
            self.gpt_input.append(inp)
            if i >= num_incidents:
                break
    def generateIncidentsPrompt(self):
        output = ""
        for i in self.gpt_input:
            output += str(i) + "\n"
        return output