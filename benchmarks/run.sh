#!/bin/bash

DIR=$(dirname $(readlink -f $0))

GLOBAL_PYTHON=python
MY_PYTHON=$(dirname $DIR)/python

echo "Running counter.py on regular Python version"
$GLOBAL_PYTHON $DIR/counter.py

echo "Running counter.py on changed Python version"
$MY_PYTHON $DIR/counter.py

echo "Running pi.py on regular Python version"
$GLOBAL_PYTHON $DIR/pi.py

echo "Running pi.py on changed Python version"
$MY_PYTHON $DIR/pi.py

