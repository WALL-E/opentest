#!/bin/bash

role=`id -u`
if test $role -ne 0
then
    echo "Operation not permitted"
    exit 1
fi

yum install -y mariadb-server mariadb-devel mariadb

systemctl start mariadb
systemctl enable mariadb

firewall-cmd --permanent --add-service mysql > /dev/null
systemctl restart firewalld.service > /dev/null

echo ""
echo "Please run 'mysql_secure_installation'"
echo ""
