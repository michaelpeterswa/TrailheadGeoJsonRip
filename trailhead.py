import geojson
import re
import json

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '~', text)

def remove_urls(text):
    """Remove urls from a string"""
    clean = re.compile('https?://\S+?(?=~)')
    return re.sub(clean, '~', text)

def listify(text):
    clean = text.lstrip('~').split('~')
    clean = [i for i in clean if i]
    return clean

if __name__ == "__main__":
    
    with open("trailhead.geojson", 'r') as f:
        data = geojson.load(f)

    features = data["features"]

    clean = list()

    for feature in features:
        name = feature["properties"]["name"]
        description = feature["properties"]["description"]

        description = remove_html_tags(description)
        description = remove_urls(description)
        description = listify(description)

        coordinates = feature["geometry"]["coordinates"][:-1]
        coordinates.reverse()

        clean.append({
                        "name": name, 
                        "desc": description, 
                        "exit": "",
                        "elevation": "",
                        "parking": "",
                        "permit": "",
                        "facilites": "",
                        "notes": "",
                        "coords": coordinates
                        })

    with open("clean_trailheads.json", 'w') as f:
        json.dump(clean, f, indent=4)