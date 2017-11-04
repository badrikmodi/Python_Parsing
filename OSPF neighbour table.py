import os
main = []
print(os.getcwd())

if __name__ == "__main__":
    with open("ospf neighbour table.txt","r+") as f:
        content = f.readlines()

    for i in content:
        spaces = i.strip()
        create_list = spaces.split()
        main.append(create_list)

    for i in main:
        for j in i:
            if j == "FULL/BDR":
                print(i[0] + " : This is my neighbour")
            
