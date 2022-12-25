# pp 156  

from shapely.geometry import Point, Polygon
from geopy.distance import distance
coords = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395,
38.997684), (46.073822, 39.007297), (46.081741, 39.008842)]
poly = Polygon(coords)
cab_26 = Point(46.073852, 38.991890)
cab_112 = Point(46.078228, 39.003949)
cabs = [cab_26,cab_112]
cabs_names = ['cab_26', 'cab_112']
pick_up = Point(46.080074, 38.991289)
entry_point = Point(46.075357, 39.000298)
for i, cab in enumerate(cabs):
  if cab.within(poly):
    dist = distance((pick_up.x, pick_up.y), (cab.x,cab.y)).m
  else:
    dist = distance((cab.x,cab.y), (entry_point.x,entry_point.y)).m + distance((entry_point.x,entry_point.y), (pick_up.x, pick_up.y)).m
  print(cabs_names[i],':', round(dist))
