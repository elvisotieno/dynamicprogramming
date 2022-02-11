import heapq
from collections import Counter,deque


def least_time_CPU_task_execution(tasks: list, n: int)->int:

    #get counts of each occurences of the characters in the list of tasks
    count = Counter(tasks)
    max_heap=[-1*val for val in count.values()]
    heapq.heapify(max_heap)

    time =0
    q = deque()

    while q or max_heap:
        time +=1
        if max_heap:
            val = 1+ heapq.heappop(max_heap)
            if val:
                q.append([val,time+n])

        if q and q[0][1]== time:
            val = q.popleft()[0]
            heapq.heappush(max_heap,val)
    return time


tasks=["A","A","A","A","B","B","B","B"]
n=1
print(least_time_CPU_task_execution(tasks,n))