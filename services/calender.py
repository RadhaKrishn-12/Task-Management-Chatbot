'''
Source: https://github.com/xtekky/gpt4free
'''
import g4f
import json
from g4f.Provider import (
    Aichat,
    Bard,
    Bing,
    ChatgptAi,
    OpenaiChat,
)


def create_new_user_calender(user_name):
    new_user_calender = {"Monday": {"am": [] , "pm": [] },
                    "Tuesday": {"am": [], "pm": []},
                    "Wednesday": {"am": [], "pm": []},
                    "Thursday": {"am": [], "pm": []},
                    "Friday": {"am": [], "pm": []},
                    "Saturday": {"am": [], "pm": []},
                    "Sunday": {"am": [], "pm": []}
                    }
    
    with open(f'./services/jsons/{user_name}_calender.json', 'w') as json_file:
        json.dump(new_user_calender, json_file)
    

user_calender = {"Monday": {"am": [{"1": "Meeting with VP"}, {"6": "Yoga lesson"}] , "pm": [{"2": "Lunch with team"}] },
                 "Tuesday": {"am": [], "pm": []},
                 "Wednesday": {"am": [], "pm": []},
                 "Thursday": {"am": [], "pm": []},
                 "Friday": {"am": [], "pm": []},
                 "Saturday": {"am": [], "pm": []},
                 "Sunday": {"am": [], "pm": []}
                 }

def create_meet(user_calender, update_task):
    try:
        if 'am' in update_task[1]:
            user_calender[update_task[0]]['am'].append({update_task[1].split(' ')[0] : update_task[2]})
        elif 'pm' in update_task[1]:
            user_calender[update_task[0]]['pm'].append({update_task[1].split(' ')[0] : update_task[2]})
    except:
        pass

def remove_meet(user_calender, update_task):
    try:
        meet_time = update_task[1].split(' ')[0] 
        if 'am' in update_task[1]:
            user_calender[update_task[0]]['am'] = [d for d in user_calender[update_task[0]]['am'] if meet_time not in d]
        elif 'pm' in update_task[1]:
            user_calender[update_task[0]]['pm'] = [d for d in user_calender[update_task[0]]['pm'] if meet_time not in d]
    except:
        pass


def g4_response(request, web_chat_request, request_type):

    # To load the user calender
    user_calender = {}
    with open(f'./services/jsons/{request.user}_calender.json', 'r') as json_file:
        user_calender = json.load(json_file)

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        # provider=g4f.Provider.Aichat,
        messages=[{"role": "user", "content": f"Extract just Day-Time-Meeting from a following text- {web_chat_request}. Output as Day- newline Time newline Meeting Purpose - "
                   }],
    )

    print("g4_response", response)

    print("Line by line for Meeting", type(response))

    lines = response.split('\n')
    update_task = []
    for idx, line in enumerate(lines):
        # print(a)
        # if 'Day' in line:
        #     print("Day",  line.split(' ')[-1])
        # elif 'Time' in line:
        #     print("Time", line.split(' ')[2:])
        # elif 'Meeting' in line:
        #     print("Purpose: ", line.split(' ')[1:])

        if 'Day' in line:
            print("Day",  lines[idx+1])
            update_task.append(lines[idx+1])
        elif 'Time' in line:
            print("Time", lines[idx+1])
            update_task.append(lines[idx+1])
        elif 'Meeting' in line:
            print("Purpose: ", lines[idx+1])
            update_task.append(lines[idx+1])
    
    # Update calender according to requests
    if request_type == "create":
        create_meet(user_calender, update_task)
    elif request_type == "remove":
        remove_meet(user_calender, update_task)
    elif request_type == "update":
        remove_meet(user_calender, update_task)
        create_meet(user_calender, update_task)

    
    with open(f'./services/jsons/{request.user}_calender.json', 'w') as json_file:
        json.dump(user_calender, json_file)
        print("Calender is updated")


    
