#from pynput import keyboard
from pynput.keyboard import Key, Controller
import pynput
import time
#------------------------------------------------v
#ctr = pynput.keyboard.Controller()
#get = pynput.keyboard.Listener()
#events = pynput.keyboard.Events()
keys = pynput.keyboard.Controller()
# time_b = time.localtime(time.time())
# datatime_b = time.strftime('%Y-%m-%d,%H:%M:%S',time_b)
# print("Data time",datatime_b)
# key.press(pynput.keyboard.KeyCode.from_vk(97))
with pynput.keyboard.Events() as events:
    for event in events:
        if event.key == pynput.keyboard.Key.esc:
            break
        # elif event.key == pynput.keyboard.Events.Press('1'):
        #     print('Test OK')
        #     key.press('A')
        #     time.sleep(1)
        #     key.release('A')
        # Windows key cmd test
        elif event.key == pynput.keyboard.KeyCode.from_char('v'):
            time.sleep(5)
            keys.press(Key.cmd)
            time.sleep(2)
            keys.release(Key.cmd)
        elif event.key == pynput.keyboard.KeyCode.from_char('1'):
            time.sleep(0)           # Adjust the delay time when the key pressed
            keys.press(Key.alt_l)
            time.sleep(0.1)         # Adjust the two key sequence delay time
            keys.press('q')
            keys.release(Key.alt_l)
            keys.release('q')
        elif event.key == pynput.keyboard.KeyCode.from_char('2'):
            time.sleep(0)           # Adjust the delay time when the key pressed
            keys.press(Key.alt_l)
            time.sleep(0.1)         # Adjust the two key sequence delay time
            keys.press('w')
            keys.release(Key.alt_l)
            keys.release('w')
        elif event.key == pynput.keyboard.KeyCode.from_char('3'):
            time.sleep(0)           # Adjust the delay time when the key pressed
            keys.press(Key.alt_l)
            time.sleep(0.1)         # Adjust the two key sequence delay time
            keys.press('a')
            keys.release(Key.alt_l)
            keys.release('a')
        elif event.key == pynput.keyboard.KeyCode.from_char('4'):
            time.sleep(0)           # Adjust the delay time when the key pressed
            keys.press(Key.alt_l)
            time.sleep(0.1)         # Adjust the two key sequence delay time
            keys.press('d')
            keys.release(Key.alt_l)
            keys.release('d')
        elif event.key == pynput.keyboard.KeyCode.from_char('5'):
            time.sleep(0)           # Adjust the delay time when the key pressed
            keys.press(Key.alt_l)
            time.sleep(0.1)         # Adjust the two key sequence delay time
            keys.press(Key.tab)
            keys.release(Key.alt_l)
            keys.release(Key.tab)
        else:
            print('Received event {}'.format(event))
            # with open("KeyBoardLog.txt", 'w', encoding='utf-8') as log:
            #     count = log.write(str(event))
            #     print(str(event)+"-Test")
            #
            time_b = time.localtime(time.time())                        # Get the system time
            datatime_b = time.strftime('%Y-%m-%d,%H:%M:%S', time_b)     # Reform the time struction
            log = open("KeyBoardLog.txt",'a',encoding='utf-8')          # Open/New and Write in the file
            time.sleep(0)                                               # Set the writing delay time
            log.write(str(datatime_b)+'-'+str(event)+'\n')              # File's form`
            log.close()                                                 # File close





#ctr.press(pynput.keyboard.key.ctrl)
#ctr.press('v')
#ctr.relese(pynput.keyboard.key.ctrl)
#ctr.relese('v')
#------------------------------------------------
#keyboard = Controller()
# Press and release space
# keyboard.press(Key.space)
#keyboard.release(Key.space)
#------------------------------------------------
# Timer test
# print('Timer start')
# time.sleep(0.1)
# print('Timer end')
#------------------------------------------------
# physical keyboard is labelled
# Test line:
# key = input('Please enter the Key:')
#keyboard.press('key')
#keyboard.press('ctrl')

#keyboard.press(Key.ctrl)
# keyboard.release(Key.ctrl)
#time.sleep(0.1)
#keyboard.press('c')
#keyboard.release('a')

# Type two upper case As
# keyboard.press('A')
#keyboard.release('A')
#with keyboard.pressed(Key.shift):
#    keyboard.press('a')
#    keyboard.release('a')

# Type 'Hello World' using the shortcut type method
#keyboard.type('Hello World')



# Recording the KeyBoard Input
#def on_press(key):
#    try:
#        print('alphanumeric key {0} pressed'.format(
#            key.char))
#    except AttributeError:
#        print('special key {0} pressed'.format(
#            key))
#
#def on_release(key):
#    print('{0} released'.format(
#        key))
#    if key == keyboard.Key.esc:
#        # Stop listener
#        return False
#
## Collect events until released
#with keyboard.Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
#
# ...or, in a non-blocking fashion:
#listener = keyboard.Listener(
#    on_press=on_press,
#    on_release=on_release)
#listener.start()