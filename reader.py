import socket
from ethernet_frame import EthernetFrame

def listen_for_frame(interface='eth0'):
    """Écoute l'interface spécifiée pour lire des trames Ethernet."""
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003)) as sock:
        sock.bind((interface, 0))
        print(f"Écoute sur {interface}...")

        while True:
            frame = sock.recv(65535)
            parsed_frame = EthernetFrame.parse_frame(frame)
            print("Trame reçue :")
            for key, value in parsed_frame.items():
                print(f"{key}: {value}")
