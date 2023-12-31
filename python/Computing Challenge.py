'''

Let's consider a string consisting of 10 characters “2”: string = “2222222222”

This computing challenge consists of writing an algorithm to work out the largest number we can create by inserting 2 multiplication operators (*) anywhere within this string.

For instance:

2 * 2 * 22222222 = 88,888,888
2 * 22 * 2222222 = 97,777,768
2222 * 2222 * 22 = 108,620,248
222 * 222 * 2222 = 109,509,048
etc.

'''

a = "2222222222"

pos1 = 1    # max value of pos is 9
pos2 = 1    # two pos values cannot be the same

biggest = 0
bigpos1 = 0
bigpos2 = 0

while pos1 < 9:
    pos2 = 1
    while pos2 < 9:
        if (not pos1 == pos2) and (not pos2 < pos1):
            head = int(a[:pos1])
            body = int(a[pos1:pos2])
            tail = int(a[:(10-pos2)])
            ans = head * body * tail
            
            if ans > biggest:
                biggest = ans
                bigpos1 = pos1
                bigpos2 = pos2

        pos2 += 1
    pos1 += 1

a = a[:bigpos1] + "*" + a[bigpos1:bigpos2] + "*" + a[bigpos2:]

print(str(a) + " = " + str(biggest))




