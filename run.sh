#!/usr/bin/env bash

color()(set -o pipefail;"$@" 2> >(sed $'s,.*,\e[31m&\e[m,'>&2))
color gunicorn --timeout 600 --config gunicorn.py --pid gunicorn.pid app:app
