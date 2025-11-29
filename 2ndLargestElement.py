n = int(input("Enter number of elements: "))

arr = []
print("Enter array elements:")
for _ in range(n):
    arr.append(int(input()))

largest = float("-inf")
second_largest = float("-inf")

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float("-inf"):
    print("No second largest element found.")
else:
    print("Second largest element:", second_largest)
