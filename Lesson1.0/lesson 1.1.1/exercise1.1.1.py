
with open('practice.txt','w')as file:
    file.write("""Invoice Number: INV-2024-001
        Invoice Date: January 15, 2024  
        Vendor: Office Supplies Co.
        Items:
        - Pens: $25.00
        - Paper: $45.50
        - Staplers: $32.99
        Total: $103.49"""
    )
with open('practice.txt','r')as file:
    lines = file.readlines()
    print(len(lines))