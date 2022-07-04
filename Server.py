
# import socket programming library, shared message class and store
import socket, pickle
from shared.Message import Message
from store.RemoteMessageStore import RemoteMessageStore
 
# import thread module
from _thread import *
import threading
 
print_lock = threading.Lock()
store = RemoteMessageStore()
 
# thread function
def threaded(c):
    while True:
 
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
             
            # lock released on exit
            print_lock.release()
            break
 
        # decode the received object and store it
        message = pickle.loads(data)
        store.add_new_message(message)
        store.print_stored_messages()
 
        # send response to client
        response = "Hello " + message.sender
        c.send(response.encode('ascii'))
 
    # connection closed
    c.close()
 
 
def Main():
    host = ""
 
    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()