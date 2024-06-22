from pynput import mouse, keyboard
import multiprocessing
from events_tracker import on_move,on_click,on_press,on_release,on_scroll,stopper


manager = multiprocessing.Manager()
logs = manager.list()

mouse_listener = mouse.Listener(
    on_move=lambda x, y: on_move(x, y, logs),
    on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, logs),
    on_scroll=lambda x, y, dx, dy: on_scroll(x, y, dx, dy, logs)
)

keyboard_listener = keyboard.Listener(
    on_press=lambda key: on_press(key, logs),
    on_release=lambda key: on_release(key, logs)
)


mouse_listener.start()
keyboard_listener.start()

stopper_process = multiprocessing.Process(target=stopper, args=(logs,))
stopper_process.start()

stopper_process.join()
mouse_listener.join()
keyboard_listener.join()
