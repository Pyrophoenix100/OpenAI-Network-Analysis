import openaiapi
ai = openaiapi.OpenAI()
ai.context_prompt = ""
while (True):
    response = ai.analyze(input("Ask the bot > "))
    print(response.choices[0].text)
    

