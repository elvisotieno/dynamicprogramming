#https://www.tutorialspoint.com/python_data_structure/python_heaps.htm#:~:text=Create%20a%20Heap.%20A%20heap%20is%20created%20by,element%20gets%20pushed%20to%20the%20index%20position%200.
#usecase : It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.
#creating heap
#created using python's inbuild library called heapq

import heapq

def min_heap():
    #A) create minn heap from a list using heapq.heapify(List) method
    H = [21,1,45,78,3,5]
    # Use heapify to rearrange the elements
    heapq.heapify(H)
    print(f'created heap: {H}')

    #B) Inserting into heap
    heapq.heappush(H,4)
    print(f'new heap after insertion is: {H}')

    #C) removing top element from the heap(deletion)
    heapq.heappop(H)
    print(f'after deletion: {H}')

    #D) updating by Replacing in a Heap

    heapq.heapreplace(H,6)
    print(f' after replacing: {H}')

min_heap()

def max_heap(H):
    h=[h*-1 for h in H ]
    heapq.heapify(h)
    print(h)

    # B) Inserting into heap
    heapq.heappush(h, -4)
    print(f'new heap after insertion is: {h}')

    # C) removing top element from the heap(deletion)
    heapq.heappop(h)
    print(f'after deletion: {h}')

    # D) updating by Replacing in a Heap

    heapq.heapreplace(h, -6)
    print(f' after replacing: {h}')

H=[30,10,50,16,15]
max_heap(H)


