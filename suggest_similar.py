import find_item as fi
import random

def suggest_similar (item,item_list):
  sugg_item_list = []
  for org_key in item.keyword:
    for comp_item in item_list:
      for comp_key in comp_item.keyword:
        if comp_key == org_key:
          sugg_item_list.append(comp_item)

  for sug_items in sugg_item_list:
    if sugg_item_list.count(sug_items) > 1:
      sugg_item_list.remove(sug_items)
  for item in sugg_item_list:
    if sugg_item_list.count(item) > 1:
      sugg_item_list.remove(item)
  return sugg_item_list