from colorama import Fore, init
import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()
init()

token = os.getenv('TOKEN')
channel_id = os.getenv('CHANNEL_ID')
messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'no', 'ikr']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

print(f'''
{Fore.CYAN}

             $$$$$$\              $$\               $$\                               $$\ 
            $$  __$$\             $$ |              $$ |                              $$ |
            $$ /  $$ |$$\   $$\ $$$$$$\    $$$$$$\  $$ | $$$$$$\ $$\    $$\  $$$$$$\  $$ |
            $$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\ $$ |$$  __$$\\$$\  $$  |$$  __$$\ $$ |
            $$  __$$ |$$ |  $$ |  $$ |    $$ /  $$ |$$ |$$$$$$$$ |\$$\$$  / $$$$$$$$ |$$ |
            $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |$$   ____| \$$$  /  $$   ____|$$ |
            $$ |  $$ |\$$$$$$  |  \$$$$  |\$$$$$$  |$$ |\$$$$$$$\   \$  /   \$$$$$$$\ $$ |
            \__|  \__| \______/    \____/  \______/ \__| \_______|   \_/     \_______|\__|                                                                                                                       
{Fore.RESET}       
    ---------------------------------------------------------------------------------------------                                                                    
                                                                                    
''')

while True:
    wait_time = random.randint(70, 200)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'            {Fore.YELLOW}[%] {Fore.YELLOW}[{r.status_code}] {Fore.LIGHTBLACK_EX}[Waiting {str(wait_time)} seconds or {str(wait_time/60)[0:4]} minutes...] {Fore.RESET} Sent message > {message}')
    time.sleep(wait_time)
