#!/usr/bin/env python3
from datetime import datetime

def print_timestamp():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current timestamp: {formatted_time}")

if __name__ == "__main__":
    print_timestamp()