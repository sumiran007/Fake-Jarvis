import csv

# Open the existing CSV file and read its contents
with open("recordings.csv", "r", newline="") as recordings:
    reader = csv.DictReader(recordings)
    rows = list(reader)  # Convert the reader to a list of rows (dictionaries)
format = input("What should I name the files as?")
# Modify the "File Name" column in each row
for i, row in enumerate(rows, start=1):
    row["File Name"] = f"{format}({i})"

# Write the updated rows back to the CSV file
with open("recordings.csv", "w", newline="") as recordings:
    # Use the same fieldnames as in the original file
    writer = csv.DictWriter(recordings, fieldnames=reader.fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(rows)  # Write all rows
