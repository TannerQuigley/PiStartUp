from subprocess import call,check_call
import os

#Install ansible
call("(sudo apt-get update)", shell=True)
call("(sudo apt-get install software-properties-common)", shell=True)
call("(sudo apt-add-repository ppa:ansible/ansible)", shell=True)
call("(sudo apt-get update)", shell=True)
call("(sudo apt-get install ansible)", shell=True)

# git stuff
# call("sudo apt-get install git")
call("(git clone https://github.com/scottmotte/ansible-pi.git)", shell=True)

call("(cd ~/ansible-pi)", shell=True)
call("(cp hosts.example hosts)", shell=True)
# call("cp wpa_supplicant.conf.example wpa_supplicant.conf")

call("(ansible-playbook playbook.yml -i hosts --ask-pass --sudo -c paramiko)", shell=True)
