with open("output.txt", "r") as f:
    # Read the contents of the file and split them by |
    contents = f.read().strip().split(" | ")

    results = []
    for sum_str in contents:
        # Evaluate each sum and append the result to the results list
        sum_eval = eval(sum_str)
        results.append(sum_eval)

    # Join the results list by spaces to create a single string
    output_str = " ".join(str(num) for num in results)

    # Print the output string
    print(output_str)
