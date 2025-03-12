#!/usr/bin/env python3

def main():
    try:
        num = int(input("16\n"))
        if num > 25:
            print("ข้อผิดพลาด")
        else:
            while num <= 25:
                print(f"ในลูป ตัวแปรของฉันคือ {num}")
                num += 1
    except ValueError:
        print("23")

if __name__ == "__main__":
    main()