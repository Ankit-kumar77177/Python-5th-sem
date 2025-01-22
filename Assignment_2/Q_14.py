room_type = input("Enter room type (Standard/Deluxe/Suite): ")
nights = int(input("Enter number of nights: "))
season = input("Enter season (Peak/Off/Regular): ")
loyalty = input("Is customer a loyalty member? (Yes/No): ")

if room_type == "Standard":
    base_cost = 100 * nights
elif room_type == "Deluxe":
    base_cost = 150 * nights
else:
    base_cost = 250 * nights

if nights > 7:
    base_cost *= 0.8
elif nights > 3:
    base_cost *= 0.9

if season == "Peak":
    base_cost *= 1.2
elif season == "Off":
    base_cost *= 0.85

if loyalty == "Yes":
    base_cost *= 0.95

print("Final booking cost:", base_cost)
