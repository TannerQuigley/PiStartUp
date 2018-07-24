from subprocess import call

#Install ansible
call("sudo apt-get update")
call("sudo apt-get install software-properties-common")
call("sudo apt-add-repository ppa:ansible/ansible")
call("sudo apt-get update")
call("sudo apt-get install ansible")

# git stuff
call("sudo apt-get install git")
call("git clone https://github.com/scottmotte/ansible-pi.git")

call("cd ansible-pi")
call("cp hosts.example hosts")
# call("cp wpa_supplicant.conf.example wpa_supplicant.conf")

call("ansible-playbook playbook.yml -i hosts --ask-pass --sudo -c paramiko")
