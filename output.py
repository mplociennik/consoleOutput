#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import subprocess

try:
    out = subprocess.check_output("git status", shell=True, stderr=subprocess.STDOUT)
    print out
except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{0}' return with error (code {1}): {2}".format(e.cmd, e.returncode, e.output))