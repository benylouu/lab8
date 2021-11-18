import random
#sorry for the variables names, haha <3

def kbig(nums, k):
    random_number_in_array = random.choice(nums)
    sleva = [y for y in nums if y > random_number_in_array]
    poseredine = [y for y in nums if y == random_number_in_array]
    sprava = [y for y in nums if y < random_number_in_array]
    
#fun fact: did you know that death penalty costs more for the country than life sentence all because of layers?
    LOL,MOL = len(sleva),len(poseredine)

    if k <= LOL:
        return kbig(sleva, k)
    elif k > (LOL+MOL):
        return kbig (sprava, k-(LOL+MOL))
    else:
        return poseredine[0]

print (kbig ([3,2,3,1,2,4,5,5,6], 4))
