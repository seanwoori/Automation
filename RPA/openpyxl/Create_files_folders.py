import os
# Get the path
path = os.getcwd()  

if __name__ == "__main__":
    content = ["This", "is", "a", "test", "file"]
    with open("testfile.txt", "w") as f: 
        for word in content: 
            f.write(word+"\n")

    with open("testfile.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(line)
            try:  
                os.mkdir(path+"\\"+line)
            except OSError:  
                continue
                #print("Cannot create folder", path+"\\"+line)
            finally:
                print("Finishing up...")
            

