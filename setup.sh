#!/bin/bash
echo "[*] Cloning configuration files..."
mkdir -p configs/splunk
mkdir -p logs/suricata

echo "[*] Setting executable permissions..."
chmod +x main.py

echo "[*] Setup complete. Run the lab with: python3 main.py"
