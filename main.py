from ethernet_frame import EthernetFrame
from sender import send_frame
from reader import listen_for_frame
import threading

def main():
    # Créer une trame Ethernet
    frame = EthernetFrame(
        dest_mac="ff:ff:ff:ff:ff:ff",  # Adresse de diffusion
        src_mac="12:34:56:78:9a:bc",   # Adresse MAC source
        eth_type=0x0800,               # Type de protocole (IPv4)
        payload="Hello, Ethernet!"
    )

    created_frame = frame.create_frame()

    # Lancer l'écoute sur un autre thread
    listen_thread = threading.Thread(target=listen_for_frame, args=('eth0',), daemon=True)
    listen_thread.start()

    # Envoyer la trame après un court délai
    send_frame(created_frame, 'eth0')

if __name__ == "__main__":
    main()
