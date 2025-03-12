import sys

def main():
    num_params = len(sys.argv) - 1  # หัก 1 ออก เพราะ sys.argv[0] คือชื่อไฟล์
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()