import csv


CONST_PRODUCT_COLUMN = 0
CONST_PRICE_COLUMN = 1



CONST_PRODUCT_TO_PRESERVE = 'pink morsel'
CONST_PRODUCT_COLUMN = 0
CONST_PRICE_COLUMN = 1
CONST_PRODUCT_QUANTITY = 2
CONST_DATE = 3
CONST_REGION = 4
    
def write_row(row):
    writer.writerow(row)



file_1 = '/home/jungle/quantium-starter-repo-main/data/daily_sales_data_0.csv'
file_2 = '/home/jungle/quantium-starter-repo-main/data/daily_sales_data_1.csv'
file_3 = '/home/jungle/quantium-starter-repo-main/data/daily_sales_data_2.csv'
CONST_OUTPUT_FILE = 'tasqas_out2.csv'

with open(CONST_OUTPUT_FILE, mode = 'w') as out_file:
    writer = csv.writer(out_file)
    
    


    data = 'asfdasfa.csv'
    with open(data) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        
        write_row(['product','sales','date','region'])
        next(csv_reader)
    
        
        for row in csv_reader:
            price = int(float((row[CONST_PRICE_COLUMN])[1:]))
            quantity = int(row[CONST_PRODUCT_QUANTITY])
            sales = (price*quantity)
            print("price: " + str(price))
            print("quantity: " + str(quantity))
            print("sales: " + str(sales))
            
            
            out_row = [row[CONST_PRODUCT_COLUMN], sales , row[CONST_DATE], row[CONST_REGION]]
            write_row(out_row)


    

    


