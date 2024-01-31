
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. Top 10 by highest room amount")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        num = int(input("Enter the sequence number "))
        print(apartments[num-1])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def custom_sort(apartment):
            return int(apartment[-1])  # Convert to float assuming prices can have decimals

        # Sort apartments based on the custom function
        sorted_apartments = sorted(apartments, key=custom_sort, reverse=True)

        # Print the top 10 by highest price
        for i in range(10):
            print(sorted_apartments[i])
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def custom_sort(apartment):
            return int(apartment[-1])  # Convert to float assuming prices can have decimals

        # Sort apartments based on the custom function
        sorted_apartments = sorted(apartments, key=custom_sort)

        # Print the top 10 by highest price
        for i in range(10):
            print(sorted_apartments[i])
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        price = int(input("Enter the price "))
        def custom_sort(apartment):
            return int(apartment[-1])
        sorted_apartments = sorted(apartments, key=custom_sort)
        filtred_apartments = []
        for apartment in sorted_apartments:
            if int(apartment[-1]) < price:
                filtred_apartments.append(apartment)
        print(filtred_apartments[:20])
        pass
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        price = int(input("Enter the price "))
        def custom_sort(apartment):
            return int(apartment[-1])
        sorted_apartments = sorted(apartments, key=custom_sort)
        filtred_apartments = []
        for apartment in sorted_apartments:
            if int(apartment[-1]) > price:
                filtred_apartments.append(apartment)
        print(filtred_apartments[:20])
        pass

    elif choice == '6':
        def custom_sort(apartment):
            return int(apartment[-5])  # Convert to float assuming prices can have decimals

        # Sort apartments based on the custom function
        sorted_apartments = sorted(apartments, key=custom_sort, reverse=True)

        # Print the top 10 by highest price
        for i in range(10):
            print(sorted_apartments[i])
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")
