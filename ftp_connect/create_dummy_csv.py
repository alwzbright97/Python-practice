import csv
import random

for i in range(100):
    print(f"[Start] Write dummy_{i:02d} csv file")
    with open(f"dummy_{i:02d}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Location'])
        for j in range(1, 10001):
            writer.writerow([f'Person_{i}', random.randint(20, 50), f'Location_{random.randint(1, 10)}'])
    print(f"[Finish] Wrote dummy_{i:02d} csv file")