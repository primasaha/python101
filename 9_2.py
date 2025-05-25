class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print()

restaurant1 = Restaurant("Takumi", "Japanese")
restaurant2 = Restaurant("Spice Heaven", "Indian")
restaurant3 = Restaurant("Tasty Treat", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
