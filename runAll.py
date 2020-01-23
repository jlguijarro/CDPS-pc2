
from subprocess import call

from subprocess import call

cmd="scp fw.fw root@fw:"
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n bbdd -- bash -c \"chmod 777 ./root/fw.fw\""
call(cmd, shell=True)


cmd="sudo lxc-attach --clear-env -n fw -- bash -c \"./root/fw.fw\""
call(cmd, shell=True)


cmd="scp installMariaDB.py root@bbdd:"
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n bbdd -- bash -c \"python /root/installMariaDB.py\""
call(cmd, shell=True)

cmd = "python ./glusters.py"
call(cmd, shell=True)

cmd = "python ./configQuiz.py"
call(cmd, shell=True)

cmd = "python ./lbconfig.py"
call(cmd, shell=True)

