from subprocess import call


cmd1 = "sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster peer probe 20.20.4.22\""
call(cmd1, shell=True)

cmd2 = "sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster peer probe 20.20.4.23\""
call(cmd2, shell=True)

cmd3 = "sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume create nas replica 3 20.20.4.21:/nas 20.20.4.22:/nas 20.20.4.23:/nas force\""
call(cmd3, shell=True)

cmd4 = "sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume start nas\""
call(cmd4, shell=True)

cmd4 = "sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume info\""
call(cmd4, shell=True)


cmd5 = "sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume set nas network.ping-timeout 5\""
call(cmd5, shell=True)

cmd50 = "sudo lxc-attach --clear-env -n nas3 -- bash -c \"gluster volume set nas network.ping-timeout 5\""
call(cmd50, shell=True)

cmd51 = "sudo lxc-attach --clear-env -n nas2 -- bash -c \"gluster volume set nas network.ping-timeout 5\""
call(cmd51, shell=True)

cmd6 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"mkdir /mnt/nas\""
call(cmd6, shell=True)

cmd7 = "sudo lxc-attach --clear-env -n s1 -- bash -c \"mount -t glusterfs nas1:/nas /mnt/nas\""
call(cmd7, shell=True)

cmd8 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"mkdir /mnt/nas\""
call(cmd8, shell=True)

cmd9 = "sudo lxc-attach --clear-env -n s2 -- bash -c \"mount -t glusterfs nas1:/nas /mnt/nas\""
call(cmd9, shell=True)

cmd10 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"mkdir /mnt/nas\""
call(cmd10, shell=True)

cmd11 = "sudo lxc-attach --clear-env -n s3 -- bash -c \"mount -t glusterfs nas1:/nas /mnt/nas\""
call(cmd11, shell=True)
