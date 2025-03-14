import csv

with open('Team_Data/Sheet1.csv', newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    data = list(reader)[1:]

new_data = []

catcher = None
pitcher = None
hitter = None
pitch = 0

name_correction = {
    "ethan d": "dean",
    "jon k": "kozak",
    "patty": "patrick",
    "jon": "kozak",
    "ricker": "riecker",
    "b.burton": "b. burton"

}

for row in data:
    new_row = []

    if row[0] != "":
        name = row[0].lower().rstrip()
        if name in name_correction:
            catcher = name_correction[name]
        else:
            catcher = name
    if row[1] != "":
        name = row[1].lower().rstrip()
        if name in name_correction:
            pitcher = name_correction[name]
        else:
            pitcher = name
    if row[2] != "":
        name = row[2].lower().rstrip()
        if name in name_correction:
            hitter = name_correction[name]
        else:
            hitter = name

    if row[3] == "Slider" or row[3] == "Curveball" or row[3] == "Changeup":
        pitch = 1
    else:
        pitch = 0
    
    new_row.append(catcher)
    new_row.append(pitcher)
    new_row.append(hitter)
    new_row.append(pitch)
    new_row.append(1 if row[4] == "TRUE" else 0)
    new_row.append(1 if row[5] == "TRUE" else 0)
    new_row.append(int(row[6]) if row[6] != "" else 0)
    new_row.append(int(row[7]) if row[7] != "" else 0)
    new_row.append(int(row[8]) if row[8] != "" else 0)
    new_row.append(1 if row[9] == "TRUE" else 0)
    new_row.append(1 if row[10] == "TRUE" else 0)
    new_row.append(1 if row[11] == "TRUE" else 0)

    new_data.append(new_row)

with open("Team_Data/parsed_sheet1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Catcher", "Pitcher", "Hitter", "Pitch", "Swing", "Strike", "Balls", "Strikes", "Outs", "1B", "2B", "3B"])
    writer.writerows(new_data)

with open("Team_Data/parsed_total.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Catcher", "Pitcher", "Hitter", "Pitch", "Swing", "Strike", "Balls", "Strikes", "Outs", "1B", "2B", "3B"])
    writer.writerows(new_data)