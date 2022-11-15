from random import randint
from point import Point


def get_random_dict():
    count = randint(1, 10)
    random_dict = {}
    for index in range(count):
        x = randint(0, 10)
        y = randint(0, 10)
        point = Point(x, y)
        random_dict[index] = point
    return random_dict


def get_closest_couriers_dict(orders_dict, couriers_dict):
    closest_couriers_dict = {}
    for o_keys, o_val in orders_dict.items():
        min_dist = orders_dict[o_keys].get_dist(couriers_dict[0])
        courier = 0
        for c_keys, c_val in couriers_dict.items():
            dist = orders_dict[o_keys].get_dist(couriers_dict[c_keys])
            if dist < min_dist:
                min_dist = dist
                courier = c_keys
        closest_couriers_dict[o_keys] = courier
    return closest_couriers_dict


def to_deliver(delivering_order, closest_courier, orders, couriers):
    orders.pop(delivering_order)
    couriers[closest_courier] = Point(0, 0)
    print("Заказ №" + str(delivering_order) + "\tбыл доставлен курьером №" + str(closest_courier))
    return orders, couriers


if __name__ == '__main__':
    orders = get_random_dict()
    couriers = get_random_dict()
    while len(orders) > 0:
        closest_couriers = get_closest_couriers_dict(orders, couriers)
        delivering_orders = list(closest_couriers.keys())
        orders, couriers = to_deliver(delivering_orders[0], closest_couriers[delivering_orders[0]], orders, couriers)