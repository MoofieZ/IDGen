def findNextID(starting_id):
    current_id = starting_id + 1
    while True:
        String = str(current_id)
        products = [int(String[i]) * (8 - i) for i in range(8)]
        total_sum = sum(products)
        if total_sum % 11 == 0:
            return current_id
        current_id += 1

while True:
    initial_id = input("Input Valid Lasallian ID: ")
    quantity = input("Number of ID Numbers to Generate: ")
    current_id = int(initial_id)  
    for i in range(int(quantity)):
        current_id = findNextID(current_id)  
        print(current_id)