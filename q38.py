# 38. Following is the structure of each record in a data file named “PRODUCT.DAT”.
# {"prod_code": value, "prod_desc": value, "stock": value}
# The values for prod_code and prod_desc are strings and the value for stock is an integer.
# Write a function in Python to update the file with a new value of stock. The stock and the product_code,
# whose stock is to be updated, are to be inputted during the execution of the function.
import pickle as pk
def update_record(new_code, new_desc, new_stock):
    with open("product.dat","rb+") as prod_info:
        data = pk.load(prod_info)
        #for record in data:
        data["prod_code"] = new_code 
        data["prod_desc"] = new_desc 
        data["stock"] = new_stock 
        pk.dump(data,'product.dat')
    return 

def main():
    update_record(1424,"lol",555)


if __name__ == "__main__":
    main()


# with open("result.dat", "wb") as f:
#     pickle.dump(record, f)
#     print("record addded :))")
