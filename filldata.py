import json

if __name__ == "__main__":

    with open("clean_trailheads.json", 'r') as f:
        data = json.load(f)

    for idx, line in enumerate(data):
        print('\n' + line["name"])
        print("----------- %d / %d -----------" % (idx, len(data)))
        for info in line["desc"]:
            print(info)

        print("-------------------------------\n")

        line["exit"] = input("Enter exit: ")
        line["elevation"] = input("Enter elevation: ")
        line["parking"] = input("Enter parking: ")
        line["permit"] = input("Enter permit: ")
        line["facilities"] = input("Enter facilities: ")
        line["notes"] = input("Enter notes: ")
        line["desc"] = ""

    with open("manually_filled.json", 'w') as f:
        json.dump(data, f, indent=4)
