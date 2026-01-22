@echo off
set /p ticker="Enter Stock Ticker (e.g., RELIANCE): "
python main.py %ticker%
pause
