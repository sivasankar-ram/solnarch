#!/bin/bash
sudo dnf update -y
sudo dnf install postgresql15.x86_64 postgresql15-server python3-pip -y
sudo postgresql-setup --initdb
sudo sed -i 's/host    all             all             127.0.0.1\/32            ident/host    all             all             127.0.0.1\/32            md5/g' /var/lib/pgsql/data/pg_hba.conf
sudo systemctl restart postgresql
sudo systemctl enable postgresql
sudo dnf install git -y

echo "ALTER USER postgres with encrypted PASSWORD 'Kloudtom@123';" > /tmp/init.sql
echo "CREATE DATABASE kloudtom;" >> /tmp/init.sql
sudo -u postgres psql < /tmp/init.sql

git clone https://github.com/sivasankar-ram/solnarch.git /opt/solnarch

cd /opt/solnarch
git checkout polls
git pull origin polls
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:9000
