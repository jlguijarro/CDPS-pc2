from subprocess import call

cmd="scp installMariaDB.py root@bbdd:"
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n bbdd -- bash -c \"python /root/installMariaDB.py\""
call(cmd, shell=True)
