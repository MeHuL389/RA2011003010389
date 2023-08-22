import requests
import json

def get_train_schedule(source, destination):
  """Gets the train schedule for the given source and destination stations."""

  url = "https://www.irctc.co.in/nget/train-search"
  params = {
    "source": source,
    "destination": destination,
  }

  response = requests.get(url, params=params)
  response.raise_for_status()

  data = json.loads(response.content)

  return data

def calculate_seat_availability(train_data):
  """Calculates the seat availability for the given train."""

  sleeper_coach_seats = train_data["coach_availability"]["SL"]
  ac_coach_seats = train_data["coach_availability"]["AC"]

  return {
    "sleeper_coach_seats": sleeper_coach_seats,
    "ac_coach_seats": ac_coach_seats,
  }

def calculate_prices(train_data):
  """Calculates the prices for the given train."""

  sleeper_coach_price = train_data["fare"]["SL"]
  ac_coach_price = train_data["fare"]["AC"]

  return {
    "sleeper_coach_price": sleeper_coach_price,
    "ac_coach_price": ac_coach_price,
  }

def get_delay(train_data):
  """Gets the delay for the given train."""

  delay = train_data["delay"]

  return delay

def main():
  """Main function."""

  source = input("Enter the source station: ")
  destination = input("Enter the destination station: ")

  train_data = get_train_schedule(source, destination)

  seat_availability = calculate_seat_availability(train_data)
  prices = calculate_prices(train_data)
  delay = get_delay(train_data)

  print("Train number:", train_data["train_number"])
  print("Train name:", train_data["train_name"])
  print("Source station:", train_data["source"])
  print("Destination station:", train_data["destination"])
  print("Departure time:", train_data["departure_time"])
  print("Arrival time:", train_data["arrival_time"])
  print("Distance:", train_data["distance"])
  print("Sleeper coach seat availability:", seat_availability["sleeper_coach_seats"])
  print("AC coach seat availability:", seat_availability["ac_coach_seats"])
  print("Sleeper coach price:", prices["sleeper_coach_price"])
  print("AC coach price:", prices["ac_coach_price"])
  print("Delay:", delay)

if __name__ == "__main__":
  main()
