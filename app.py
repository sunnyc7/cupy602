import os
import signal

from trader import generator

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

if __name__ == "__main__":
    #generator.display_menu()
    display_menu()