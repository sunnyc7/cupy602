import os
import signal

from trader import generator

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

if __name__ == "__main__":
    display_menu()