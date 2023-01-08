# import sys

# sys.stdin = open('H:\내 드라이브\Colab Notebooks\myCode\CodingTest\BaekJoon\p2588\input.txt')

# while sys.stdin.read(readline):
#     print(sys.stdin.readline())
n1 = int(input('first Num :'))
n2 = input('second Num : ')
sum = 0
for i in range(len(n2)-1,-1,-1) :
    print(int(n2[i]) * n1)
    sum += int(n2[i]) * n1 * (10**(len((n2))-i-1))
print(sum)