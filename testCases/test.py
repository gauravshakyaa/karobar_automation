
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
import requests
import os


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
  
  p1 = ("Adam", 1977)
  p2 = ("Ellen", 1985)
  p3 = ("Mary", 1953)
  p4 = ("Ernest", 1997)
  people = [p1, p2, p3, p4]

  older = older_people(people, 1979)
  print(older)

# oldest_person_2()
