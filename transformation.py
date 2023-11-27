import pyproj
from pyproj import Transformer


lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

t1 = Transformer.from_crs(wgs84, lv95)
t2 = Transformer.from_crs(lv95, wgs84)

r1 = t1.transform(47.53487677458141, 7.641955113723078)
#print(r1) # 2615310.591188584, 1264924.920298897

r2 = t2.transform(2615310.591188584, 1264924.920298897)
#print(r2) # (47.5348767850414,  7.641955121168162)

start_lng = 7.641955113723078
start_lat = 47.53487677458141

end_lng = -122.47864020149932
end_lat = 37.81951340907846

g = pyproj.Geod(ellps='WGS84')

r = g.npts(start_lng, start_lat, end_lng, end_lat, 100)
#print(r)

r2 = []
for x in r:
    r2.append([x[0],x[1]])


alles = list([[start_lng, start_lat]] + r2 + [[end_lng, end_lat]])

print(alles)

geojson = f"""{{ "type": "Feature", "geometry":
   {{ "type": "MultiPoint", "coordinates": {alles} }}, 
   "properties": {{ "about": "Geodätische Linie" }} }} 
"""

file = open("g.geojson", "w", encoding="utf-8")
file.write(geojson)
file.close()

print(geojson)
