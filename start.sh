#!/bin/bash

clear
echo -e "\033[1;31m"
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║ 🚫  \033[1;97m\033[41m ALERT \033[0m\033[1;31m  This tool is NOT FREE to use! 🔐                    ║"
echo "║                                                                ║"
echo "║ 🔔  You must SUBSCRIBE to our YouTube channel first:           ║"
echo "║      \033[1;36mhttps://youtube.com/@hackers_colony_tech\033[1;31m             ║"
echo "║                                                                ║"
echo "║ ⏳  Redirecting in 8 seconds...                                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo -e "\033[0m"

sleep 8

# Open YouTube link silently
am start https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya > /dev/null 2>&1

echo -e "\n\033[1;32m✅ Please subscribe and then press Enter to continue...\033[0m"
read

# Launch the actual tool
python main.py
