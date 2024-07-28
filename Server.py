import socket

def run_server():
    # Initialize a socket object
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set the server address and port
    server_host = '127.0.0.1'
    server_port = 12345
    
    # Bind the socket to the specified host and port
    s_socket.bind((server_host, server_port))
    
    # Start listening for incoming connections
    s_socket.listen(1)
    print(f"Server is running on port {server_port}")
    
    # Accept a connection from a client
    connection, address = s_socket.accept()
    print(f"Connection established with {address}")
    
    while True:
        # Receive a message from the client
        message = connection.recv(1024).decode('utf-8')
        if not message:
            break
        
        # Calculate the length of the received message
        char_count = len(message)
        
        # Convert the message to uppercase
        upper_message = message.upper()
        
        # Formulate the response with character count and uppercase message
        response = f"{char_count}\n{upper_message}"
        connection.sendall(response.encode('utf-8'))
    
    # Close the connection after communication ends
    connection.close()

if __name__ == '__main__':
    run_server()
