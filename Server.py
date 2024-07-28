import socket

def run_server():
    # creates a socket object
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Sets  the server address and port
    server_host = '127.0.0.1'
    server_port = 12345
    
    # Bind the socket to the  host and port number above
    s_socket.bind((server_host, server_port))
    
    #  listens for incoming connections
    s_socket.listen(1)
    print(f"Server is running on port {server_port}")
    
    # accepts a connection from a client
    connection, address = s_socket.accept()
    print(f"Connection established with {address}")
    
    while True:
        # Receive a message from the client
        message = connection.recv(1024).decode('utf-8')
        if not message:
            break
        
        # Calculate the length of the received message, i.e the character numbers
        char_count = len(message)
        
        # makes the message have uppercase
        upper_message = message.upper()
        
        # creates the new response with character count and uppercase message
        response = f"{char_count}\n{upper_message}"
        connection.sendall(response.encode('utf-8'))
    
    # Closes the connection after communication ends
    connection.close()

if __name__ == '__main__':
    run_server()
