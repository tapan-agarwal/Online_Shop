#!/bin/bash

ARGS=""

ARGS="$ARGS --bind 0.0.0.0:8080"

exec gunicorn $ARGS wsgi:app