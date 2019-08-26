#!/bin/bash

[[ -d export ]] || mkdir export
cd ./json
for f in html pdf md
do
    resume export --format $f resume.$f
    mv resume.$f ../export/jayson-stemmler-resume.$f
done
cd ../
