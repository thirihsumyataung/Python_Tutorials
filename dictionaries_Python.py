
customer = {
    "name" : "John Smith",
     "age" : 30 ,
     "is_varified" : True
}
customer['name'] = 'Jack Smith'
#print(customer.get("name")) # get (key ) OUTPUT will be NONE if there is no key

#we can add new keys value easily
customer["birthday"] = "Jan 1 1998"
print(customer["birthday"])

