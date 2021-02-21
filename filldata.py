import json

if __name__ == "__main__":

    with open("clean_trailheads.json", 'r') as f:
        data = json.load(f)

    for line in data:
        print('\n' + line["name"])
        print("-------------------------------")
        for info in line["desc"]:
            print(info)

        print("-------------------------------\n")

        line["exit"] = input("Enter exit: ")
        line["elevation"] = input("Enter elevation: ")
        line["parking"] = input("Enter parking: ")
        line["permit"] = input("Enter permit: ")
        line["facilities"] = input("Enter facilities: ")
        line["notes"] = input("Enter notes: ")

    with open("manually_filled.json", 'w') as f:
        json.dump(line, f, indent=4)