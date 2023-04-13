import utils.trafficgenlib as trafficgenlib
import datetime as dt
import json
'''
Rquesting here the trafficgenlib.generate_device_metric_time_range() function to generate data for a period of 30 days, 
with 60 minute frequency, for device PE-4 and specifically for the metric of interest bng_subscribers.
'''
class IncidentGenerator:
    incidents = []

    #Changed frequency to 60 from 5, significantly faster execution
    #Generates the same device with different timestamp/bng_subscribers.
    def __init__(self):
        #Sterilize output
        self.incidents = []

    def listIncidents(self):
        if (self.incidents == []):
            print("No incidents loaded")
        for i, j in enumerate(self.incidents):
            print("(" + str(i) + "): " + j)

    def generateNumberIncidents(self, start_incident, end_incident):
        #Filtering and processing
        output = []
        for i, j in enumerate(self.incidents):
            if i < start_incident:
                continue
            inp = j
            output.append(inp)
            if i >= end_incident - 1:
                break
        return output

    def generateIncidentsPrompt(self, incident_list):
        output = ""
        for i in incident_list:
            output += str(i) + "\n"
        return output
    
    def loadIncidents(self, incident_list):
        self.incidents = incident_list
    
    def generateIncidents(self, length):
        incident_policy = trafficgenlib.generate_incident_policy()
        event_templates = trafficgenlib.generate_event_templates()
        device_inventory = trafficgenlib.generate_device_inventory()
        interface_inventory = trafficgenlib.generate_interface_inventory()
        incidents = trafficgenlib.run_incidents_on_events(dt.datetime.now(), incident_policy, event_templates, length, device_inventory, interface_inventory)
        for i, j in enumerate(incidents):
            self.incidents.append(j['message'])