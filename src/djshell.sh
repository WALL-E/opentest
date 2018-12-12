#!/bin/bash

PWD=$(cd "$(dirname "$0")"; pwd)

python3.6 ${PWD}/manage.py shell
