import pybaseball as pbl

# https://pypi.org/project/pybaseball/

print(pbl.statcast(start_dt="2024-06-24", end_dt="2024-06-25")['pitch_type'].iloc[0:10])