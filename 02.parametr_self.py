# -*- coding: utf-8 -*-
class Drzewo:
    
    def wyswietl_info_o_drzewie(self):
        self.nazwa = 'Sosna'
        self.wiek = 30
        print(f'Drzewo {self.nazwa} ma {self.wiek} lat.')

drzewo = Drzewo()

# %%
drzewo.wyswietl_info_o_drzewie()
# %%
Drzewo.wyswietl_info_o_drzewie(drzewo)
# %%

class User:
    age = 0
    name = " "
    def print_age(message, self):
        print(message, "wiek: ", self.age, self.name)
    
user1 = User()
user2 = User()

user1.age = 24
user1.name = "Ola"
user1.print_age("Dodatkowy tekst")

user2.age = 25
user2.name = "Ela"        
user1.print_age("Dodatkowy tekst2")

# %%
age = 450
class User:
    age = 0
    def print_age(self):
        print("wiek: ", age)
        
mirek = User()
mirek.age = 24

mirek.print_age()#Wynik to wiek: 450 ponieważ nie zastosowalismy parametru self
# %%
age = 450
class User:
    age = 0
    def print_age(self):
        print("wiek: ", self.age)
        
mirek = User()
mirek.age = 24

mirek.print_age()#Wynik to wiek: 24 po zastosowanie self

# %%
age = 450
class User:
    age = 0
    def print_age(self):
        print("wiek: ", self.age)
        
mirek = User()
#mirek.age = 24

mirek.print_age()#wynik to wiek: 0 poniewaz przywrocony zostal par.domyslny
