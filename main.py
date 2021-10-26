from playsound import playsound
import os
import time

def findName():
    files = os.listdir('.')
    for f in files:
        if f.find('.m4a') != -1 or f.find('.mp3') != -1 or f.find('.mp3') != -1:
            name = f
    return name

print("Welcome to this stupid program.")
print("Make sure you have dragged the corresponding audio file into the hypnopaedia folder")
print("Make sure your computer will not sleep automatically. Google this if you don't know how.")
print("Type 'yes' to continue, anything else to quit.")

st = input().strip()
if st == "yes":
    print("Now we should decide how much time later (in your sleep) should the audio starts to repeat.")
    print("Do you want to enter time in seconds (type 's'), minutes (type 'm'), or hours (type'h')?")
    st1 = input().strip()
    print("Now enter the time in your chosen unit (either in integer or float):")
    tim = float(input().strip())
    if st1 == 'm':
        tim *= 60
    elif st1 == 'h':
        tim *= 3600
    print("Now enter how many repetitions you want (in integer):")
    repete = int(input().strip())
    soundtrack = findName()
    time.sleep(tim)
    for i in range(repete):
        playsound(soundtrack)
        #time.sleep(0.1)
else:
    print("bye")
