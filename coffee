#!/bin/sh

pushd ~/Dropbox/PFUMA/p-flock.github.io


if [ -n "$1" ]
then
  if [ -n "$2" ]
  then
    python ~/coffee_tracker/record_coffee.py --format=$1 --mg=$2
  else
    echo "Bad usage. coffee <fmt> <mg>"
  fi
else
  python ~/coffee_tracker/record_coffee.py
fi
vim -u NONE -s ~/coffee_tracker/format.vim coffeelog.json
git add coffeelog.json
git add coffeelog.js
if [ -n "$1" ]
then
    git commit -m "Drank $1"
else
    git commit -m "Drank Coffee"
fi
git push
popd
