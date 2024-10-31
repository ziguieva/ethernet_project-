import struct

class EthernetFrame:
    def __init__(self, dest_mac, src_mac, eth_type, payload):
        self.dest_mac = dest_mac
        self.src_mac = src_mac
        self.eth_type = eth_type
        self.payload = payload

    def create_frame(self):
        """Crée une trame Ethernet."""
        dest_mac_bytes = bytes.fromhex(self.dest_mac.replace(':', ''))
        src_mac_bytes = bytes.fromhex(self.src_mac.replace(':', ''))
        eth_type_bytes = struct.pack('!H', self.eth_type)

        return dest_mac_bytes + src_mac_bytes + eth_type_bytes + self.payload.encode()

    @staticmethod
    def parse_frame(frame):
        """Analyse une trame Ethernet et retourne ses composants."""
        dest_mac = ':'.join(format(b, '02x') for b in frame[:6])
        src_mac = ':'.join(format(b, '02x') for b in frame[6:12])
        eth_type = struct.unpack('!H', frame[12:14])[0]
        payload = frame[14:].decode()

        return {
            'dest_mac': dest_mac,
            'src_mac': src_mac,
            'eth_type': eth_type,
            'payload': payload
        }
