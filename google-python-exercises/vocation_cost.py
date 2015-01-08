def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost
    
def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money
    return sum
    
print trip_cost("Los Angeles", 5, 600)