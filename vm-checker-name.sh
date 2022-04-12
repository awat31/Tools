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
root@lab-admin:~/VM-Checker# cat vm-checker2.sh
#!/bin/bash
# Script to SSH into all machines and print the VMs on each machine
# Aaron Watkins

main(){
        ssh -o LogLevel=QUIET -t $1 "$(typeset -f check); check"
}
check(){
        echo "--------------------------------"
        hostname
        echo "--------------------------------"
        virsh list --all | awk '{ print $2 " | " $3}'
        echo "--------------------------------"
        exit

}
main $1
