from streetview import search_panoramas
from streetview import get_streetview
from streetview import get_panorama
panos = search_panoramas(lat = 41.011782, lon = -78.435571)
first = panos[-1].pano_id
second = panos
'''
print(first)
image = get_streetview(
    pano_id = first,
    api_key = "AIzaSyArqq6R88oxCc9rJx5RdYKP4BwEPyJNuoo"
)

image.save("image2.jpg", "jpeg")
'''
image = get_panorama(pano_id = first)
image.save("pano.jpg", "jpeg")
