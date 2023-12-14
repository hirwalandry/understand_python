
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car has already started.")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == "stop":
        if not started:
            print("Car has already stopped.")
        else:
            started = False
            print("Car stopped.") 
    elif command == "help":
        print("""
start - start car
stop  - stop car
quit - quit game
        """)
    elif command == "quit":
        break
    else:
        print("I dont understand that...")