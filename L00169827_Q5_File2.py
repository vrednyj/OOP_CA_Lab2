# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VREDNYJ
#
# Created:     05.11.2021
# Copyright:   (c) VREDNYJ 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import time
import paramiko


USERNAME = 'l00169827'
PASSWORD = 'Pizdiuk123!'
IP = '192.168.85.130'
rsa_key='rsa_key_'

def exc_print_content(command):
    '''
    :param command: str # Commands for Ubuntu
    :return: None
    '''
    (stdin, stdout, stderr) = client.exec_command(command)
    log_file = open("ssh_connection.log", "a",encoding='utf-8')
    for line in stdout.readlines():
        print(line, end='')
        log_file.write('{0} - {1}'.format(time.strftime('%Y-%m-%d %H:%M:%S'),line))
    log_file.close


def run_that_all():
    '''
    This function a list of commands to pass to exc_print_content() function.
    :return: None
    '''
    command = 'sudo -S apt update'
    exc_print_content(command)  # command to execute
    command = 'sudo -S apt install curl -y'  # -y is the key to do not ask for confirmation for installation
    exc_print_content(command)
    command = 'curl --version'  # Checking if the curl is installed
    exc_print_content(command)
    command = 'ls'
    exc_print_content(command)
    command = 'cd Downloads && mkdir Lab && cd Lab && mkdir Lab1 && mkdir Lab2 && ls'  # To perform all
    # commands in a sequence withing one session.
    exc_print_content(command)  # No SU is required, thus False by default.
    command = 'tree'  # Get the folders in tree like view
    exc_print_content(command)
    command = 'ls -l --time=atime' # This is to check the last time when the files were accessed.
    exc_print_content(command)


if __name__ == '__main__':
    client = paramiko.SSHClient()
    #k = paramiko.RSAKey.from_private_key_file('rsa_key')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(IP, username=USERNAME,password=PASSWORD)
    #client.connect(IP, username=USERNAME, key_filename=k)
    client.invoke_shell()
    run_that_all()
    client.close()




