#!/bin/sh

set -x

PYTHONPATH=$PWD/lib:$PWD python -m unittest discover tests -v $*
