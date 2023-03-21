import openai
import os
from generator import IncidentGenerator
keyfile = open(os.path.join(os.path.dirname(__file__), "key.txt"), "r")
incidents = IncidentGenerator(num_incidents=1)
openai.api_key = keyfile.read()
context_prompt = "Respond with a possible fix or cause for the following errors"
prompt = incidents.generateIncidentsPrompt()
output = openai.Completion.create(
  model="text-davinci-003",
  prompt= context_prompt + prompt,
  max_tokens= 100, #max tokens to generate
  temperature= 0 #randomness, between 0 and 2, higher values will make output more random
)
print("Prompt:\n" + prompt)
print(output.choices[0].text)