import curses
from curses import wrapper

class UI:
    def __init__(self):
        pass

    def start(self):
        print("HALOO UI")
        wrapper(self.view)

    def view(self, stdscr):
        stdscr.clear()
        stdscr.addstr(10, 10, "hello world")
        stdscr.refresh()
        stdscr.getch()

ui = UI()