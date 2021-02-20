from pykml import parser

with open("trailhead.kml", 'w') as f:
    doc = parser.parse(f)

print(doc)