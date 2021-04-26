class Shoes:
    
    color = "Color of all these pairs is purple\n"

    def __init__(self, name = "unknown", price = "unknown", size = "unknown", country = "unknown", year = "unknown", ):
        self.name = name 
        self.price = price
        self.size = size
        self.country = country
        self.year = year

       
    def __str__(self):
       return f"Brand name is {self.name}\nPrice of this pair is {self.price} dollars\n
       Size of this pair is {self.size}\nCountry in which it was made is {self.country}\nYear when it was made is {self.year}\n"
    
    @staticmethod
    def color_shower():
        return Shoes.color

    def __del__(self):
        print("Destructor worked succrsfully")


pair1 = Shoes("Nike", 380, 9.5)
pair2 = Shoes("Abidas", 90, 7.0, "China")
pair3 = Shoes("Puma", 185, 11.0, "Germany", 2018)


print(pair1)
print(pair2)
print(pair3)

print(Shoes.color_shower())
