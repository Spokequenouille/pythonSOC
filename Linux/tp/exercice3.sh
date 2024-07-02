groupadd tpgroup

adduser tpuser 
usermod -a -G tpgroup tpuser

useradd -m tpuser2
usermod -a -G tpgroup tpuser2
sudo usermod -a -G sudo tpuser2

su tpuser
su tpuser2

mkdir test
touch fichier{1..2}.txt
chown tpuser2:tpgroup /home/tpuser/fichier1.txt
chmod 744 tpuser/fichier1.txt
chmod 777 -R test/ 
chown -R tpuser:tpgroup test/

usermod -m -d /home/tpuser-new tpuser
usermod --shell /bin/zsh tpuser
usermod -l newtpuser tpuser
groupadd newgroup
usermod -g newgroup newtpuser
passwd -l newtpuser
passwd -u newtpuser
groups newtpuser
id newtpuser 
deluser --remove-home newtpuser
groupdel tpgroup
