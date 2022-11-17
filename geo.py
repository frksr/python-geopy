from geopy.distance import great_circle as GRC

kadikoy = (41.010160,29.014801)
abd = (23.314265, -102.297463)
distance = GRC(kadikoy,abd)

print("The distance between kadikoy and abd is:", distance) 

