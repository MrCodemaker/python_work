class Restaurant():
    """docstring for Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        """Возвращает аккуратно отформатированное описание ресторана."""
        long_name = print(self.cuisine_type.title() +
                          " restaurant " +
                          self.restaurant_name.title())

    def open_restaurant(self):
        print("The restaurant is open!")


restaurant = Restaurant('meat and wine', 'italian')
print(restaurant.describe_restaurant())
print(open_restaurant())
