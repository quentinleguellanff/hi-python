import sys, json, os.path

output = ""
with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    for key in data.keys():
        output += "\n"+"["+key+"]\n"
        for sub_key,value in data[key].items():
            output += sub_key + "=" + value + "\n"

    print(output)
    
with open("output.ini", "w") as outputFile:
	outputFile.write(output)