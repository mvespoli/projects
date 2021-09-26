import math
import string
# import numpy as np
class PaginationHelper:
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
      counter = 0
      item_index += 1
      if item_index > len(self.pizza) or item_index < 1:
        print (-1)
        return -1
      while item_index > self.items_per_page:
        item_index -= self.items_per_page
        counter += 1
      print(counter)
      return counter

    
    #   # returns the number of items on the current page. page_index is zero based
#   # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
      if page_index >= len(self.pages_array) or page_index < 0:
        print(-1)
        return -1
      print(self.pages_array[page_index])
      print(len(self.pages_array[page_index]))
      return len(self.pages_array[page_index])
      # array = [self.list[i::i + page_index] for i in range(0, len(self.list), self.items_per_page)]
      

      # arr = np.array(self.list)
      # print(arr)
      # newarr = np.array_split(arr, self.items_per_page)
      
      # print(newarr)
      # # if IndexError:
      # #   ans = -1
      # # else:
      # try:
      #   ans = len(newarr[page_index-1]) 
      # except IndexError:
      #   ans =-1
      
      
      # print (ans)
    # returns the number of pages
    def page_count(self):
      print (self.pages)
      return self.pages
      
  # returns the number of items within the entire collection
    def item_count(self):
      print (self.items)
      return self.items
  
  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
    def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page
      self.items = len(collection)
      self.pizza = str((string.ascii_lowercase[:len(collection)]))
      self.pizza = list(self.pizza)
      self.pages = math.ceil(self.items/self.items_per_page)
      counter = 0
      self.pages_array = []
      while counter < len(self.pizza):
        current_page = []
        for i in range(0, items_per_page):
          if counter < len(self.pizza):
            current_page.append(self.pizza[counter]) 
          counter += 1
        self.pages_array.append(current_page)
        
  
#   # determines what page an item is on. Zero based indexes.
#   # this method should return -1 for item_index values that are out of range
#     def page_index(self,item_index):
    
#     print(collection)

collection = range(1,7)
helper = PaginationHelper(collection, 4)
helper.item_count()
helper.page_count()
helper.page_item_count(-1)
helper.page_index(-7)