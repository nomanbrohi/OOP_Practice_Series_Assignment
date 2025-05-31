class Logger():
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")

log = Logger()

del log
