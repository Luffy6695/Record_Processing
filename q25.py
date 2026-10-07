import sys
import json

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as file:
    records = json.load(file)

report = {
    "input_count": len(records)
}

with open(output_file, "w") as file:
    json.dump(report, file, indent=4)

print("Report generated successfully")
