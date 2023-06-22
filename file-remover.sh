# Bash file to find and delete a given file within a system

#file=$1

#hash=$(md5sum $file)
#hash=$(echo $hash | awk '{print $1}')
hash=$1

echo 'Target is' $1 #'with hash' $hash
echo '-------------------------------'

for i in $(find /home -type f -exec md5sum "{}" + | awk '{ print $1 ":" $2 }');
do
        targethash=$(echo "$i" | awk -F ":" '{print $1}')
        targetfile=$(echo "$i" | awk -F ":" '{print $2}')

        if [ $targethash == $hash ]
        then

                echo 'Target Found! File location' $HOSTNAME $targetfile
                echo 'Removing File'
                rm -rf $targetfile
                echo 'File Removed'
        fi
done
