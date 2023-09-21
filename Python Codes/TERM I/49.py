
fh=open("b.txt","r")

for line in fh:
    x=line.upper() 
    print(x,end='')

fh.close()

"""
In your original code:

```python
fh = open("b.txt", "r")

for line in fh:
    x = fh.readline().upper()
    print(x)

fh.close()
```

The issue is that you're using both a `for` loop to iterate over lines and the `fh.readline()` method within the loop. Here's what's happening step by step:

1. The `for line in fh:` loop reads one line at a time from the file and assigns it to the `line` variable.

2. Inside the loop, you immediately use `fh.readline().upper()`, which attempts to read the next line from the file. This effectively skips every other line because the `for` loop already read a line, and now you're trying to read the next one.

So, in your code, it only processes every second line because of this double reading of lines. To fix this issue, you should either use the `for` loop to read lines and convert them to uppercase, or use the `fh.readline()` approach consistently. Here's the corrected version using the `for` loop:

```python
fh = open("b.txt", "r")

for line in fh:
    x = line.upper()
    print(x)

fh.close()
```

With this code, you'll read and convert all lines from the file to uppercase and print them one by one.


"""