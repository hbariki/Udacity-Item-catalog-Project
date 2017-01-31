from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# create a user
User1 = User(name="Harshini", email="Harshinibariki@gmail.com")

#Menu for UrbanBurger
restaurant1 = Restaurant(name = "Urban Burger")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", course = "Entree", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", course = "Dessert", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99", course = "Beverage", restaurant = restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name = "Iced Tea", description = "with Lemon", price = "$.99", course = "Beverage", restaurant = restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", price = "$3.49", course = "Entree", restaurant = restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name = "Veggie Burger", description = "Made with freshest of ingredients and home grown spices", price = "$5.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem8)
session.commit()




#Menu for Super Stir Fry
restaurant2 = Restaurant(name = "Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name = "Chicken Stir Fry", description = "with your choice of noodles vegetables and sauces", price = "$7.99", course = "Entree", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Peking Duck", description = " a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25", course = "Entree", restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Spicy Tuna Roll", description = "Tuna Roll with spices", price = "$9.99", course = "Appetizer", restaurant = restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Nepali Momo ", description = "Special Nepali Momo", price = "$15", course = "Entree", restaurant = restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Beef Noodle Soup", description = "Beef Noodle soup", price = "$7.99", course = "Appetizer", restaurant = restaurant2)

session.add(menuItem5)
session.commit()




#Menu for Panda Garden
restaurant3 = Restaurant(name = "Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Pho", description = "a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.", price = "$7.99", course = "Appetizer", restaurant = restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chinese Dumplings", description = "a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", price = "$8.99", course = "Entree", restaurant = restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Gyoza", description = "The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner", price = "$12", course = "Entree", restaurant = restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Stinky Tofu", description = "Taiwanese dish, deep fried fermented tofu served with pickled cabbage.", price = "$9.99", course = "Entree", restaurant = restaurant3)
session.add(menuItem4)
session.commit()



#Menu for Thyme for that
restaurant4 = Restaurant(name = "Thyme for That Vegetarian Cuisine ")

session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(name = "Tres Leches Cake", description = "Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.", price = "$8.99", course = "Dessert", restaurant = restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Mushroom risotto", description = "Portabello mushrooms in a creamy risotto", price = "$7.99", course = "Entree", restaurant = restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Honey Boba Shaved Snow", description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price = "$9.99", course = "Beverage", restaurant = restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Cauliflower Manchurian", description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price = "$8.99",    course="Appetizer", restaurant = restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Aloo Gobi Burrito", description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", price = "$9.99", course = "Entree", restaurant = restaurant4)

session.add(menuItem5)
session.commit()




#Menu for Tony's Bistro
restaurant5 = Restaurant(name = "Tony\'s Bistro ")

session.add(restaurant5)
session.commit()


menuItem1 = MenuItem(name = "Shellfish Tower", description = "A Grilled Shellfish with spiced Onions.", price = "$7.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken and Rice", description = "A Deep fried chicken with cup of white rice.", price = "$10.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Mom's Spaghetti", description = "A spaghetti with mild species init.", price = "$8.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Chocolate Icecream", description = "A chocolate Icecream.", price = "$6.99", course = "Dessert", restaurant = restaurant5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Tonkatsu Ramen", description = "Noodles in a delicious pork-based broth with a soft-boiled egg", price = "$7.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem5)
session.commit()




#Menu for Andala's
restaurant6 = Restaurant(name = "Andala\'s")

session.add(restaurant6)
session.commit()


menuItem1 = MenuItem(name = "Lamb Curry", description = "Slow cook that thang in a pool of tomatoes, onions and al those tasty Indian spices.", price = "$11.99", course = "Entree", restaurant = restaurant6)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken Marsala", description = "Chicken cooked in Marsala wine sauce with mushrooms", price = "$9.99", course = "Entree", restaurant = restaurant6)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Potstickers", description = "Delicious chicken and veggies encapsulated in fried dough.", price = "$11.99", course = "Appetizer", restaurant = restaurant6)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Cheese cake", description = "A cheese cake with the toppings of choclate fillings and cherries", price = "$7.99", course = "Dessert", restaurant = restaurant6)

session.add(menuItem4)
session.commit()




#Menu for Pista House
restaurant7 = Restaurant(name = "Pista House ")

session.add(restaurant7)
session.commit()

menuItem9 = MenuItem(name = "Chicken65", description = "A deep fried chicken with authentic Indian species.", price = "$8.99", course = "Appetizer", restaurant = restaurant7)

session.add(menuItem9)
session.commit()



menuItem1 = MenuItem(name = "Mutton Biryani", description = "A Fully cooked mutton with Tomatoes, onions and a cooked birayni rice.", price = "$7.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken Tikka Masala", description = "Boiled chicken and gravy of onions and species.", price = "$8.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Egg noodles", description = "A boiled noodles with egg.", price = "$9.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Mango Lassi", description = "A Lassi added with Mango pulp Milk and sugar.", price = "$4.99", course = "Beverage", restaurant = restaurant7)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Gulab Jammon", description = "A deep fried Jammon with sugar syrup init.", price = "$4.99", course = "Dessert", restaurant = restaurant7)

session.add(menuItem5)
session.commit()





print "added menu items!"
