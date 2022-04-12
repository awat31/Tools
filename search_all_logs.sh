#!/bin/bash

rm -rf ~/logtemp
mkdir ~/logtemp
cp /var/log/* ~/logtemp/
cd ~/logtemp
for file in $(ls .)
do
        if [[ $file == *.gz ]]
        then
                gzip -d  $file
        fi
done
for filecleaned in $(ls .)
do
        if grep -q $1 "$filecleaned"
        then
                printf "\n"
                echo "------------------------"
                echo $filecleaned
                echo "------------------------"
                cat $filecleaned | grep $1
        fi

done
