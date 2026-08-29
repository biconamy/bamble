# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MiniCRM
import os, sys

ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
    'bright_magenta': '\033[95m',
    'bright_cyan': '\033[96m',
    'bright_white': '\033[97m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
}

def colorize(text, code):
    return f'{ANSI.get(code, text)}{text}{ANSI["reset"]}'

def set_enabled(enable):
    global ANSI
    ANSI = {} if enable else None

def print_colored(text, code, end='\n', file=None):
    if ANSI:
        print(colorize(text, code), end=end, file=file)
    else:
        print(text, end=end, file=file)
