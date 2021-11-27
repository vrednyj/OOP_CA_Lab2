#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VREDNYJ
#
# Created:     27.11.2021
# Copyright:   (c) VREDNYJ 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
""" #!/usr/bin/env python #include this shebang if running in a *nix environment """

''' Sockets code to carry out a port scan '''
''' Modified from:  '''

import socket
import subprocess
import sys
import csv
from datetime import datetime

dict_of_port_name = {} # This dictionary will keep the data from CSV file about Ethernet ports and service names.


def create_dictionary():
    '''
    This function to create a dictionary from CSV file. {port:service_name}

    :return: None
    '''
    try:
        file_name ='service-names-port-numbers.csv'
        csvfile = open(file_name,'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_of_port_name[row['Port Number']] = row['Service Name']
    except:
        print('The file {} could not be found. Please check. \nThis program may operate incorrectly'.format(file_name))
        input('Hit any key to continue.')

    csvfile.close()


def port_scan():
    '''
    This function to check if the ports are opened.
    :return: None
    '''
    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)

    # Ask for input
    try:
        remoteServer    = input("Enter a remote host to scan: ") # Will use "try:" to avoid using ip_validator. This allows to scan ports on remote and local hosts.
        remoteServerIP  = socket.gethostbyname(remoteServer)
    except:
        print('This program has terminated. Please check your entry.')
        sys.exit()


    # Print a nice banner with information on which host we are about to scan
    print ("-" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors
    #dict_of_port_name = {} #for debug
    try:
        #try 1, 1025 if you have time
        for port in range(18,24):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {0}: \tService name: {1:^20} Status: Opened".format( port, str(dict_of_port_name.get(str(port))).upper())) # Using .get method to avoid exception.
            else:
                print ("Port {0}: \tService name: {1:^20} Status: Closed".format( port, str(dict_of_port_name.get(str(port))).upper()))
            sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print ('Scanning Completed in: ', total)

if __name__ == "__main__":
    create_dictionary()
    port_scan()