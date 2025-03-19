
## **📌 ScanItUp**
*A fast, stealthy, and optimized network scanner for cybersecurity professionals and penetration testers.*

![ScanItUp Banner](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

### **🚀 Features**
✅ Retrieves detailed device information (**IP, MAC, device name, connection time**)  
✅ Uses **CIDR/netmask** for accurate network range calculation  
✅ **TCP SYN scan** to bypass ICMP restrictions  
✅ **Reliable ARP scanning** using `arp-scan`  
✅ Optimized concurrency for **faster scans**  
✅ **Stealth mode** to avoid detection  
✅ **Error handling** for permissions & resource limits  

---

### **🛠 Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/c01d43am/scanitup.git
   cd scanitup
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scanner:
   ```bash
   python3 scanitup/scanner.py -t 192.168.1.0/24
   ```

---

### **📌 Usage**
```bash
python3 scanitup/scanner.py -t <target-network>
```
Example:
```bash
python3 scanitup/scanner.py -t 192.168.1.0/24 --stealth
```
🔹 Use `--help` for more options:
```bash
python3 scanitup/scanner.py --help
```

---

### **🖥 Example Output**
```
[+] Scanning 192.168.1.0/24...
-------------------------------------------
IP Address   MAC Address        Device Name       Connection Time
192.168.1.1  AA:BB:CC:DD:EE:FF  Router           5h 23m
192.168.1.10 11:22:33:44:55:66  Laptop           1h 12m
192.168.1.22 66:77:88:99:AA:BB  Smart TV         3h 45m
-------------------------------------------
[✔] Scan completed in 3.2 seconds.
```

---

### **🔧 Configuration & Advanced Options**
#### **Stealth Mode**
- Bypasses detection by reducing scan noise.
- Example:
  ```bash
  python3 scanitup/scanner.py -t 192.168.1.0/24 --stealth
  ```

#### **TCP SYN Scan (For ICMP-Restricted Networks)**
- Uses raw TCP packets for better stealth.
- Example:
  ```bash
  python3 scanitup/scanner.py -t 192.168.1.0/24 --tcp-syn
  ```

#### **ARP Scan for LAN Devices**
- Ensures better device detection.
- Example:
  ```bash
  python3 scanitup/scanner.py -t 192.168.1.0/24 --arp
  ```

---

### **💻 Contributing**
Feel free to contribute! Fork the repo, create a new branch, and submit a pull request.

---

### **📜 License**
**MIT License** – Free to use and modify. See `LICENSE` for details.

---

### **🔗 Connect with Me**
👤 **GitHub:** [@c01d43am](https://github.com/c01d43am)  
💬 **Twitter:** [@yourhandle](#)  
📧 **Email:** your.email@example.com  

