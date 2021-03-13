# Programmed by Rishav Kumar
# all copyright reserved to lazy_robo_lab, lazyrobot, lazyrobot.project

# Simple program to add a server after you have 
# Created your pickle file
# Could create a file to delete or modify servers as well

# Enter the value of server you added in main.py and this will add the data and value in your servers.pickle that read the history


import pickle
from main import Server

servers = pickle.load( open( "servers.pickle", "rb" ) )

print("Add your new server to the servers.pickle")
print("........................................")
print("..........................")
print("..................")
print("..........")


servername = input("Enter server name")
port = int(input("Enter a port number as integer"))
connection = input("Enter a type ping/plain/ssl")
priority = input("Enter priority high/low")
secure = input("Enter secutiy prefrence yes/no")

# Here making the list after getting the value from the user of this system/program
new_server = Server(servername, port, connection, priority, secure)
# Here append the new seerver in the older list of server and start recording logs/history
servers.append(new_server)

pickle.dump(servers, open("servers.pickle", "wb" ))