import curses
import sys
import itertools

if len(sys.argv) != 2:
    sys.exit(1)

target_name = sys.argv[1]
stdscr = curses.initscr()

def main(stdscr):
    start = 0
    curses.curs_set(0)

    while True:
        stdscr.move(0,0)
        stdscr.clear()
        height, width = stdscr.getmaxyx()


        with open(target_name, "r") as target_file:
            current_line = 0
            for line in itertools.islice(target_file, start, start + height):
                if line[-1] == '\n':
                    useline = line[:-1]
                else:
                    useline = line

                stdscr.addnstr(current_line, 0, useline, width)
                current_line += 1

        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == ord('j'):
            start += 1
        elif c == ord('k'):
            start = max(start - 1, 0)

curses.wrapper(main)
