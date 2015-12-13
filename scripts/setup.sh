#To setup pyowm - weather api
#cd /home/pi/git
#git clone https://github.com/csparpa/pyowm.git
#cd pyowm
#python setup.py install

#To setup mysql-python-connector
echo "Removing existing zip files"
rm mysql-connector-python-2.0.4.zip
rm -rf mysql-connector-python-2.0.4
wget "http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df"
sleep 5
unzip mysql-connector-python-2.0.4.zip
cd mysql-connector-python-2.0.4
echo "About to Install mysql-connector"
sudo python setup.py install
