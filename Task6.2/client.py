import socket

# this is the client parameters
DNS_SERVER_IP = '127.0.0.1'
DNS_SERVER_PORT = 61
BUFFER_SIZE = 512

def create_udp_socket():
    """Creates a UDP socket."""
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_query(sock, query, server_ip, server_port):
    """Sends the DNS query to the server."""
    sock.sendto(query.encode(), (server_ip, server_port))

def receive_response(sock):
    """Receive response from the server."""
    data, _ = sock.recvfrom(BUFFER_SIZE)
    return data.decode()

def main():
    client_socket = create_udp_socket()

    while True:
        hostname = input("Enter hostname or alias name: ")
        query_type = input("Enter query type (A or CNAME): ")
        query = f"{hostname} {query_type}"

        send_query(client_socket, query, DNS_SERVER_IP, DNS_SERVER_PORT)
        response = receive_response(client_socket)

        print(f"Response from server: {response}")

        continue_query = input("Would you like to continue with another query? : ").strip().lower()
        if continue_query != 'yes':
            break

if __name__ == '__main__':
    main()
