import csv

with open('Team_Data/Sheet2.csv', newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    data = list(reader)[1:]

new_data = []

catcher = None
pitcher = None
hitter = None
pitch = 0
balls = 0
strikes = 0
outs = 0
b1 = 0
b2 = 0
b3 = 0

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
    
    thrown = True if row[4] == "TRUE" else False
    swing = True if row[5] == "TRUE" else False

    new_row.append(catcher)
    new_row.append(pitcher)
    new_row.append(hitter)
    new_row.append(pitch)
    new_row.append(1 if thrown else 0)
    new_row.append(1 if swing else 0)
    new_row.append(balls)
    new_row.append(strikes)
    new_row.append(outs)
    new_row.append(b1)
    new_row.append(b2)
    new_row.append(b3)

    #new_row = (catcher, pitcher, hitter, pitch, 1 if thrown else 0, 1 if swing else 0, balls, strikes, outs, b1, b2, b3)

    if thrown or swing:
        strikes += 1
    else:
        balls += 1
    
    if strikes > 2:
        strikes = 2
    
    if row[6] == "Out":
        outs += 1
        balls = 0
        strikes = 0
    
    if outs == 3:
        outs = 0
    
    if row[6] == "Hit" or row[6] == "Walk":
        balls = 0
        strikes = 0

    b1 = 1 if row[7] == "TRUE" else 0
    b2 = 1 if row[8] == "TRUE" else 0
    b3 = 1 if row[9] == "TRUE" else 0

    new_data.append(new_row)

with open("Team_Data/parsed_sheet2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Catcher", "Pitcher", "Hitter", "Pitch", "Swing", "Strike", "Balls", "Strikes", "Outs", "1B", "2B", "3B"])
    writer.writerows(new_data)

with open("Team_Data/parsed_total.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_data)