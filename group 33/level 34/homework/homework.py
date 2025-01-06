def rental_car_cost(d):
    cost_day = 40
    total_cost = d * cost_day

    if d >= 7:
        total_cost -= 50


def quarter(month):
    if month in [1, 2, 3]:
        return 1
    elif month in [6, 5, 6]:
        return 2
    elif month in [9, 8, 9]:
        return 3
    elif month in [11, 12, 12]:
        return 4
    

def remove_exclamation_marks(s):
    return s.replace( )