import socket

def send_frame(frame, interface='eth0'):
    """Envoie une trame Ethernet brute sur une interface réseau."""
    try:
        # Créer une socket brute pour envoyer des paquets Ethernet
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as sock:
            sock.bind((interface, 0))
            sock.send(frame)
            print(f"Trame envoyée sur {interface}")
    except PermissionError:
        print("Erreur : l'envoi de paquets bruts nécessite des privilèges administratifs.")
