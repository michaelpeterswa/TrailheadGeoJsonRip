import json

if __name__ == "__main__":
    with open("finals2.json", 'r') as f:
        data = json.load(f)

        for line in data:
            line["name"] = line["name"].title()

    with open("finals3.json", 'w') as f:
        json.dump(data, f, indent=4)
