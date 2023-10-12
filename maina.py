import tkinter as tk
from tkinter import scrolledtext
from random import choice

last_computer_letter = None

def check_city():
     global last_computer_letter

     city = entry.get().title()  
     if not city:   
          response = f"Ви ввели місто "
     elif city in used_cities:
          response= f"місто {city} вже було використано"
     elif city not in cities:
          response= f"Місто {city} відсутнє в списку який знає гра"
     elif last_computer_letter and city[0] != last_computer_letter:
          response = f"Місто повинно починатися на літеру {last_computer_letter}"
     else:    
          used_cities.append(city) 
          last_letter = get_last_letter(city)
          
          computer_city = get_city_by_letter(last_letter)
          if not computer_city:
               response = f"Ви виграли! Я не знаю міст на літеру {last_letter}"
          else:
               used_cities.append(computer_city)
               last_computer_letter = get_last_letter(computer_city)
               response = f"Мій варіант місто - {computer_city}"   

              
     game_log.config(state=tk.NORMAL)    
     game_log.insert(tk.END, f"Ви: {city}\n")   
     game_log.insert(tk.END, f"Гра:{response}\n" ) 
     game_log.yview(tk.END)
     game_log.config(state=tk.DISABLED)
     notification.config(text=response)
     entry.delete(0, tk.END)

def get_last_letter(city):
    exceptions = ["\u042c", "\u0419", "\u0418"]
    last_letter = city[-1].upper()
    while last_letter in exceptions:
         city = city[:-1]
         last_letter = city[-1].upper()
    return last_letter
    

def get_city_by_letter(letter):
     available_cities = []
     for city in cities:
          if city[0].upper() ==letter and city not in used_cities:
               available_cities.append(city)
     if available_cities:
          return  choice(available_cities) 
     return None       

def surrender():
    game_log.config(state=tk.NORMAL)    
    game_log.insert(tk.END, f"Суперник попереду\n")   
    game_log.yview(tk.END)
    game_log.config(state=tk.DISABLED)
    notification.config(text="Суперник попереду; Спробуйте ще раз")
    entry.delete(0, tk.END) 


def load_cities_from_file(filename):
     cities =[]
     with open(filename, "r", encoding="utf-8") as fd:
          for line in fd:
               cities.append(line.strip())
     return cities         
          
cities = load_cities_from_file("cities(1).txt") 
used_cities =  []            

root =tk.Tk()
root.title("Гра в міста")
root.geometry("800x400")

left_frame=tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

label=tk.Label(left_frame, text="Введіть назву міста")
label.pack(padx=10, pady=10)

entry=tk.Entry(left_frame, width=35)
entry.pack(padx=10, pady=10)
button_frame = tk.Frame(left_frame)
button_frame.pack(pady=10)


button=tk.Button(button_frame, text="Відправити", command=check_city )
button.pack(padx=10, side=tk.LEFT)

button_end=tk.Button(button_frame, text="Competitor win", command=surrender )
button_end.pack(padx=10, side=tk.LEFT)

notification=tk.Label(left_frame, text="")
notification.pack(padx=10,pady=10)

game_log=scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
game_log.pack(padx=10, pady=10, side=tk.RIGHT)
game_log.config(state=tk.DISABLED)

root.mainloop()