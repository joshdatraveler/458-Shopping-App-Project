import item_class as ic
import txt_to_class_conv as ttcc
#items will be classes stored in another document
#this funtion will be the search function that runs when a user searches

def find_item(search):
  search = ("'" +  str(search) + "'")
  search_list = []
  txtfile = 'inventory.txt'
  item_list = ttcc.txt_to_class_conv(txtfile)
  #print (item_list)
  
  for item in item_list:
    #print (item.keyword)
    for key in item.keyword:
      #print(key)
      if search == key:
        search_list.append(item)

  for item in search_list:
    if search_list.count(item) > 1:
      search_list.remove(item)
  return search_list
      

    







#search will be tailored to look for keywords and names. a list of items with matching name and keyword1 will be presented after the user searches (these will be stored in a temp list so the user can go between list data and individual item data) - Josh