#!/bin/bash
# This script takes a VM name as an arguement and checks through all the hosts in hosts.txt to see if that VM is there.
# To add a new host to the script, add it to the hosts.txt file in this directory
# Run script alone
# Aaron Watkins

main(){
	for host in $(cat hosts.txt);
	do
		ssh -o LogLevel=QUIET -t $host "$(typeset -f check); check $1"
	done
}

check(){
	touch virsh.tmp
	virsh list --all > virsh.tmp
	if grep -q "$1" "virsh.tmp"
	then
		machine=$(hostname)
		echo "-------------------"
		echo "VM Found!"
		printf "\n"
		echo "Host: $machine"
		printf "Full VM Name: "
		cat virsh.tmp | grep $1 | awk '{ print $2}'
		printf "VM State: "
		cat virsh.tmp | grep $1 | awk '{ print $3 " "$4 }'
		echo "-------------------"
	fi
	rm virsh.tmp
}

main $1
