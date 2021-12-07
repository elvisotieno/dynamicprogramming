# Although you can use slicing technique string[::-1] which is good/efficient in practice
# We'll use stack in this module to show our data structures skills

#Using Stack

def reverse_string(s):
    stack=[]
    for element in s:
        stack.append(element)

    reverse=''
    while len(stack)>0:
        reverse += stack.pop()
    return reverse

s='elvis'
print(reverse_string(s))

#Other techniques

# Using two-pointer sliding window protocal
def reverse_with_two_pointers(s):
    r= [char for char in s]
    p1=0
    p2=len(r)-1
    while p1<p2:
        r[p1],r[p2] = r[p2],r[p1]
        p1 +=1
        p2 -=1
    return ''.join(n for n in r)
print(reverse_with_two_pointers('sidney'))

#sing slicing
def reverse_with_slice(s):
    return s[::-1]

print(reverse_with_slice('Charles'))

