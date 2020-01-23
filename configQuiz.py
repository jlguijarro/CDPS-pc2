from subprocess import call

#s1
cmd0 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"apt-get update\""
call(cmd0, shell=True)

cmd1 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -\""
call(cmd1, shell=True)

cmd2 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"sudo apt install -y nodejs\""
call(cmd2, shell=True)

cmd3 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2020.git\""
call(cmd3, shell=True)

cmd4 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /root/quiz_2020; mkdir -p public/uploads; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; npm run-script migrate_cdps; npm run-script seed_cdps; ./node_modules/forever/bin/forever start ./bin/www\""
call(cmd4, shell=True)

cmd5 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"ln -s /mnt/nas /root/quiz_2020/public/uploads\""
call(cmd5, shell=True)

#s2
cmd6 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"apt-get update\""
call(cmd6, shell=True)

cmd7 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -\""
call(cmd7, shell=True)

cmd8 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"sudo apt install -y nodejs\""
call(cmd8, shell=True)

cmd9 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2020.git\""
call(cmd9, shell=True)

cmd10 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /root/quiz_2020; mkdir -p public/uploads; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www\""
call(cmd10, shell=True)

cmd11 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"ln -s /mnt/nas /root/quiz_2020/public/uploads\""
call(cmd11, shell=True)

#s3

cmd12 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"apt-get update\""
call(cmd12, shell=True)

cmd13 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -\""
call(cmd13, shell=True)

cmd14 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"sudo apt install -y nodejs\""
call(cmd14, shell=True)

cmd15 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2020.git\""
call(cmd15, shell=True)

cmd16 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /root/quiz_2020; mkdir -p public/uploads; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www\""
call(cmd16, shell=True)

cmd17 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"ln -s /mnt/nas /root/quiz_2020/public/uploads\""
call(cmd17, shell=True)


