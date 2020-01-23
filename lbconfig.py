from subprocess import call



cmd1 = "sudo lxc-attach --clear-env -n lb -- bash -c \"apt-get update\""
call(cmd1, shell=True)

cmd2 = "sudo lxc-attach --clear-env -n lb -- bash -c \"apt-get install -y haproxy\""
call(cmd2, shell=True)

cmd3 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo 'frontend lb' >> /etc/haproxy/haproxy.cfg\""
call(cmd3, shell=True)

cmd4 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	bind *:80' >> /etc/haproxy/haproxy.cfg\""
call(cmd4, shell=True)

cmd5 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	mode http' >> /etc/haproxy/haproxy.cfg\""
call(cmd5, shell=True)

cmd5 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	default_backend webservers' >> /etc/haproxy/haproxy.cfg\""
call(cmd5, shell=True)

cmd6 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo 'backend webservers' >> /etc/haproxy/haproxy.cfg\""
call(cmd6, shell=True)

cmd7  ="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	mode http' >> /etc/haproxy/haproxy.cfg\""
call(cmd7, shell=True)

cmd8 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	balance roundrobin' >> /etc/haproxy/haproxy.cfg\""
call(cmd8, shell=True)

cmd9 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server s1 20.20.3.11:3000 check' >> /etc/haproxy/haproxy.cfg\""
call(cmd9, shell=True)

cmd10 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server s2 20.20.3.12:3000 check' >> /etc/haproxy/haproxy.cfg\""
call(cmd10, shell=True)

cmd11 = "sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server s3 20.20.3.13:3000 check' >> /etc/haproxy/haproxy.cfg\""
call(cmd11, shell=True)

cmd12 = "sudo lxc-attach --clear-env -n lb -- bash -c \"sudo service haproxy restart\""
call(cmd12, shell=True)
