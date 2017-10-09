import os
import signal

import trader

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

if __name__ == "__main__":
    display_menu()