
# import time
# import logging
# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import allure
# # from pageObjects.LoginPage import LoginPage
# # from utilities.URLs import URLs

# driver = webdriver.Chrome()

# driver.maximize_window()
# time.sleep(2)

# driver.get("https://pilot.karobarapp.com/")
# time.sleep(2)
# element = driver.find_element(By.NAME, "phoneNumber")
# element.send_keys("9860")
# time.sleep(2)
# element.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
# time.sleep(2)
# element.clear()
# time.sleep(2)
# driver.quit()



from datetime import date


def Sudoku_add_and_copy():
  def print_sudoku(numbers: list):
    for number in range(len(numbers)):
      for i in range(9):
        if numbers[number][i] == 0:
          print("_", end="")
        else:
          print(numbers[number][i], end="")
        if (i + 1) % 3 == 0:
          print(" ", end="")
      print()
      if (number + 1) % 3 == 0:
        print()
    
      
  def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_grid = [row[:] for row in sudoku]
    new_grid[row_no][column_no] = number
    return new_grid

  if __name__ == "__main__":
    sudoku  = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 5, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

def tic_tac_toe():
  def play_turn(game_board: list, x: int, y: int, piece: str):
    if game_board[y][x] == "":
      game_board[y][x] = piece
      return True
    else:
      return False

  if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

def transpose_matrix():
  def transpose(matrix: list):
    for i in range(len(matrix)):
      for j in range(i+1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix
  if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(matrix))

def dictionary():
  def times_ten(start_index: int, end_index: int):
    new_dictionary = {}
    for i in range(start_index, end_index):
      new_dictionary[f"{start_index}"] = f"{start_index*10}"
    
    return new_dictionary

  if __name__ == "__main__":
    print(times_ten(1, 5))
    
def factorials():
  def factorials(n: int):
    new_dictionary = {
      1 : 1,
      2 : 2
    }
    for i in range(3, n+1):
      factorial = 1
      for j in range(1, i+1):
        factorial *= j
      new_dictionary[i] = factorial
    
    return new_dictionary

  if __name__ == "__main__":
    k = factorials(10)
    print(k[4])

def count_dictionery():
  def count(word_list):
    new = {}
    for word in word_list:
      if word not in new:
        new[word] = 0
      
      new[word] += 1

    return new

  if __name__ == "__main__":
    word_list = [
    "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
    "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
    "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
    ]

    print(count(word_list))

def print_with_starting_name():
  def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
      initial = word[0]
      if initial not in groups:
        groups[initial] = []
      groups[initial].append(word)
    return groups
  if __name__ == "__main__":
    word_list = [
    "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
    "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
    "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
    ]
    groups = categorize_by_initial(word_list)
    for key, value in groups.items():
      print(f"words beginning with {key}:")
      for word in value:
        print(word)
      print()

def histogram():
  def histogram(word):
    result = {}
    for i in word:
      initial = i
      if i not in result:
        result[i] = []
      result[i].append("*")
    return result
  if __name__ == "__main__":
    word = "statistically"
    
    result = histogram(word)
    for key, value in result.items():
      print(key, end=" ")
      for i in value:
        print(i, end="")
      print()

def phone_book():
  while True:
    phone_book={"ram": "123"}
    command = input("command (1 search, 2 add, 3 quit): ")
    if command == "1":
      name = input("name: ")
      if name not in phone_book:
        print("no number")
        
      else:
        print(phone_book[name])
        
    elif command == "2":
      name = input("name: ")
      number = input("number: ")
      phone_book[name] = number
      print("ok!")

    elif command == "3":
      print("quitting...")
      break

def invert_dictionary():
  def invert_dictionary(dictionary):
    item = list(dictionary.items())
    dictionary.clear()
    for key, value in item:
      dictionary[value] = key

  s = {'a': 1, 'b': 2, 'c': 3}
  invert_dictionary(s)
  print(s)

def get_average_height_dictionary():

  person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
  person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
  person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}

  people = [person1, person2, person3]
  combined_height = 0
  for person in people:
    combined_height += person["height"]
  
  average = combined_height/len(people)

  print(average)

def movie_dictionary():
  
  database = []
  def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(movie)
  add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
  add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
  print(database)

def search_movies():
  def find_movies(database: list, search_term: str):
    new = []
    for movie in database:
      if search_term in movie["name"].lower():
        new.append(movie)

    return new


  database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
  {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
  {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

  my_movies = find_movies(database, "python")
  print(my_movies)

def create_tuple():
  def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    highest = max(x, y, z)
    sum = x + y + z
    return (smallest, highest, sum)
  if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

def oldest_person():
  def oldest_person(people: list):
    oldest = ""
    age = 1999
    for person in people:
      if person[1] < age:
        oldest = person[0]

    print(oldest)


  p1 = ("Adam", 1977)
  p2 = ("Ellen", 1985)
  p3 = ("Mary", 1953)
  p4 = ("Ernest", 1997)
  people = [p1, p2, p3, p4]
  oldest_person(people)
  
def oldest_person_2():
  def older_people(people: list, year: int):
    list = []
    for person in people:
      if person[1] < year:
        list.append(person[0])
    
    return list

def object_and_method():
  def smallest_average(person1: dict, person2:dict, person3:dict):
    result = 0
    persons = [person1, person2, person3]
    for person in persons:
      person_average = (person["result1"] + person["result2"] + person["result3"])/len(persons)
      if person_average > result:
        result = person_average
  def pet():
    class Pet:
      def __init__(self, name: str, species: int, year_of_birth: str):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

    new_pet = Pet
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)
  def older_book1():
    class Book:
      def __init__(self, name, author, genre, year):
  
          self.name = name  # Assigning the book title
          self.author = author  # Assigning the book's author
          self.genre = genre  # Assigning the book's genre
          self.year = year  # Assigning the publication year

    # Creating instances of the Book class
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)
    def older_book(book1: Book, book2: Book):
      if book1.year > book1.year:
        print(f"{book1.name}, is older, it was published in {book1.year}")
      elif book1.year < book2.year:
        print(f"{book2.name}, is older, it was published in {book2.year}")
      else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
    
    return older_book(python, everest)
  
  
  older_book1()

def bank():
  class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float, account_interest: float):
      self.account_number = account_number
      self.owner = owner
      self.balance = balance
      self.account_interest = account_interest
    
    def add_interest(self):
      self.balance += self.balance * self.account_interest

    def withdraw(self, amount: float):
      if amount >= self.balance:
        self.balance -= amount
        return True
      
      return False
  
  peters_account = BankAccount("123456789", "Peter Python", 1000, 0.05)
  print(peters_account.balance)
  
  if peters_account.withdraw(1000):
    print(f"Withdrawal successful, new balance is {peters_account.balance}")
  else:
    print("Withdrawal failed, insufficient funds")

def decreasing_counter():
  class DecreasingCounter:
    def __init__(self, initial_value: int):
      self.value = initial_value
      self.initial_value = initial_value

    def print_value(self):
      print("value:", self.value)

    def decrease(self):
      if self.value > 0:
        self.value -= 1

    def set_to_zero(self):
      self.value = 0

    def reset_original_value(self):
      self.value =  self.initial_value

  counter = DecreasingCounter(55)
  counter.decrease()
  counter.decrease()
  counter.decrease()
  counter.decrease()
  counter.print_value()
  counter.reset_original_value()
  counter.print_value()

def player():
  class PersonalBest:
    def __init__(self, player: str, day: int, month: int, year: int, points: int):
      # Default values
      self.player = ""
      self.date_of_pb = date(1900, 1, 1)
      self.points = 0

      if self.name_ok(player):
        self.player = player

      if self.date_ok(day, month, year):
        self.date_of_pb = date(year, month, day)
      
      if self.points_ok(points):
          self.points = points

    def name_ok(self, name: str) -> bool:
      return len(name) >= 2
    
    def date_ok(self, day, month, year):
      try:
        date(year, month, day)
        return True
      except Exception:
        return False
      
    def points_ok(self, points):
      return points >= 0
   

def rectabgle():
  class Rectangle:
    def __init__(self, left_upper: tuple, right_lower: tuple):
      self.left_upper = left_upper
      self.right_lower = right_lower
      self.width = right_lower[0]-left_upper[0]
      self.height = right_lower[1]-left_upper[1]

      def area(self):
        return self.width * self.height
      
      def __repr__(self):
        return f"Rectangle: ({self.left_upper}, {self.right_lower})"

  rectangle = Rectangle((0, 0), (10, 10))
  print(rectangle)

def stopwatch():
  class Stopwatch:
    def __init__(self):
      self.seconds = 0
      self.minutes = 0
    
    def __str__(self):
      return f"{self.minutes:02}:{self.seconds:02}"

    def tick(self):
      self.seconds += 1
      if self.seconds == 60:
        self.seconds = 0
        self.minutes += 1

  class Clock:
    def __init__(self, hour, minute, second):
      self.hour = hour
      self.minute = minute
      self.second = second
    
    def __str__(self):
      return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def set(self, hour, minute, second=0):
      self.hour = hour
      self.minute = minute
      self.second = second


var = "google"
len = len(var)-1
for i in range(len, -1, -1):
  print(var[i])