# import serial
import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import time  # Import the sleep function from the time module
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)

# arduinoData = serial.Serial('com4', 9600)

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

# Function to encrypt the string
# according to the morse code chart


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


def led_on():
    GPIO.output(8, GPIO.HIGH)


def led_off():
    GPIO.output(8, GPIO.LOW)


def dot():
    led_on()
    time.sleep(0.1)
    led_off()
    time.sleep(0.1)
    


def dash():
    led_on()
    time.sleep(0.3)
    led_off()
    time.sleep(0.1)


def blank():
    led_off()
    time.sleep(0.1)

def end():
    led_off()
    time.sleep(1.2)
    
def cur():
    led_off()
    time.sleep(0.1)

time.sleep(5)
print("configured")


message = input()

result = encrypt(message.upper())

result = list(result)
result.pop(-1)
# result.append('.')
# result.append('-')

print(result)

time.sleep(.8)

for e in result:
    cur()
    if(e == '.'):
        dot()
    elif(e == '-'):
        dash()
    elif(e == ' '):
        blank()
    elif(e == 'p'):
        end()
GPIO.output(8, GPIO.HIGH)
print("done")