import sys
import string
import logging
import random

logging.basicConfig(level=logging.INFO)

item_list = []

class Movie:
    def __init__(self, title, year, plays, genere) -> None:
        self.title = title
        self.year = year
        self.genere = genere
        self.plays = plays

    def play(self, step=1):
        self.plays += step
        print(f"Wyświetliłem {self.title} po raz {self.plays} i dokonałem stosownego wpisu")

    
    def display(self):
        info = ("dodałem film i dopisałem go do listy->")
        item_list.append([f'{self.title}', f'{self.year}', f'{self.genere}', f'{0}', f'{0}', f'{self.plays}'])
        result = print(f"{info} {self.title}; {self.year}; {self.genere}; ''; ''; {self.plays}")
   
    def __str__(self):
        return f'{self.title} {self.year} {self.genere} wyświetlono {self.plays} razy'

    def __repr__(self):
        return f'{self.title} {self.year} {self.genere} wyświetlono {self.plays} razy'

class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def display(self):
        info = ("dodałem odcinek serialu i dopisałem go do listy->")
        item_list.append([f'{self.title}', f'{self.year}', f'{self.genere}', f'{self.episode_number}', f'{self.season_number}', f'{self.plays}'])
        result = print(f"{info} {self.title}; {self.year}; {self.genere}; {self.episode_number}; {self.season_number}; {self.plays}")

def get_movies():
    print("Wyświetlam zapisane fimy:")
    for item in item_list:
        if int(item[3]) == 0:
            print(f"{item[0]}; rok produkcji: {item[1]}; gatunek: {item[2]}")

def get_series():
    print("Wyświetlam zapisane seriale:")
    for item in item_list:
        if int(item[3]) >= 1:
            print(f"{item[0]} S0{item[4]}E0{item[3]}; rok produkcji: {item[1]}; gatunek: {item[2]}")

def search(title):
    for item in item_list:
        if item[0] == title:
            if int(item[3]) == 0:
                print(f"{item[0]}; rok produkcji: {item[1]}; gatunek: {item[2]}")
            if int(item[3]) >= 1:
                print(f"{item[0]} S0{item[4]}E0{item[3]}; rok produkcji: {item[1]}; gatunek: {item[2]}")

def generate_views(number):
    for generate in range(1, number):
        items_count = len(item_list)-1
        random_item = random.randint(0, items_count)
        random_views = random.randint(1, 200)
        for item in item_list:
            if item == item_list[random_item]:
                item[5] = int(item[5]) + random_views
                print(item)


dune = Movie(title= 'Dune', year= '2021', genere= 'sci-fi', plays= 5)
dune2 = Movie(title= 'Dune 2', year= '2023', genere= 'sci-fi', plays= 0)
neverwere1 = Series( title= 'Neverwere', year= '1996', genere= 'urban fantasy', episode_number= 1, season_number= 1, plays= 1)
neverwere2 = Series( title= 'Neverwere', year= '1996', genere= 'urban fantasy', episode_number= 2, season_number= 1, plays= 1)
neverwere2 = Series( title= 'Neverwere', year= '1996', genere= 'urban fantasy', episode_number= 3, season_number= 1, plays= 1)
neverwere4 = Series( title= 'Neverwere', year= '1996', genere= 'urban fantasy', episode_number= 4, season_number= 1, plays= 1)
neverwere5 = Series( title= 'Neverwere', year= '1996', genere= 'urban fantasy', episode_number= 5, season_number= 1, plays= 1)
neverwere6 = Series( title= 'Neverwere', year= '1996', genere= 'urban fantasy', episode_number= 6, season_number= 1, plays= 1)
avatar = Movie( title= 'Avatar', year= '2009', genere= 'sci-fi', plays= 1)


dune.display()
dune2.display()
neverwere1.display()
neverwere2.display()
neverwere2.display()
neverwere4.display()
neverwere5.display()
neverwere6.display()
avatar.display()

print(dune)

dune.play()

print(dune)

get_movies()
get_series()

search('Avatar')
search('Neverwere')

generate_views(5)

