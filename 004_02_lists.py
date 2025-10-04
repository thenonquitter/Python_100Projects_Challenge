# list is a kind of data structures.
# list has a order.
# list uses positive or negative indices.
#.append(elements)

import random

friends = ["앨리스", "밥", "찰리", "데이비드", "임마누엘"]
pick = random.randint(0,4)
print(friends[pick])

print(random.choice(friends))

# IndexError
# index 번호를 잘못 참조
# 원소의 갯수와 인덱스 번호를 착각하여 발생하기 쉬움

# nested lists
# 리스트를 리스트의 원소로 삼을 수 있다