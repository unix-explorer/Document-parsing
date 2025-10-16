import csv
from csv_parser import simple_csv_reader

def creating_challenging_csv():
 # CSV with different delimiters
    semicolon_data = [
        ['Product;Price;Quantity;Category'],
        ['Laptop;999.99;10;Electronics'],
        ['Book;19.99;50;Education'],
        ['Phone;699.99;25;Electronics']
    ]

    with open("practice2.csv",'w')as file:
        for line in semicolon_data:
            file.write(line[0]+'\n')
    
# CSV with quotes and special characters
    complex_data = [
        ['Name', 'Description', 'Price'],
        ['Basic Item', 'Simple product', '19.99'],
        ['Special, Item', 'Product, with commas', '29.99'],
        ['"Quoted" Item', 'Product with "quotes"', '39.99']
    ]
    with open('practice3.csv','w')as file:
        writer = csv.writer(file)
        writer.writerows(complex_data)

creating_challenging_csv()
if __name__=="__main__":
    while True:
        file_path = input("Enter file path:")
        simple_csv_reader(file_path)