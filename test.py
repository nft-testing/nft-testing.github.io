
import os
import json

text = ''

directory = os.fsencode('metadata_2')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json") and filename != "collection.json":
        with open('metadata_2/'+filename, "r") as json_file:
            print(filename)
            data = json.load(json_file)
            print(data)
            data['attributes'] = []
            data['image'] = "https://nft-testing.github.io/metadata/lock.png"

        with open('metadata_2/'+filename, "w") as json_file:

            json_file.write(json.dumps(data))

    else:
        continue

print(text)

with open('base.txt', "w") as file:
    file.write(text)