from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 35*60
    eyessecs = 30*60
    exsecs = 45*60
    while True:
        if time() - init_water > watersecs:
            print(f"Water drinking time. Enter 'drank' to stop")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank water at")
        if time() - init_eyes > eyessecs:
            print(f"Eye exercise time. Enter 'doneeyes' to stop")
            musiconloop("eyes.mp3", "doneeyes")
            init_eyes = time()
            log_now("Eyes relaxed at")
        if time() - init_exercise > exsecs:
            print(f"Physical activity time. Enter 'donephy' to stop")
            musiconloop("exercise.mp3", "donephy")
            init_exercise = time()
            log_now("Physical activity done at")