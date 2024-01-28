import pathlib

files= ["1.txt", "2.txt", "3.txt", "4.txt"]

if __name__ == "__main__":
    for i, file_path in enumerate(files):
        path = pathlib.Path.joinpath(pathlib.Path.cwd(), files[i])
        with open(path, "r") as f:
            print(f.read())
