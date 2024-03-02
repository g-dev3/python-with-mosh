
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


numbers = [10,3,6,2]

def find(max):
    max = numbers[0]

    for number in numbers:
        if number > max:
            max = number
    print(max)