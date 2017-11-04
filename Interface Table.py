import os
main = []
print(os.getcwd())

def ip_address(x):
    for i in main:
        for y in i:
            if y == find:            
                print('Ip address for ' + find + ' is ' + i[1])

if __name__ == "__main__":				
				
	with open("Interface Table.txt","r+") as f:
		content = f.readlines()

		for i in content:
			list1 = i.strip("\t")
			list2 = list1.split()
			main.append(list2)

	find = input("Enter the interface for which you want to find ip address: ")
	ip_address(find)

    
    
    

    
