# Simple Packet Sniffer and Analyzer

This is a simple packet sniffer and analyzer written in Python using the Scapy library. It captures network packets and prints a summary of each packet to the console.

## Requirements

- Python 3.x
- Scapy library

## Installation

1. **Make sure you have Python installed on your system.** You can download it from [python.org](https://www.python.org/downloads/).

2. **To avoid the "externally managed environment" error while installing Scapy, you can either:**

   ### Option 1: Use a Virtual Environment
   - Create a virtual environment:
     ```bash
     python -m venv myenv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       myenv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source myenv/bin/activate
       ```
   - Install Scapy in the virtual environment:
     ```bash
     pip install scapy
     ```

   ### Option 2: Use the `--break-system-packages` Option
   - If you want to install Scapy globally, use:
     ```bash
     pip install scapy --break-system-packages
     ```

   ### Option 3: Install from a Specific Package Source
   - Ensure your pip is up-to-date:
     ```bash
     pip install --upgrade pip
     ```
   - Then install Scapy:
     ```bash
     pip install scapy -i https://pypi.org/simple
     ```

## Usage

1. Save the code above to a file named `packet_sniffer.py`.

2. Open a terminal and navigate to the directory where `packet_sniffer.py` is located.

3. Run the packet sniffer script with superuser privileges (required for capturing packets):
   ```bash
   sudo python packet_sniffer.py
4. The packet sniffer will start capturing packets. You will see a summary of each packet printed to the console.

5. To stop the packet sniffer, press Ctrl + C.

Notes

    This packet sniffer captures all packets on the network interface. Make sure you have permission to capture packets on the network you are monitoring.
    You can modify the packet_callback function to analyze packets further or log them to a file instead of just printing to the console.

License

This project is open-source and available under the MIT License.
