#!/bin/sh

pushd ~/Dropbox/PFUMA/p-flock.github.io
python ~/coffee_tracker/record_coffee.py
vim -u NONE -s ~/coffee_tracker/format.vim coffeelog.json
popd
