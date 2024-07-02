#! /bin/bash

ls /var/log
ls -l /var/log
ls -a /etc
ls -lh /home

cd /var/log
cd ~
cd ..
cd -

echo "CREATION DES REPERTOIRES : "
mkdir cybersec
mkdir cybersec/{logs,reports,scripts}
echo "Répertoire cybersec : "
ls cybersec/
mkdir -p cybersec/reports/2024/january/week1
echo "Répertoire reports : "
ls cybersec/reports/2024/january

echo "CREATION DE FICHIERS : "
touch cybersec/readme.txt
touch cybersec/logs/log{1..3}.txt
touch cybersec/logs/log_$(date +%Y-%m-%d).txt
echo "Répertoire logs : "
ls cybersec/logs/

echo "MANIPULATION DE FICHIERS ET REPERTOIRES : "
cp cybersec/readme.txt cybersec/scripts
cp cybersec/logs/*.txt cybersec/reports/2024/january/week1/
echo "Dossier logs après mv : "
ls cybersec/logs/
echo "Dossier week1 : "
ls cybersec/reports/2024/january/week1/

echo "DEPLACER ET RENOMMER DES FICHIERS : "
mv cybersec/logs/log1.txt cybersec/scripts/script_log1.txt
mv cybersec/readme.txt cybersec/README.txt
echo "Dossier logs : "
ls cybersec/logs
echo "Readme : "
ls cybersec

echo "SUPPRESSION DE FICHIERS ET REPERTOIRES :"
rm cybersec/logs/log2.txt
echo "Suppression log2.txt"
ls cybersec/logs/
rm -r cybersec/reports/2024/january/week1/
echo "Suppression week1"
ls cybersec/reports/2024/january/
rm cybersec/logs/*.txt
echo "Suppression logs"
ls cybersec/logs