import csv
flights = []
with open('Fligths.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        flights.append(row)


filtered_flights = [row for row in flights if row["Departure"] == 'Philadelphia' and row["Destination"] == 'Los Angeles' and int(row["Price"]) < 1200)]
for flight in filtered_flights:
    print(flight)