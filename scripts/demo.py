import requests
import colorama
from urllib.parse import quote
import re
from colorama import Fore, Back, Style

prefix = Style.RESET_ALL + Fore.CYAN + "DPCLab" + Fore.LIGHTCYAN_EX + " Demo |  " + Style.RESET_ALL

def print_spacer():
    print(prefix)

def demo_loop():
    print_spacer()
    print_spacer()
    text = input(prefix + Fore.LIGHTBLACK_EX + "(enter text) " + Fore.MAGENTA)
    response = requests.get("https://ru.dpccdn.net/analyze/" + quote(text, safe=''))).json()
    percent_troll = 100*(response['master'] + 1)/2
    explanation = Style.RESET_ALL + f"— {percent_troll:.1f}% — {len(response['tokenized'])} unique tokens processed"
    if response['master'] > 0.25:
        print(prefix + Fore.RED + "TROLL-LIKE " + explanation)
    elif response['master'] > 0:
        print(prefix + Fore.YELLOW + "MILDLY TROLL-LIKE " + explanation)
    else:
        print(prefix + Fore.GREEN + "NOT TROLL-LIKE " + explanation)

    sentence_formatted = Back.LIGHTBLACK_EX + Fore.BLACK + text
    for word in sorted(response['tokenized'], key=lambda k: abs(response['tokenized'][k]), reverse=True):
        polarity = response['tokenized'][word]
        if abs(polarity) < 0.3:
            continue
        color = Back.LIGHTBLACK_EX
        if polarity > 0.5:
            color = Back.RED
        elif polarity > 0.3:
            color = Fore.RED
        elif polarity < -0.3:
            color = Fore.GREEN
        elif polarity < -0.5:
            color = Back.GREEN
        sentence_formatted = sentence_formatted.replace(word, color + word + Back.LIGHTBLACK_EX + Fore.BLACK)
    print_spacer()
    print(prefix + sentence_formatted + Style.RESET_ALL)
    # print(prefix + Fore.LIGHTBLACK_EX + str(response))


if __name__ == "__main__":
    print(prefix + Fore.LIGHTGREEN_EX + "Russian IRA Tweet Detector — initializing...")
    while True:
        colorama.init()
        demo_loop()