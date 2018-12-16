def sum_numbers(numbers=None):
    if numbers == None:
        return sum(range(1,101))
    if len(numbers) == 0:
        return 0
    return sum(numbers)

print(sum_numbers([1,2,3]))
print(sum_numbers(range(1,11)))
print(sum_numbers([]))
print(sum_numbers(None))
