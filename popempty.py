import json

if __name__ == "__main__":
    with open("manually_filled.json", 'r') as f:
        data = json.load(f)

        for line in data:
            line.pop('facilites', None)

    with open("final_trailheads.json", 'w') as f:
        json.dump(data, f, indent=4)
