# ftp-ec2-s3-cf

**EC2 that automatically move files received through FTP to S3** 


## Installation

CloudFormation template [Deploy now!](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?&templateURL=https://raw.githubusercontent.com/jasango/ftp-ec2-s3-cf/main/template.json)


## Usage

* IP / domain name: take note of the public IP address / DNS name of your EC2 instance
* Username: ftp
* Password: Watch your ftp service password at the end of you EC2 server User Data. If you would like to change your password log in to your server and change the password.txt file.


## ToDo

* Add the creation of an elastic IP address in the template.
