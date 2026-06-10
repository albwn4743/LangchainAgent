from knowledge import bank_details,bank_data

while True:
    n=input()
    if n.lower() == 'exit':
        break
    a = bank_details(n)

    print(a)