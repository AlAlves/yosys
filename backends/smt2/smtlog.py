#
# yosys -- Yosys Open SYnthesis Suite
#
# Copyright (C) 2012  Clifford Wolf <clifford@clifford.at>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import sys

class SmtLog:
    def __init__(self):
        self.filename = "log"
        self.ext = ".smtlog"
        self.prefix = "pre_"

        self.show_err = True
        self.write_allowed = False

        self.depth = 0
        self.refine = 0

        self.logfile = None

    # GETTERS / SETTERS
    def set_filename(self, filename="log"):
        if(filename != ""):
            self.filename = filename
    
    def set_depth(self, depth=0):
        self.depth = depth

    def set_refine(self, refine=0):
        self.refine = refine
    
    def toggle_log(self):
        self.write_allowed = not self.write_allowed
    
    def toggle_on_log(self):
        self.write_allowed = True

    def toggle_off_log(self):
        self.write_allowed = False

    # -----------------

    # Open <logfile> if not already open and set <filename> if given
    def open_file(self, filename=""):
        if(self.logfile == None or self.logfile.closed):
            self.set_filename(filename)
            self.logfile = open(self.filename, "w")
        elif(self.show_err):
            sys.stderr.write("Can't open file {}".format(filename))
    
    # Closes <logfile> and set <logfile> to None
    def close_file(self):
        if(self.logfile != None):
            if(not self.logfile.closed):
                self.logfile.close()
            self.logfile = None
    
    # Write a text in <logfile> if it is open
    def write_log(self, text):
        if(self.logfile != None and not self.logfile.closed):
            self.logfile.write(text)
        elif(self.show_err):
            sys.stderr.write("Can't write line:\n{}in file {}".format(text, self.filename))
    
    # Write a line in <logfile> if it is open
    def write_line(self, text):
        if(self.write_allowed):
            if(not text.endswith("\n")):
                text = text+"\n"
            self.write_log(text)

    
    def show_depth(self, depth=-1):
        if(depth != -1):
            self.set_depth(depth)
        self.write_line("\n=== \tDepth \t{} \t===".format(self.depth))
