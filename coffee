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
python ~/coffee_tracker/upload_coffee.py
popd
files=(./gifs/*.gif)
gif="${files[RANDOM % ${#files[@]}]}"
imgcat $gif
