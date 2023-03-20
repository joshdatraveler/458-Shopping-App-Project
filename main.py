import item_class as ic
import find_item as fi
import txt_to_class_conv as ttcc
import suggest_similar as ss
import check_cart as cc
import checkout as co

#search = input ('input: ')
#print(fi.find_item(search))
#print(ic.add_item_inventory())

def main():
  user_cart = []
  checkout = False

  while checkout != True: 
    print ('User Menu:\n1. Search for item\n2. Check Cart\n3. Go to Checkout')
    user_act = int(input('Please Select an action: '))
    if user_act == 1:
      count = 0
      user_search = input("Enter your search: ")
      cur_querey = fi.find_item(user_search)
      #print (cur_querey)
      print ('Based on your search, here\'s what we found: ' )
      for item in cur_querey:
        count += 1
        print (str(count) + '. ' + str(item.item_name))

      user_choice = int(input('Enter the number of an item \nthat you would like more info on: '))
      if user_choice == 'menu':
        continue
      user_choice -= 1
      item = cur_querey[user_choice]
      print ('$'+ str(item.price))
      print (item.desc)
      print (str(item.stock)+ ' Left in Stock!!')
      print ('Would you like to add to cart or go to menu')
      add = int(input ('Press 1 to add, 2 to keep looking: '))
      if add == 1:
        user_cart.append(item)
        sug_list = ss.suggest_similar(item,cur_querey)
        print ('Here are some other things we think you would like: ')
        sug_list = sug_list[:3]
        count = 1
        for item in sug_list:
          print (str(count) + '. ' + str(item.item_name))
          count += 1
        print ('Enter the number of an item that you would like more info on: ')
        user_choice = int(input('Item number: '))
        user_choice -= 1
        item = sug_list[user_choice]
        print ('$'+ str(item.price))
        print (item.desc)
        print (str(item.stock)+ ' Left in Stock!!')
        print ('Would you like to add to cart or keep looking?')
        addsug = int(input('Press 1 to add, go back to menu:'))
        if addsug == 1:
          user_cart.append(item)
          #print (user_cart)
        elif addsug == 2:                  
          continue
      else:
        continue

    elif user_act == 2:
     checkout = cc.check_cart(user_cart)
    elif user_act == 3:
     checkout = co.checkout(user_cart)
    
        
if __name__ == '__main__':
  main()
