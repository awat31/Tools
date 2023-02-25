#!/bin/bash
# Script to show the total usage of CPU and Memory resource on all VMs


totalmem=0
totalcpu=0
allcpu=$( lscpu | grep '^CPU(s):.*' | awk '{ print $2 }' )
allram=$( free -h -t | grep Total: | awk '{ print $2 }' )

echo " VM | CPU: | RAM: "
echo "__________________"
for line in $(virsh list --all | awk '{ print $2 }' )
do
        if [ $line == "Name" ]
        then
                continue
        else
                cpuused=$(virsh vcpucount $line --maximum)

                ramused=$(virsh dumpxml $line | grep currentMemory | cut -d '>' -f2 | cut -d '<' -f1)
                ramused=$(( $ramused / 1024 ))
                ramused=$(( $ramused / 1024 ))

                echo "$line | CPU: $cpuused | RAM: $ramused GB |"

                totalcpu=$(( $totalcpu + $cpuused ))
                totalmem=$(( $totalmem + $ramused ))

        fi
done
echo "-----------------------------------"
echo "Total CPU Used: $totalcpu / $allcpu"
echo "Total RAM Used: $totalmem Gi / $allram"
