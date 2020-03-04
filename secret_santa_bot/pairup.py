import random
from collections import deque


def pairup(people):
    random.shuffle(people)
    partners = deque(people)
    partners.rotate(n=random.randint(1, len(people)))
    pairs = zip(people, partners)
    return [{'gifter': thing1, 'giftee': thing2, 'retired': False} for thing1, thing2 in pairs]
