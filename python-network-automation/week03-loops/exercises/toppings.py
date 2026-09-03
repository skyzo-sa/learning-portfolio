requested_toppings = ['mushrooms', 'extra cheese']

# checks to see whether the person requested mushrooms on their pizza
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
# checks to see whether the person requested mushrooms on their pepperoni
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
# checks whether extra cheese was requested,
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")