arr = [1,2,3,4,2,6,5,6,8,8,7,7,9];

print("Duplicate element in given array : ")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]==arr[j]):
            print(arr[j])