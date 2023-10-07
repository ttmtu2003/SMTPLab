import base64
from socket import *
from pip._vendor.distlib.compat import raw_input

msg = "\r\nI love computer networks!\r\n"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g., AOL mail server) and call it mailserver
mailServer = "smtp.aol.com"
mailPort = 587
serverPort = (mailServer, mailPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverPort)

recv = clientSocket.recv(1024)
print("Message after connection request:", recv.decode())

if recv[:3] != '220':
    print('220 reply not received from server.\n')

# Send HELO command and print server response.
helloCommand = 'HELO Alice\r\n'
clientSocket.send(helloCommand.encode())
recv1 = clientSocket.recv(1024)
print("Send HELO command and print server response:", recv1.decode())

if recv1[:3] != '250':
    print('250 reply not received from server.\n')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: ttmtu2003@gmail.com\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command:", recv2.decode())

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: ttmtu03@gmail.com\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print("After RCPT TO command:", recv3.decode())

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print("After DATA command:", recv4.decode())

# Send message data.
subject = "Subject: SMTP mail client testing\r\n"
clientSocket.send(subject.encode())

# User input for message body
message = raw_input("Enter message here:\r\n") + '\r\n'

# Send message and end with a single period.
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())

recv5 = clientSocket.recv(1024)
print("Response after sending message body:", recv5.decode())

# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024)
print(recv6.decode())
print(quitCommand)

clientSocket.close()
