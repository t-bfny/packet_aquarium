from scapy.all import sniff, Packet
import json

# パケットをパースしてJSONっぽい形式にする関数
def packet_to_dict(pkt: Packet):
    return {
        "summary": pkt.summary(),
        "src": pkt[0].src if hasattr(pkt[0], 'src') else None,
        "dst": pkt[0].dst if hasattr(pkt[0], 'dst') else None,
        "protocol": pkt.name,
        "length": len(pkt)
    }

# キャプチャ関数
def capture_packets(count=5):
    print(f"Capturing {count} packets...")
    packets = sniff(count=count)
    parsed = [packet_to_dict(pkt) for pkt in packets]
    return parsed

if __name__ == "__main__":
    capture_packets()

