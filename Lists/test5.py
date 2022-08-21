

def reversing_list(n):
    a=n[::-1]
    return a

print(reversing_list([4, 5, 6, 7, 8, 9]))

#-------------------------------------------------------------------------------------------------------------------
# Function to reverse a list using list cpmprehension
def reverse_list(original_list):
    return [original_list[len(original_list) - i] for i in range(1, len(original_list)+1)]

original_list = [10, 11, 12, 13, 14, 15]
print(reverse_list(original_list))

