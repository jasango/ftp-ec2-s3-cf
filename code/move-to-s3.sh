#!/bin/bash
now=$(date)
text="ejecucion $now"
echo $text >> ftp.log
for folder in /home/ec2-user/ftp/* ; do
    echo "$folder"
    SUBFOLDERS="$folder/*"
    for subfolder in $SUBFOLDERS
    do
      echo "Processing $subfolder subfolder..."
      sufix="${subfolder:19}"
      aws s3 sync "$subfolder" s3://jasango-webcam/$sufix --storage-class STANDARD_IA
      sudo rm -rf "$subfolder"
    done
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