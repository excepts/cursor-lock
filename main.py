import pythoncom, pyWinhook, os, win32api, win32con, threading, sys, pyautogui
from pynput.keyboard import Listener

def restart(toggle_key):
    main(toggle_key)

def main(toggle_key):
    main_thread_id = win32api.GetCurrentThreadId()

    os.system('cls')

    print(f'TOGGLE KEY > {toggle_key}\n')

    def lock(_):
        return False

    def main_thread_listener(key):
        if key == toggle_key:
            def listen_t():
                def toggle_off(key): 
                    if key == toggle_key:
                        win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0)
                        hm.UnhookMouse()

                        return False

                with Listener(on_press=toggle_off) as listener:
                    listener.join()
                
                restart(toggle_key)

            listen = threading.Thread(target=listen_t)
            listen.start()



            hm = pyWinhook.HookManager()
            hm.MouseMove = lock
            hm.HookMouse()
            pythoncom.PumpMessages()

            sys.exit()
    
    with Listener(on_press=main_thread_listener) as listener:
        listener.join()  

if __name__ == '__main__':
    os.system('title CursorLock')

    print('TOGGLE KEY > ')

    toggle_list = []
    def assign_toggle(key):
        toggle_list.append(key)
        return False

    with Listener(on_press=assign_toggle, suppress=True) as listener:
        listener.join()

    toggle_key = toggle_list[0]
    os.system('cls')

    main(toggle_key)