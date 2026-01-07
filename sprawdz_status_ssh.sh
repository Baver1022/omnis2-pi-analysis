#!/bin/bash
# Sprawdzanie statusu analizy Pi na Windows przez SSH

echo "=========================================="
echo "STATUS ANALIZY PI - 10B DIGITS"
echo "=========================================="
echo "Sprawdzanie: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

sshpass -p '1234' ssh -o StrictHostKeyChecking=no test@192.168.0.54 'powershell -ExecutionPolicy Bypass -File C:\Users\test\OMNIS2\sprawdz_status.ps1'

echo ""
echo "=========================================="
echo "Aby sprawdzic ponownie, uruchom:"
echo "  ./sprawdz_status_ssh.sh"
echo "=========================================="

