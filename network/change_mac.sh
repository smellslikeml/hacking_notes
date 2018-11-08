# bash script to change MAC apparent
# address with macchanger
service network-manager stop; sleep 5 
ifconfig eth0 down
macchanger -b -a eth0; sleep 5 
ifconfig eth0 up; sleep 5
service network-manager start

