import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "Hello world this is some text for this app!"
    current_text = []
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        stdscr.addstr(1, 0, ''.join(current_text))  # Show input on next line
        stdscr.refresh()
        key = stdscr.get_wch()  # Use get_wch to distinguish printable/control
        if isinstance(key, str):
            if ord(key) == 27:  # ESC key to exit
                break
            elif key in ('\b', '\x7f'):  # Backspace handling
                if current_text:
                    current_text.pop()
            elif len(current_text) < len(target_text):  # Only allow up to target_text length
                current_text.append(key)
        elif key == curses.KEY_BACKSPACE:
            if current_text:
                current_text.pop()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
