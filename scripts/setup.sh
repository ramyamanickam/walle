#To setup pyowm - weather api
#cd /home/pi/code/git
#git clone https://github.com/csparpa/pyowm.git
#cd pyowm
#python setup.py install

#To setup mysql-python-connector
#echo "Removing existing zip files"
#rm mysql-connector-python-2.0.4.zip
#rm -rf mysql-connector-python-2.0.4
#wget "http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df"
#sleep 5
#unzip mysql-connector-python-2.0.4.zip
#cd mysql-connector-python-2.0.4
#echo "About to Install mysql-connector"
#sudo python setup.py install

#Install lighttpd server
#sudo apt-get install lighttpd
#echo @About to backup the config file"
#sudo cp /etc/lighttpd/lighttpd.conf /etc/lighttpd/lighttpd.conf.backup
#sudo cp /home/pi/git/walle/walle/config/etc/lighttpd/lighttpd.conf /etc/lighttpd/

#Setup Streaming server
#sudo apt-get install libav-tools git python-setuptools python-pip python-picamera
#sudo pip install ws4py
git clone https://github.com/waveform80/pistreaming.git /home/pi/server/PiStreaming

