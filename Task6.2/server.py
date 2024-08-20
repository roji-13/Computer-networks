import socket

# this is the server parameters
DNS_SERVER_IP = '127.0.0.1'
DNS_SERVER_PORT = 61
BUFFER_SIZE = 512

# Initialize DNS records (A and CNAME)
dns_records = {
    'roji.com': {'type': 'A', 'value': '192.168.1.1'},
    'coraline.com': {'type': 'CNAME', 'value': 'roji.com'}
}

def create_udp_socket():
    """Create a UDP socket."""
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def bind_socket(sock, ip, port):
    """Bind the socket to the IP address and port."""
    sock.bind((ip, port))

def parse_dns_query(data):
    """Parse the DNS query to extract hostname and type."""
    hostname = data.decode().split(' ')[0]
    query_type = data.decode().split(' ')[1]
    return {'hostname': hostname, 'type': query_type}

def handle_a_record(hostname):
    """Handle A record queries."""
    if hostname in dns_records and dns_records[hostname]['type'] == 'A':
        return {'type': 'A', 'value': dns_records[hostname]['value']}
    return generate_error_response()

def handle_cname_record(hostname):
    """Handle CNAME record queries."""
    if hostname in dns_records and dns_records[hostname]['type'] == 'CNAME':
        cname_target = dns_records[hostname]['value']
        if cname_target in dns_records and dns_records[cname_target]['type'] == 'A':
            return {'type': 'CNAME', 'value': f"{hostname} -> {cname_target} -> {dns_records[cname_target]['value']}"}
    return generate_error_response()

def generate_error_response():
    return {'type': 'ERROR', 'value': 'Host not found'}

def generate_dns_response(response, query):
    """Makes a DNS response message."""
    if response['type'] == 'A':
        return f"A {response['value']}"
    elif response['type'] == 'CNAME':
        return f"CNAME {response['value']}"
    elif response['type'] == 'ERROR':
        return "ERROR Host not found"
    return None

def main():
    server_socket = create_udp_socket()
    bind_socket(server_socket, DNS_SERVER_IP, DNS_SERVER_PORT)
    print("DNS Server is running...")

    while True:
        data, client_address = server_socket.recvfrom(BUFFER_SIZE)
        query = parse_dns_query(data)
        hostname = query['hostname']
        query_type = query['type']

        if query_type == 'A':
            response = handle_a_record(hostname)
        elif query_type == 'CNAME':
            response = handle_cname_record(hostname)
        else:
            response = generate_error_response()

        # Pass both response and query to generate_dns_response
        response_message = generate_dns_response(response, query)
        server_socket.sendto(response_message.encode(), client_address)


if __name__ == '__main__':
    main()
