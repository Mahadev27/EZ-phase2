import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Timer completed!")

def reset():
    global paused
    global time_left

    paused = False
    time_left = start_time
    print("Timer reset to {} seconds".format(time_left))

def stop():
    global paused
    global time_left

    paused = False
    time_left = 0
    print("Timer stopped")

def pause():
    global paused

    paused = True
    print("Timer paused")

def resume():
    global paused

    paused = False
    print("Timer resumed")

start_time =int(input("Enter the time in seconds:"))
paused = False
time_left = start_time

while True:
    choice = input("\n       Press 'r' to reset, 's' to stop, 'p' to pause, or 'res' to resume: ")

    if choice == 'r':
        start_time = int(input("Enter the number of seconds: "))
        reset(start_time)
    elif choice == 's':
        stop()
        break
    elif choice == 'p':
        pause()
    elif choice == 'res':
        resume()
    else:
        print("Enter right option")

