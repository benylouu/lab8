import random

def kbig(nums, k):
#deviding the array into three parts, introducing temporary variables
    random_number_in_array = random.choice(nums)
    sleva = [y for y in nums if y > random_number_in_array]
    poseredine = [y for y in nums if y == random_number_in_array]
    sprava = [y for y in nums if y < random_number_in_array]
    
    LOL,MOL = len(sleva),len(poseredine)

#searching for the correct digit that we need
    if k <= LOL:
        return kbig(sleva, k)
    elif k > (LOL+MOL):
        return kbig (sprava, k-(LOL+MOL))
    else:
        return poseredine[0]
#yay it works!
