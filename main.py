# Programmed by Rishav Kumar
# all copyright reserved to lazy_robo_lab, lazyrobot, lazyrobot.project

# This will help begineer to learn nodes by nodes

import socket
import ssl
from datetime import datetime
import pickle

import subprocess
import platform

# use for make a gmail alert
# # import email alert from gmail.py
# from gmail import email_alert


# create class to use in other plogram as well

class Server():
    def __init__(self, name, port, connection, priority, secure):
        self.name = name
        self.port = port
        self.connection = connection.lower()
        self.priority = priority.lower()
        self.secure = secure

# for make a history of all the monetring

        self.history = []
# for alert
        self.alerty = False

# create a function who chaeck and take care of function working
    def check_connection(self):
# about connection and assuming connection failed
        msg = ""
        success = False
        now = datetime.now()

        try:
            if self.connection == "plain":
                socket.create_connection((self.name, self.port), timeout=10)
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False


            elif self.connection == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False
            else:
# if above doesn't work then self ping and desplay message that port is up/open and connection stablished and if not then show alert ao send on mail
                if self.ping():
                    msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                    success = True
                    self.alert = False
# display message when server timeout
        except socket.timeout:
            msg = f"server: {self.name} you failed, timeout. On port {self.port}"
# display message when server refuse to connect show error
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server: {self.name} {e}"
# display when server does not connect and show message
        except Exception as e:
            msg = f"No clue??What Happened: {e}"



# this section is for email alert
# # here we send the alert to the email if any server not active, this check the connection and alert already sended to me/owner or not then send it if False
#         if success == False and self.alert == False:
# # send Alert
#             self.alert = True
#             email_alert(self.name,f"{msg}\n{now}","lazyrobot.project@gmail.com")



        
# seprate function to make a call to history

        self.create_history(msg,success,now)

    def create_history(self, msg, success, now):
# maximum history createdd
        history_max = 100
# call/reach my previous history list and append tuple as meaage, success and current datetime
        self.history.append((msg,success,now))

# if history cross the maximum 100 then 
        while len(self.history) > history_max:
# it pop up the oldest item in history (only max to 100 history)
            self.history.pop(0)        




# for ping self it return True if connection get true and False if connection not stablish
    def ping(self):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', self.name ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False
            



if __name__ == "__main__":
# make a pickle file to save the result/history
    try:
        servers = pickle.load(open("servers.pickle","rb"))
    except:
# now make a server list ti will depends on you
        servers = [
            Server("google.com", 80, "plain", "high", "yes"),
            Server("linkedin.com", 80, "plain", "high", "yes"),
            Server("smtp.gmail.com", 465, "ssl", "high", "yes"),
            Server("rdxcreationx.tech", 80, "plain", "high", "yes"),
            Server("192.168.43.127", 80, "ping", "high", "yes"),
            Server("yahoo.com", 80, "plain", "high", "yes"),
            Server("microsoft.com", 80, "plain", "high", "yes"),
            Server("python.org", 80, "plain", "high", "yes")
        ]

# after this we have to check server connection in seerver list with print history (privous scan/server monitor)
    for server in servers:
        server.check_connection()
        print(len(server.history))
        print(server.history[-1])

# save our data to picke file
    pickle.dump(servers, open("servers.pickle", "wb"))