import csv
from pathlib import Path

def basic_csv_creation():
    """Show how to create a csv file"""
    sample_data = [
        ['Name', 'Email', 'Age', 'City'],
        ['John Doe', 'john@email.com', '30', 'New York'],
        ['Jane Smith', 'jane@email.com', '25', 'London'],
        ['Bob Johnson', 'bob@email.com', '35', 'Tokyo']
    ]

    with open("sample_csv.csv",'w')as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)

    print("Basic csv file created.")

def simple_csv_reader(file_path: str):
    """Show different ways of reading csv files."""
    
    print('\n'+"="*50)
    print("Reading CSV Files Different Methods.")
    print('\n'+"="*50)

    #Method 1 csv reader (basic)
    print("Using CSV Reader:")
    with open(file_path,'r')as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader):
            print(f"Row: {row_num} Data: {row} ")

    #Method 2: csv Dict-Reader(Recommended)
    print("\n\nUsing Csv Dict-Reader:")
    with open(file_path,'r')as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    
    #Method 3: Reading all data at once
    print("\n\nReading all data to a list:")
    with open(file_path,'r')as file:
        reader = csv.DictReader(file)
        all_data = list(reader)
        print(f"Total Records: {len(all_data)}")
        print(f"First Row: {all_data[0]}")



if __name__=="__main__":
    simple_csv_reader()