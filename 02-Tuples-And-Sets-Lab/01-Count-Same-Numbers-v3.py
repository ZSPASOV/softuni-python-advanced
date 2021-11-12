nums = tuple(float(t) for t in input().split())
s = set()

for number in nums:
    if number not in s:
        s.add(number)
        print(f'{number} - {nums.count(number)} times')