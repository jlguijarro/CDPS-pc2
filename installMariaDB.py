from subprocess import call

cmd1 = "apt update"
call(cmd1, shell=True)

cmd2 = "apt -y install mariadb-server"
call(cmd2, shell=True)

cmd3 = "sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf"
call(cmd3, shell=True)

cmd4 = "systemctl restart mysql"
call(cmd4, shell=True)

cmd5 = "mysqladmin -u root password xxxx"
call(cmd5, shell=True)

cmd6 = "mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\""
call(cmd6, shell=True)

cmd7 = "mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\""
call(cmd7, shell=True)

cmd8 = "mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\""
call(cmd8, shell=True)

cmd9 = "mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\""
call(cmd9, shell=True)

cmd10 = "mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\""
call(cmd10, shell=True)