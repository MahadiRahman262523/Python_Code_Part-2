
from collections import deque

bank = deque(["mahadi","rahamn","dhrubo"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

if not bank :
    print("no person left")
