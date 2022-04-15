import re

f = open("animals_list_raw.txt")

filtered_animals = []

for line in f.readlines():
    print(line)
    animal_ = line.split()[0]
    if animal_.capitalize() ==animal_ and len(animal_)>1:
        filtered_animals.append(re.sub('\[[^>]+\]', '', animal_))
    

print(filtered_animals)

f.close()
f2 = open("animals_list.txt", "w+")

f2.write(str(filtered_animals))
