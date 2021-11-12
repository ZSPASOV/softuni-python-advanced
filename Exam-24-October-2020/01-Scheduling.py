# from collections import deque

# jobs = deque([int(n) for n in input().split(', ')])
jobs = [int(n) for n in input().split(', ')]
index_job = int(input())
done_jobs = []
looked_job = jobs[index_job]
cycles = 0

while True:
    if len(jobs) == 0 or min(jobs) > looked_job:
        break
    if jobs.index(min(jobs)) < index_job:
        cycles += jobs.pop(jobs.index(min(jobs)))
        index_job -= 1
    elif jobs.index(min(jobs)) > index_job:
        cycles += jobs.pop(jobs.index(min(jobs)))
    else:
        cycles += jobs.pop(index_job)


print(cycles)

#print(sum(done_jobs) + jobs[index_job])