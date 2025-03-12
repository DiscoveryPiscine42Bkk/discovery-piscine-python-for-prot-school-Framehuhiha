def main():
    try:
       
        num1_input = input("Enter the first number (default is 3):5 ")
        num2_input = input("Enter the second number (default is 5):9 ")
       
       
        if num1_input == "":
            num1 = 3
        else:
            num1 = float(num1_input)
       
        if num2_input == "":
            num2 = 5
        else:
            num2 = float(num2_input)
       
        result = num1 * num2
       
       
        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")
        else:
            print("The result is zero.")
       
        print(f"Multiplication result: {result}")
   
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()