import curses
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(prog='least',
            description="If `less` is more than `more`, `least` is less than "
                        "`less`: it's a minimal paging utility.")
parser.add_argument("file", help="the file to page through")
args = parser.parse_args()

target_name = args.file
stdscr = curses.initscr()

def main(stdscr):
    curses.use_default_colors()
    start = 0
    curses.curs_set(0)

    with open(target_name, "r") as target_file:
        file_length = sum(1 for line in target_file)

    while True:
        stdscr.move(0,0)
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        max_line = max(file_length - height, 0)

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
            start = min(start + 1, max_line)
        elif c == ord('k'):
            start = max(start - 1, 0)
        elif c == ord('g'):
            start = 0
        elif c == ord('G'):
            start = max_line
        elif c == ord('+'):
            start = min(start + height, max_line)
        elif c == ord('-'):
            start = max(start - height, 0)

curses.wrapper(main)
