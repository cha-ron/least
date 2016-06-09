`least` is a minimal pager employing curses in python; it should be called
with a single file (to display) as its argument, and the following commands
can be used:

* `q`, to quit
* movement
    * one-line increments
        * `j`, to move one line down
        * `k`, to move one line up
    * one-page increments
        * `+`, down one page
        * `-`, up one page
    * to
        * `g`, top of file
        * `G`, bottom of file

To install, run `pip install [directory]`, or `pip install .` from within this
repo.
