def play_with_arrays():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    print(original_array)
   
    transformed_set = {x + 2 for x in original_array}  # Using set comprehension to ensure unique values
    print(transformed_set)

if __name__ == "__main__":
    play_with_arrays()