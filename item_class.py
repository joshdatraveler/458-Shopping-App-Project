class Product:
  def __init__(self,item_name,desc,price,stock,keyword):
    self.item_name = item_name
    self.desc = desc
    self.price = price
    self.stock = stock
    self.keyword = keyword
  def __repr__(self):
    return '{},{},{},{},{}'.format(self.item_name,self.desc,self.price,self.stock,self.keyword)

#gonna write up a code that adds instances of this class to a txt file that will act as the "inventory" - Josh

def add_item_inventory ():
  name = str(input("add item name: "))
  desc = str(input('Add brief description: '))
  price = float(input('Enter item price: '))
  stock = int(input('enter inventory amount: '))
  keywords = []
  add_keyword = str(input('Enter a keyword: '))
  keywords.append(add_keyword)
  add_keyword = str(input('Enter keyword or end to stop adding keywords: '))
  add_keyword = add_keyword.lower()
  while add_keyword != 'end':
    keywords.append(add_keyword)
    add_keyword = str(input('Enter keyword or end to stop adding keywords: '))
    add_keyword = add_keyword.lower()
  
  new_item = Product(name,desc,price,stock,keywords)
  print (new_item)
  with open('inventory.txt', 'a') as f:
    f.write('\n'+ str(new_item))


  