import random
from collections import deque


def pairup(people):
    random.shuffle(people)
    partners = deque(people)
    partners.rotate(n=random.randint(1, len(people)))
    return zip(people, partners)
