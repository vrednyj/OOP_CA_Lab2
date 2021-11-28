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
rsa_key = 'rsa_key_'


def exc_print_content(command):
    """
    :param command: str # Commands for Ubuntu
    :return: None
    """
    (stdin, stdout, stderr) = client.exec_command(command)
    log_file = open("ssh_connection.log", "a", encoding='utf-8')
    for line in stdout.readlines():
        print(line, end='')
        log_file.write('{0} - {1}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), line))
    log_file.close()


def run_that_all() -> None:
    """
    This function a list of commands to pass to exc_print_content() function.
    :return: None
    """
    list_of_command = ['sudo -S apt update',  #
                       'sudo -S apt install curl -y',  # -y is the key to do not ask for confirmation for installation
                       'curl --version',  # Checking if the curl is installed
                       'ls',
                       'cd Downloads && mkdir Lab && cd Lab && mkdir Lab1 && mkdir Lab2 && ls',
                       'tree',  # Get the folders in tree like view
                       'ls -l --time=atime'  # This is to check the last time when the files were accessed.
                       ]
    for command in list_of_command:
        exc_print_content(command)  # command to execute


if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(IP, username=USERNAME, password=PASSWORD)
    client.invoke_shell()
    run_that_all()
    client.close()
