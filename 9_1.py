class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print('this is a initialization method')

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now!")

restaurant= Restaurant ('Takumi','Japanese')

restaurant.describe_restaurant()
restaurant.open_restaurant()
