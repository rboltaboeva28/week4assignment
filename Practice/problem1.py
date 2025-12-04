def format_roster(names):
    cleaned_list = []
    for n in names:
        cleaned = n.strip().upper()
        if cleaned != "":
            cleaned_list.append(cleaned)
    return cleaned_list






student_list = [
    "  john doe ",
    "JANE SMITH",
    "   ",
    "alice wonderland",
    "bOb rOsS  "
]

# Run the function
cleaned_roster = format_roster(student_list)
print(cleaned_roster)