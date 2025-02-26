import sys

n = len(sys.argv)
if n < 2:
    print("Please input the file path")
    quit()
try:
    if sys.argv[1].lower() == "help":
        print(
            "Usage:\npython DictSubset.py <file_path> <min_length (inclusive)> <max_length (inclusive)> <input_file_delimiter> <output_file_delimiter>"
        )
        print("This tool replaces the original file. Please keep a backup if important")
        quit()
    idelim = sys.argv[4]
    if idelim == "\\n":
        idelim = "\n"
    elif idelim == "\\t":
        idelim = "\t"
    elif idelim == "\\w":
        idelim = " "

    odelim = sys.argv[5]
    if odelim == "\\n":
        odelim = "\n"
    elif odelim == "\\t":
        odelim = "\t"
    elif odelim == "\\w":
        odelim = " "
    outp = ""
    file = open(sys.argv[1], "r")
    content = file.read().split(idelim)
    largest = ""
    smallest = "0" * int(sys.argv[3])
    for i in content:
        if len(i.strip()) <= int(sys.argv[3]) and len(i.strip()) >= int(sys.argv[2]):
            outp += i + odelim
            if len(i) > len(largest):
                largest = i
            if len(i) < len(smallest):
                smallest = i
    file.close()
    file = open(sys.argv[1], "w")
    file.write(outp)
    file.close()
    print("Largest word: " + largest + " (" + str(len(largest)) + " characters)")
    print("Smallest word: " + smallest + " (" + str(len(smallest)) + " characters)")
except Exception as e:
    print(e.with_traceback)
    print("Please input the correct parameters")
