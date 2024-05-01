# # nama = "Fatma"
# # Nama = "Hana"
# # print("Ini adalah hasil ketika gw ketik 'nama' =", nama)
# # print("Ini adalah hasil ketika gw ketik 'Nama' =", Nama)
# # # lebar = input("Masukkan lebarnya: ")
# # # print("Nama anda adalah: ", nama)
# # # luas = (int(panjang) * int(lebar))
# # # # print(luas)
# # def print_range(start, end):
# # 	# Loop through the numbers from start to end
# # 	while start <= end:
# # 		print(start)

# # print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# # Fill in the blanks so that the while loop continues to run while the
# # "divisor" variable is less than the "number" parameter.

# def sum_divisors(number):
# # Initialize the appropriate variables
#   divisor = 0
#   total = 1

#   # Avoid dividing by 0 and negative numbers 
#   # in the while loop by exiting the function
#   # if "number" is less than one
#   if number < 1:
#     return 0 

#   # Complete the while loop
#   while number:
#     if number % divisor == 0:
#       total += divisor
#     # Increment the correct variable
#     number += 1

#   # Return the correct variable 
#   return number


# print(sum_divisors(0)) # Should print 0
# print(sum_divisors(3)) # Should print 1
# # 1
# print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# # 114
# animal = "Lamborghini"
# print(animal[-4:])

teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values()

class Food:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
class Martabak(Food):
    pass

class Bakso(Food):
    pass

john_eat = Martabak("Coklat", "john2")
print(john_eat.name)

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound))
 
class Piglet(Animal):
    sound = "Oink!"
 
class Cow(Animal):
    sound = "Moooo"

hamlet = Piglet("Hamlet")
hamlet.speak()
 
class Cow(Animal):
    sound = "Moooo"
 
milky = Cow("Milky White")
milky.speak()
