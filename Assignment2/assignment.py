def find_pair(nums, target):
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            print(f"Pair found ({num}, {complement})")
            return
        seen.add(num)

    print("Pair not found.")

if __name__ == "__main__":
    # Take input from the user for the first example
    numlist = list(map(int, input("Enter list for numbers -- separated by space ").split()))
    # numlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    target1 = int(input("Enter the sum required "))
    print("\nThe list is::>",numlist)
    find_pair(numlist, target1)
