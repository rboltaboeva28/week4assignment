data = """  john smith - 1990
SARAH CONNOR - 1984
  kylo REN - 1995
LARA croft - 1992"""

with open("raw_users.txt", "w") as f:
    f.write(data)

with open("raw_users.txt", "r") as file, open("clean_profiles.txt", "w") as file2:
    for line in file:
        profile = line.strip().split("-")
        name = profile[0].title()
        year = int(profile[1])
        age = 2025 - year
        file2.write(f"Name: {name} (Age: {age})\n")

