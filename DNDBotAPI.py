import random

def find_lowest(array):
    lowest_number = array[0]
    for x in range(len(array)):
        if (array[x] < lowest_number):
            lowest_number = array[x]
    return lowest_number

def array_total(array):
    previous_value = 0
    for x in range(len(array)):
        previous_value = previous_value + array[x]
    return previous_value

def roll_dice(amount, dice_type):
    dice_container = []
    for x in range(1, int(amount) + 1):
        roll = random.randint(1, int(dice_type))
        dice_container.append(roll)
    for x in range(0, len(dice_container)):
        return dice_container[x]

def roll_stat():
    dice_mem = []
    for x in range(4):
        dice = roll_dice(4, 6)
        dice_mem.append(int(dice))
    total = array_total(dice_mem) - find_lowest(dice_mem)
    return total

def roll_character():
    total_mem = []
    for x in range(6):
        total = roll_stat()
        total_mem.append(total)
    return total_mem


def merge_array(array):
    temp_array = []
    for x in range(len(array)):

        if (temp_array.__contains__(array[x])):
            temp_array = temp_array
        else:
            temp_array.append(array[x])

    return temp_array

def reroll_stats(array):
    temp_array = merge_array(array)
    print(temp_array)

    for x in range(len(temp_array)):
        #Gets the index of the array where the lowest number is found
        if (find_lowest(temp_array) == temp_array[x]):
            first_index = x
            array.pop(x)
            array.insert(x, roll_stat())

        #Dets the index of the array where the second lowest number is found
        if(find_lowest(array) == array[x]):

            array.pop(x)
            array.insert(x, roll_stat())
    return array