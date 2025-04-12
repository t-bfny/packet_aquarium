from flask import Flask, jsonify, render_template
from capture import capture_packets
import threading

app = Flask(__name__)

def capture_packets_thread():
    packet_info = capture_packets()  # パケットをキャプチャして返す
    return packet_info

@app.route("/")
def index():
  
    return render_template("index.html")


@app.route("/capture")
def capture():
    print("== /capture accessed ==")
    try:
        packet_info = capture_packets(count=5)
        print(f"Captured: {packet_info}")
        return jsonify(packet_info)
    except Exception as e:
        print(f"Error during capture: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
