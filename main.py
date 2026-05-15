#Create file in specific location
# with open("/home/home/Desktop/Python/data.txt", "w") as file:
#     file.write("File created")

#Code to read the file
with open("/home/home/Desktop/Python/data.txt", "r") as file:
    content = file.read()
    print(content)

#Code to append to the file
# with open("/home/home/Desktop/Python/data.txt", "a") as file:    file.write("\nThis is second line in file handling")

