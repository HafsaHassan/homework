def return_n_number(n):
    if n == 1:
        return 8
    else:
        return return_n_number(n - 1) + 7


# Test cases

print(return_n_number(1))  # Equals 8
print(return_n_number(5))  # Equals 36
print(return_n_number(10))  # Equals 71
