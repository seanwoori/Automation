import pathlib

if __name__ == "__main__":
    # Joining the cwd path with the filename
##    filepath = pathlib.Path.joinpath(pathlib.Path.cwd(), '1.txt')
##    print("filepath is:\n", filepath)
##    print()
##
##    with open(filepath, "r") as f:
##        print(f.read())
##    print(pathlib.Path.cwd())

    # Search for all files in the folder with a certain extension
    # get the path with Path
    current_path = pathlib.Path('.')

    # define the file extension pattern
    filePattern = "*.py"

    for Patternfile in current_path.glob(filePattern):  
        print(Patternfile)
        with open(Patternfile, "r") as f:
            print("Opened", Patternfile, "succefully")

