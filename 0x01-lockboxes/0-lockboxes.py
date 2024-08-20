#!/usr/bin/python3

def canUnlockAll(boxes):
  opened_boxes = [0]
  all_keys = []

  for i in range(len(boxes)):
    if i in opened_boxes:
      keys_in_box = boxes[i]
      map(lambda x: all_keys.append(x), keys_in_box)
      for k in keys_in_box:
        # all_keys.append(boxes[k])
        map(lambda x: all_keys.append(x), boxes[k])
  
  return(all_keys)


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
