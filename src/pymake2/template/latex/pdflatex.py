#!/usr/bin/env python

"""
Template make script for pdflatex.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import time

from pymake2 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Default configuration.
DEFAULT_CONF = { 'bindir'  : 'bin',
                 'flags'   : [ '-file-line-error', '-halt-on-error' ],
                 'srcdir'  : 'src',
                 'srcfile' : 'main.tex' }

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(conf=DEFAULT_CONF)
def clean(conf):
    """
    Cleans the build by deleting the bin directory and all its contents.
    """

    delete_dir(conf.bindir)

@target(conf=DEFAULT_CONF)
def compile(conf):
    """
    Compiles the executable program from its sources in the source directory.
    """

    create_dir(conf.bindir)

    bindir = os.path.abspath(conf.bindir)
    srcdir = os.path.abspath(conf.srcdir)

    flags      = conf.flags
    jobname    = [ '-jobname'         , conf.name                       ]
    output_dir = [ '-output-directory', os.path.relpath(bindir, srcdir) ]
    srcfile    = conf.srcfile

    cwd = os.getcwd()

    os.chdir(srcdir)
    run_program('pdflatex', flags + jobname + output_dir + [srcfile])
    os.chdir(cwd)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    pymake2()
