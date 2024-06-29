flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Jim", "Athens", "Guadalajara")]

flights_to_print = []

for index, flight in enumerate(flights):
    traveller, origin, destination = flight
    new_string = f"Itenerary {index+1}: {traveller} - From {origin} to {destination}"
    flights_to_print.append(new_string)

separator = "\n"

string = separator.join(flights_to_print)

print(string)