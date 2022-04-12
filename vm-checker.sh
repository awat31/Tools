#!/bin/bash
# Script to SSH into all machines and print the VMs on each machine
# Aaron Watkins

main(){

        for host in $(cat vms.txt);
        do
                ssh -o LogLevel=QUIET -t $host "$(typeset -f check); check"
        done
}

check(){
        echo "--------------------------------"
        hostname
        echo "--------------------------------"
        virsh list --all | awk '{ print $2 " | " $3}'
        echo "--------------------------------"
        exit

}

main
