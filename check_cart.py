import checkout as co
import item_class as ic

def check_cart(cart):
  total = 0
  for item in cart:
    print (item.item_name)
    print ('Price: $' + str(item.price))
    total += item.price

  print ('Total (before tax): '+ str(round(total,2)))
  checkormen = int(input('Would you like to 1. Checkout or \n2. Return to the menu: '))
  if checkormen == 1:
    return (co.checkout(cart))
  else:
    return False
              
  
