#!/bin/bash
if test $1
then
  enscript -p $1.ps $1.txt
  ps2pdf $1.ps $1.pdf
else
  echo "USE: $0 FILENAME.txt"
fi
