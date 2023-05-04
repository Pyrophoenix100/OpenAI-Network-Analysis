import openaiapi
ai = openaiapi.OpenAI()
ai.context_prompt = ""
contextDictArray = []
ai.context.append({"role": "system", "content": "You are a helpful assistant, that will start every message with Eureka!"})
message = input("Ask the bot > ")