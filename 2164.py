import sys
import collections

N = int(sys.stdin.readline().rstrip())
card = collections.deque([i for i in range(N)])

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card[0]+1)