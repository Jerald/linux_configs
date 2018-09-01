#!/usr/bin/python3

import os.path

# Defines the character which separates our fields
sepVar = ","

# Change this if you want to convert a list from a old seperator to a new one.
# Defines what separator is used for loading the file.
retroSepVar = ","

# The default headers for a new file
defaultHeaders = ["FileName", "Category", "Link Path", "Prefix"]

# Helper functions

def readWholeFile():
    tempTable = []

    line = fileobj.readline()
    while line != "":
        splitLine = line.split(retroSepVar)

        # Remove trailing newline on last element
        splitLine[-1] = splitLine[-1][:-1]

        tempTable.append(splitLine)
        line = fileobj.readline()

    return tempTable


# Operation functions

def headersFunc(uInput):
    output = ""
    for header in splitHeaders:
        output += header + " | "

    # Python string comprehension is weird...
    output = output[:-3]

    print("Headers: " + output)
    return

def add(uInput):
    entry = []

    for header in splitHeaders:
        try:
            entry.append(input(header + ": "))
        except (EOFError, KeyboardInterrupt):
            exit()

    table.append(entry)

    view()
    return

def view(uInput=""):
    if len(uInput) == 2 and uInput[1] == "raw":
        print(splitHeaders)

        for entry in table:
            print(entry)

        return

    print()
    #Dirty Hack (tm). I modified the tabulate source to use the arguments as specified by that symbol table
    exec(open(".tabulate.py").read(), {"mArg1": table, "mArg2": splitHeaders, "mArg3": "orgtbl"})
    print()
    return

def save(uInput):
    fileobj.seek(0)
    fileobj.truncate()
    fileobj.write(headers + "\n")

    for entry in table:
        fileobj.write(sepVar.join(entry) + "\n")

    print("Saved table to file!")
    return

def remove(uInput):
    if len(uInput) < 2:
        print("Wrong number of args. Usage: remove <file_name>")

    for entry in table:
        # Removal argument matches first field, aka file name
        if entry[0] == uInput[1]:
            table.remove(entry)
            view()
            return

    print("No matching file found for: " + uInput[1])

    return

def new(uInput):
    global table, headers, splitHeaders

    table = []

     # Write the basic headers to the file
    headers = sepVar.join(defaultHeaders)
    fileobj.write(headers + "\n")

    splitHeaders = headers.split(sepVar)

    view()
    return

def otherwise(uInput):
    print("Command not found: " + " ".join(uInput))
    return

# Actual code

fileName = "filelist"

if os.path.isfile("./" + fileName):
    fileobj = open(fileName, "r+")
else:
    fileobj = open(fileName, "w+")

headers = fileobj.readline()

# Remove trailing newline
headers = headers[:-1]

if headers == "":
    print ("No (or empty) filelist found, starting from scratch...")

    # Write the basic headers to the file
    headers = sepVar.join(defaultHeaders)
    fileobj.write(headers + "\n")

splitHeaders = headers.split(sepVar)

# Read the whole file into a variable
table = readWholeFile()

# Main loop
userInput = ""
while True:
    # Actually get new user input
    try:
        userInput = input("> ")
    except (EOFError, KeyboardInterrupt):
        exit()

    if userInput == "exit":
        exit()

    switchDict = {
        "headers": headersFunc,
        "add": add,
        "view": view,
        "save": save,
        "remove": remove,
        "new": new
    }

    userInput = userInput.split(" ")

    if userInput[0] in switchDict:
        switchDict[userInput[0]](userInput)
    else:
        otherwise(userInput)
