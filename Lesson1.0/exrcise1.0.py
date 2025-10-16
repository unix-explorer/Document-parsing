def simple_invoice_parser(file_path: str):
    #Open file and read data
    with open(file_path, 'r')as file:
        file_content = file.read()
    
    #Extract the lines of information
    lines = file_content.split('\n')

    invoice_data: dict= dict()
    items = []
    for line in lines:
        if "Invoice Number:" in line:
            invoice_data["Invoice Number:"]=line.split(':')[-1]
        
        elif 'Invoice Date:' in line:
            invoice_data['invoice_date'] = line.split(': ')[1]
        
        elif 'Vendor:' in line:
            invoice_data['vendor'] = line.split(': ')[1]
        
        elif '-' in line:            
            item = dict()
            item_info = line.split(':')
            item[item_info[0].replace('-','')]=item_info[-1]
            items.append(item)

        elif 'Total:' in line:
            total_str = line.split(': ')[1].replace('$', '')
            invoice_data['total'] = float(total_str)
    
    invoice_data['items']=items
    
    return invoice_data

if __name__=="__main__":
    file_path = input('Enter path:')
    print(simple_invoice_parser(file_path))