#!/usr/bin/env sh

flask db upgrade

uwsgi --socket 0.0.0.0:3031 --uid uwsgi --plugins python3 --protocol uwsgi --wsgi wsgi:app
