#!/bin/bash

# System information script
# Displays basic system information

echo "====== System Information ======"
echo ""
echo "Hostname: $(hostname)"
echo "OS: $(uname -s)"
echo "Kernel: $(uname -r)"
echo "Architecture: $(uname -m)"
echo ""
echo "====== Disk Usage ======"
df -h | head -n 2
echo ""
echo "====== Memory Usage ======"
free -h 2>/dev/null || echo "free command not available"
echo ""
echo "====== Uptime ======"
uptime
