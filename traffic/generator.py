import trafficgenlib
import datetime as dt
import json

'''
Rquesting here the trafficgenlib.generate_device_metric_time_range() function to generate data for a period of 30 days, 
with 60 minute frequency, for device PE-4 and specifically for the metric of interest bng_subscribers.
'''
#Changed frequency to 60 from 5, significantly faster execution
#Generates the same device with different timestamp/bng_subscribers.
parameters1 = {  'time_delta':600  } 
metric_df = trafficgenlib.generate_device_metric_time_range(dt.datetime.now(), dt.datetime.now() + dt.timedelta(days=30),
            parameters1, ['PE-4'], ['bng_subscribers'])
incidents = trafficgenlib.run_incidents_on_events(dt.datetime.now(), trafficgenlib.generate_incident_policy(), trafficgenlib.generate_event_templates(), 30, trafficgenlib.generate_device_inventory(), trafficgenlib.generate_interface_inventory())
a = open("C:/Users/TuchschererAlec/OneDrive - University of Wisconsin-Stout/Classes/Spring 2023/CNIT-490/Week 3-5 Notes/logs_tools/output.xlsx", "w+")
a.write(metric_df.to_csv())
with open("C:/Users/TuchschererAlec/OneDrive - University of Wisconsin-Stout/Classes/Spring 2023/CNIT-490/Week 3-5 Notes/logs_tools/output.xlsx") as output:
    output.write(incidents)
    print(incidents)