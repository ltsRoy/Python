import csv

with open("check.csv",'r',newline="") as fh:
    wo2=csv.reader(fh,delimiter="\t")
    for i in wo2:
        print(i)
        
        
    """To ensure that empty lines are not included when reading a CSV file in Python, you can add a simple check to skip lines that are empty or contain only whitespace. Here's an example of how you can modify your code to achieve this:

```python
import csv

with open("your_file.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # Check if the row is not empty or contains only whitespace
        if any(cell.strip() for cell in row):
            print(row)  # or do something with the non-empty row
```

In this code:

1. We open the CSV file in read mode ("r").

2. We create a CSV reader object using `csv.reader(file)`.

3. We iterate through each row in the CSV file using a `for` loop.

4. Inside the loop, we use a list comprehension and the `strip()` method to check if any cell in the row contains non-whitespace characters. If any cell contains non-whitespace characters, we consider the row as non-empty.

5. If the row is not empty, you can process it as needed. In this example, I've used `print(row)` to display the non-empty rows. You can replace this with your desired logic.

By using this approach, you can skip empty lines when reading a CSV file and only process rows that contain meaningful data.
    """