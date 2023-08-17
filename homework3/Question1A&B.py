def process_queue(input_file):
    queue = []

    with open(input_file, 'r') as f:
        for line in f:
            command, name = line.strip().split()
            if command == "JUMP":
                queue.insert(0, name)  # Insert to front of queue
            elif command == "JOIN":
                queue.append(name)     # Append to back of queue

    return queue


def main():
    input_file = "names.txt"
    final_order = process_queue(input_file)

    print("Order of queue:")
    for position, name in enumerate(final_order, start=1):
        print(f"{position}. {name}")


if __name__ == "__main__":
    main()

# Time Complexity:
# Reading the names.txt file will take as long as how many lines there are.
# Therefore, this would be O(n).
# Completing each command only requires inserting to the front or to the back.
# Therefore, this would be O(1).
# Printing the order of the queue would take longer depending on how many names.
# Therefore, this would be O(n).
# Overall, the time complexity would be O(n).

# Space Complexity:
# Similar to time, the more names and people jumping to the front there are,
# the more space will be required.
# Therefore, this would be O(n).
# Printing the names will conistantly take up space.
# Therefore, this would be O(1).
# Overall, the space complexity would be O(n).

# Assumptions:
# There are no sorting or searching operations to impact the complexity.
# All names in the names.txt file will have either JUMP or JOIN before the name.
