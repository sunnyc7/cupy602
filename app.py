import os
import signal

import trader as trad

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

if __name__ == "__main__":
    trad.generator.display_menu()