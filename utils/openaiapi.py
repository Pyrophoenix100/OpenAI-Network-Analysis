import openai
import os
class OpenAI:
  context_prompt = "Respond with a possible fix or cause for the following errors"
  
  max_generation = 500
  model_lookup = {0: "text-davinci-003", 1: "ada", 2: "davinci"}
  model = 0
  def __init__(self):
    keyfile = open(os.path.join(os.path.dirname(__file__), "key.txt"), "r")
    openai.api_key = keyfile.read()

  def analyze(self, incident_prompt):
    try:
      output = openai.Completion.create(
        model=self.model_lookup[self.model],
        prompt= self.context_prompt + incident_prompt,
        max_tokens= self.max_generation #max tokens to generate
      )
    except:
      output = "Error in settings"
    return output
  def configGenerate(self, config_prompt):
    try:
      prompt_file = open(os.getcwd() + "/prompts/Cisco-Config-Generation.txt")
      context_prompt = prompt_file.readline()
      output = openai.Completion.create(
        model=self.model_lookup[self.model],
        prompt= context_prompt + "\n" + config_prompt,
        max_tokens= self.max_generation, #max tokens to generate
        temperature= 0 #randomness, between 0 and 2, higher values will make output more random
      )
    except:
      output = "Error in settings"
    return output