import check_cart as cc
import item_class as ic

def checkout(cart):
  total = 0
  for item in cart:
    total+= item.price
  tax =  total*0.06
  print ('Grand Total: ' + str(round((total+tax),2)))
  checkconf = input('Checkout? (yes or no): ')
  if checkconf == 'yes':
    print ('Transferring to payment window')
    return True
  elif checkconf == 'no':
    print ('Returning to store')
    return False