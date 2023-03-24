import random
import openai

openai.api_key = "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"

engine = "text-davinci-003"
prompt = input("")
max_tokens = 2048

python = "python"
html = "html"
css = "css"
java = "java"
cpp = "C++"
code_generate = "create a code"

while True:
    if(prompt != "exit"):
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens
        )
        print(response["choices"][0]["text"])

        if(code_generate in prompt):
            if python in prompt:
                with open("output.py", "w") as file:
                    file.write(response["choices"][0]["text"])
            elif html in prompt: 
                with open("output.html", "w") as file:
                    file.write(response["choices"][0]["text"])
            elif css in prompt:
                with open("output.css", "w") as file:
                    file.write(response["choices"][0]["text"])
            elif java in prompt:
                with open("output.java", "w") as file:
                    file.write(response["choices"][0]["text"])
            elif cpp in prompt:
                with open("output.cpp", "w") as file:
                    file.write(response["choices"][0]["text"])
        
        prompt = input("")
    else:
        exit()