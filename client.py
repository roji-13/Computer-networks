import socket

def run_client():
    # Initialize a socket object
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_host = '127.0.0.1'
    server_port = 12345
    
    # creates a connection to the server
    c_socket.connect((server_host, server_port))
    
    # Send a message to the server
    msg = "Hello SIT202"
    c_socket.sendall(msg.encode('utf-8'))
    
    # Receive the server's response
    response = c_socket.recv(1024).decode('utf-8')
    
    # Parse the response to separate character count and uppercase message
    char_count, upper_msg = response.split('\n')
    
    # Display the received data
    print(f"Character count: {char_count}")
    print(f"Uppercase message: {upper_msg}")
    
    # ends the connection
    c_socket.close()

if __name__ == '__main__':
    run_client()
