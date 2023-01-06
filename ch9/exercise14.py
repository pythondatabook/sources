# pp 154

from shapely.geometry import Point, Polygon

coords1 = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395,
38.997684), (46.073822, 39.007297), (46.081741, 39.008842)]

coords2 = [(40.102991, 35.977384), (40.065489, 35.977599), (40.109395,
35.997684), (40.073822, 36.007297), (40.081741, 36.008842)]

poly1 = Polygon(coords1)
poly2 = Polygon(coords2)

cab_26 = Point(46.073852, 38.991890)
cab_112 = Point(46.078228, 39.003949)
pick_up = Point(46.080074, 38.991289)

cabs_dict ={}
polygons = {'poly1': poly1, 'poly2': poly2}
cabs = {'cab_26': cab_26, 'cab_112': cab_112}
for poly_name, poly in polygons.items():
  cabs_dict[poly_name] = []
  if pick_up.within(poly):
    for cab_name, cab in cabs.items():
      if cab.within(poly):
        cabs_dict[poly_name].append(cab_name)  
    break

from geopy.distance import distance
dists = {}
for cab in next(iter(cabs_dict.values())):
  dists[str(cab)] = int(distance((pick_up.x, pick_up.y), (cabs[cab].x, cabs[cab].y)).m)

max(dists, key=dists.get)
