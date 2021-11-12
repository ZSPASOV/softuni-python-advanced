from collections import deque

jobs = deque([int(n) for n in input().split(', ')])
#jobs = [int(n) for n in input().split(', ')]
index_job = int(input())
done_jobs = []
looked_job = jobs[index_job]
cycles = 0

while len(jobs) > 0 or looked_job <= min(deque):
    if looked_job < min(jobs):
        break
    cycles += jobs.pop()


print(cycles)

#print(sum(done_jobs) + jobs[index_job])