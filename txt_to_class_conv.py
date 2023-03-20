import item_class as ic

def txt_to_class_conv(txtfile):
  item_list = []
  fi = open(txtfile, 'r')
  lines = fi.readlines()
  for item in lines:
    item_data = item.split(',',4)
    #turning the keywords string back into a list
    #print (item_data)
    name = item_data[0]
    desc = item_data[1]
    price = float(item_data[2])
    inv = int(item_data[3])
    keywords = item_data[4]
    keywordlist = keywords.strip('][').split(', ')
    keyword = []
    for word in keywordlist:
      keyword.append(word)
    item_class = ic.Product(name,desc,price,inv,keyword)
    #print (item_class)
    item_list.append(item_class)
  return item_list