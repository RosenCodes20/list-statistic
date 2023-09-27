following_lines = int(input())
positive_list = []

negative_list = []

sum_of_neg = 0

count_of_pos = 0
for line in range(following_lines):
    number = int(input())

    if number >= 0:
        count_of_pos += 1

        positive_list.append(number)

    else:
        negative_list.append(number)

sum_of_neg = sum(negative_list)

print(positive_list)

print(negative_list)

print(f"Count of positives: {count_of_pos}")

print(f"Sum of negatives: {sum_of_neg}")
