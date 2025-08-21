from datetime import datetime
from app.customer import Customer, customers
from app.shop import Shop, shops
from app.car import distance_cost


customers_list = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        customer["car"]
    ) for customer in customers]
shops_list = [
    Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    ) for shop in shops]


def shop_trip() -> None:
    for customer in customers_list:
        print(f"{customer["name"]} has {customer["money"]} dollars")
        trip_costs = {
            shop: distance_cost(customer, shop) + shop.products_cost(customer)
            for shop in shops_list
        }
        for shop, cost in trip_costs.items():
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        cheapest_shop = min(trip_costs, key=trip_costs.get)
        min_cost = trip_costs[cheapest_shop]

        if min_cost < customer["money"]:
            print(f"{customer["name"]} rides to {cheapest_shop.name}\n")
            date = datetime(2021, 1, 4, 12, 33, 41)
            print(f"Date: {date.strftime("%d/%m/%Y %H:%M:%S")}")
            print(f"Thanks, {customer["name"]}, for your purchase!")
            print("You have bought:")
            for key, value in customer.product_cart.items():
                cost = (cheapest_shop.products[key] * value)
                if str(cost).count(".0") > 0:
                    cost = int(cost)
                print(f"{value} {key}s for {cost} dollars")
            print(
                f"Total cost is "
                f"{cheapest_shop.products_cost(customer)} dollars"
            )
            print("See you again!\n")
            print(f"{customer["name"]} rides home")
            print(
                f"{customer["name"]} now has "
                f"{customer["money"] - min_cost} dollars\n"
            )
        else:
            print(
                f"{customer["name"]} doesn't have "
                f"enough money to make a purchase in any shop"
            )
