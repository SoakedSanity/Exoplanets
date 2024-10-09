# Customizable options for selection of characteristics.

print("This programme is able to find known exoplanet record holders on selected characteristics.")
print("Select one of the following characteristics by typing the correct number:")
print("Type 1 to get exoplanets with the longest orbital period [measured in days]")
print("Type 2 to get the most massive exoplanets [measured in Earth mass units]")
print("Type 3 to get exoplanets with the largest eccentricity (the most elongated exoplanetary orbits)")
print("Type 4 to get exoplanets, which are the furthest from Earth by distance [measured in parsecs]")

char = 0
while char < 1 or char > 4:
    char = int(input())
    if char < 1 or char > 4:
        print("You must select one of the listed variants! There will be more options in the future!")

iter = int(input("Now select how many exoplanet record holders you want to see: "))

if char == 1:
    print("Finding exoplanets with the longest orbital period...")
if char == 2:
    print("Finding the most massive exoplanets...")
if char == 3:
    print("Finding exoplanets with the largest eccentricity...")
if char == 4:
    print("Finding exoplanets, which are the furthest from Earth by distance...")

# Excluding all unnessesary data.

file1 = open('ExoplanetDataset/Exo_Cut.txt', "r")
content = file1.readlines()
file1.close()

names = []
values = []
for s in content:
    s1 = s.split(", ")
    names.append(s1[0])
    values.append(float(s1[char*2-1]))

values, names = zip(*sorted(zip(values, names)))

# print(names)
# print(values)

label = [['Orbital period: ', ' days.'], ['Mass: ', ' Earth masses.'], ["Eccentricity: ", "3"], ["Distance: ", " parsecs."]]
already_listed = []

x = 0
number = 1
while len(already_listed) < iter:
    if names[-1-x] not in already_listed:
        already_listed.append(names[-1-x])
        print("------------------------------------------------")
        print("Exoplanet #" + str(number) + ": " + str(names[-1-x]))
        print(label[char-1][0] + str(values[-1-x]) + label[char-1][1])
        number+=1
    x += 1