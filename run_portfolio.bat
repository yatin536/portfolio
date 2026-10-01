@echo off
title Yatin Kumar Singh - Portfolio Server
cd /d "%~dp0"
echo ===================================================
echo Starting Yatin's Portfolio on http://localhost:8080
echo ===================================================
start http://localhost:8080
python server.py 8080
pause
