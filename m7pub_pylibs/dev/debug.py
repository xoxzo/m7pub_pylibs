#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2009, MARIMORE Inc Tokyo, Japan.
# Contributed by 
#       Iqbal Abdullah <iqbal@marimore.co.jp>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
#   *   Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#   *   Redistributions in binary form must reproduce the above copyright notice, 
#       this list of conditions and the following disclaimer in the documentation 
#       and/or other materials provided with the distribution.
#   *   Neither the name of the MARIMORE Inc nor the names of its contributors 
#       may be used to endorse or promote products derived from this software 
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Commonly used utilities during development
"""

from __future__ import absolute_import

import datetime, tempfile

def log(str, fn="mamodebug.log"):
    """
    Writes *str* to a file called 'mamodebug.log' by default.
    The log file will be placed in the directory returned by
    tempfile.gettempdir(), which is usually the default directory for tempfiles
    on your system.

    The function will append the time and date to *str*, i.e:
    
    .. note:: [2010-10-24 13:31:10] Test string

    """

    now = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    dir = tempfile.gettempdir()

    fd = open("%s/%s" % (dir, fn), 'a+')
    fd.write("[%s] %s\n" % (now, str))
    fd.close()


def logger(str, fn):
    """
    Writes *str* to the file *fn*. 

    The function will append the time and date to *str*, i.e:
    
    .. note:: [2010-10-24 13:31:10] Test string

    """

    now = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")

    fd = open("%s" % (fn), 'a+')
    fd.write("[%s] %s\n" % (now, str))
    fd.close()


if __name__ == '__main__':

    log("Hello World! 漢次テストあいうえお")
