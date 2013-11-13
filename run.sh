#!/bin/bash

source ./venv/bin/activate
LD_LIBRARY_PATH=LD_LIBRARY_PATH:venv/lib/ python2 app.py
