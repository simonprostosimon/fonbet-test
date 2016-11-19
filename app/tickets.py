import random 


def is_lucky(number):
    assert isinstance(number, int) or isinstance(number, str)

    number = str(number)

    return sum(map(lambda v: int(v), number[:3])) == sum(map(lambda v: int(v), number[-3:]))

def gen_random(length=6):
    assert isinstance(length, int) 
    
    return ''.join([str(random.randint(0, 9)) for _ in range(length)]) # NOTE: May be dangerous if length is a large number (beacuase str is immutable) 
    
