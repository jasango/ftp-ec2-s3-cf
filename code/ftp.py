import os, random, string, random
from os import path

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

length = 8
chars = string.ascii_letters + string.digits
random.seed = (os.urandom(1024))

def generate_uuid():
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uuid_format = [8, 4, 4, 4, 12]
        for n in uuid_format:
            for i in range(0,n):
                random_string += str(random_str_seq[random.randint(0, len(random_str_seq) - 1)])
            if n != 12:
                random_string += '-'
        return random_string

def main():
    FTP_ROOT = '/home/ec2-user'
    USER = 'ftp'
    PASSWORD = ''    
    # password management
    if (path.exists("password.txt")):
        file = open("password.txt", "r")
        PASSWORD = file.read()
        file.close()
    else:     
        PASSWORD = generate_uuid()   
        # write password to file
        file = open("password.txt", "w")
        file.write(PASSWORD)
        file.close()
        
    HOST = '0.0.0.0'
    PORT = 21
    PASSIVE_PORTS = '3000-8000'
    ANONYMOUS = os.getenv('ANONYMOUS', False)
    user_dir = os.path.join(FTP_ROOT, USER)
    if not os.path.isdir(user_dir):
        os.mkdir(user_dir)
    authorizer = DummyAuthorizer()
    authorizer.add_user(USER, PASSWORD, user_dir, perm="elradfmw")
    if ANONYMOUS:
        authorizer.add_anonymous("/ftp_root/nobody")

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.permit_foreign_addresses = True

    passive_ports = map(int, PASSIVE_PORTS.split('-'))
    handler.passive_ports = range(passive_ports[0], passive_ports[1])
    # start service
    print('*************************************************')
    print('*                                               *')
    print('*            ftp-ec2-s3-lambda-cf               *')
    print('*                                               *')
    print('*************************************************')
    print('---------------')
    print("FTP User: ",USER)
    print("FTP Password: ",PASSWORD)
    server = FTPServer((HOST, PORT), handler)
    server.serve_forever()
    
if __name__ == '__main__':
    main()

