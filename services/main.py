'''
Source: https://github.com/xtekky/gpt4free
'''
import g4f

from g4f.Provider import (
    Aichat,
    Bard,
    Bing,
    ChatgptAi,
    OpenaiChat,
)

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Update a calendre with meeting on thursday at 4 am."}],
#     stream=True,
# )

# for message in response:
#     print(message, flush=True, end='')

# normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    provider=g4f.Provider.Aichat,
    messages=[{"role": "user", "content": "Extract just Day-Time-Meeting in a text from from following text - I have a meeting with Ai head at 2 pm on MOnday"}],
)  # alternative model setting

print(response)

print("Line by line", type(response))
for line in response.split('\n'):
    # print(a)
    if 'Day' in line:
        print("Day",  line.split(' ')[-1])
    elif 'Time' in line:
        print("Time", line.split(' ')[2:])
    elif 'Meeting' in line:
        print("Purpose: ", line.split(' ')[1:])