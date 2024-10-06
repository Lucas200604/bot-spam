import pyautogui
import time

mensaje = pyautogui.prompt(text='Que mensaje deseas spamear?', title='Ingresar mensaje' , default='')

time.sleep(5)

while True:
    time.sleep(0.2)
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')
