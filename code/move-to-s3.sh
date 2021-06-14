#!/bin/bash
now=$(date)
text="ejecucion $now"
echo $text >> ftp.log
FILES="/home/ec2-user/ftp/datos/*"
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  aws s3 cp "$f" s3://jasango-webcam
  sudo rm -f "$f"
done
#check service running
command="sudo ps -aux | grep -c 'sudo python -u ftp.py'"
result=$(eval "$command") 
if [ "$result" -eq 1 ]
then
   echo 'service not running'
   sudo chown ec2-user password.txt
   sudo '/home/ec2-user/ftp.sh' &  
fi	