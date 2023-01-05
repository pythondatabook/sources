# pp 34 - 35 

l = [
	 {
	  "name": "photo1.jpg",
	  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
	 },
	 {
	  "name": "photo2.jpg",
	  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
	 },
	 {
	  "name": "photo3.jpg",
	  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
	 },
	 {
	  "name": "photo4.jpg",
	  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
	 }
	]
  
def intersection(lst1, lst2):
  return "_".join([value for value in lst1 if value in lst2]) 
  
photo_groups = {}
for i in range(0, len(l)-1):
  for j in range(i+1,len(l)):
    lst = intersection(l[i]["tags"],l[j]["tags"])
    if lst: 
      k = photo_groups.setdefault(lst, list((l[i]["name"], l[j]["name"])))  
print(photo_groups)
