def main():
    password = "Python is awesome"
    user_input = input("Enter the password:8523 ").strip()  
   
    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()