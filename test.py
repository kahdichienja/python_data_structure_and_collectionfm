datatItems = {
    "category":{
        "type":[
            {
                "name": "Dog",
                "price": 15,
            },
            {
                "name": "Cat",
                "price": 15,
            },
            {
                "name": "Elephant",
                "price": 15,
            },
            {
                "name": "Owl",
                "price": 15,
            },
            {
                "name": "Bear",
                "price": 15,
            },
        ],
        "colours":[
            {
                "name": "Green",
                "price": 0,
            },
            {
                "name": "Brown",
                "price": 0,
            },
            {
                "name": "Yellow",
                "price": 0,
            },
            {
                "name": "Pink",
                "price": 0,
            },
            {
                "name": "Blue",
                "price": 0,
            },
            {
                "name": "Violet",
                "price": 0,
            },
            {
                "name": "Orange",
                "price": 0,
            },
            {
                "name": "White",
                "price": 0,
            },
        ],
        "Accesspries":[
            {
                "name": "hat",
                "price": 5,
            },
            {
                "name": "Sunglasses",
                "price": 5,
            },
            {
                "name": "Sport Shoes",
                "price": 4,
            },
            {
                "name": "Sandals",
                "price": 2,
            },
            {
                "name": "Outfit - Boy",
                "price": 6,
            },
            {
                "name": "Outfit - Girl",
                "price": 6,
            },
        ]
    }
}

# print(datastore['office']["medical"][0])
# print(datastore['office'].get("law"))
# for item in datastore['office']['medical']:
#     if item.get('use') == "examination" :  
#         print("The {}  rooms now cost {}".format(item.get('use'), item.get('price')))

# item = datastore['office']['parking']



class Datastore:
    # get data from store.
    def get_all_data_from_datastore_type(self):
        category_type = datatItems['category']['type']
        
        for item in category_type:
            # print (f"{item.get('use')}, Price Is:{item.get('price')}")
            print(f"{item.get('name')}")
    # get data from store.
    def get_all_data_from_datastore_colours(self):
        category_colours = datatItems['category']['colours']
        
        for item in category_colours:
            # print (f"{item.get('use')}, Price Is:{item.get('price')}")
            print(f"{item.get('name')}")


    def __str__(self):
        return 'this is datastore instance'

class DatastoreValidator:
    # validation of ['category']['type'] datastore
    def validate_datastore_type(self, args):
        # the switcher returns a list
        switcher = [args for item in datatItems['category']['type'] if item.get('name') == args]
        # checking if argument in switcher list list
        if args in switcher:
            return True
        else:
            print('Invalid Entry')

    # validation of ['category']['colours'] datastore
    def validate_datastore_colours(self, args):
        # the switcher returns a list
        switcher = [args for item in datatItems['category']['colours'] if item.get('name') == args]
        # checking if argument in switcher list list
        if args in switcher:
            return True
        else:
            print('Invalid Entry')
    def __str__(self):
        return 'this is validator instance'


class Customer:
    name = ''
    orders = []
    cart_obj = []
    
    def register_customer_name(self):
        print('Welcome to Bible Buddies. Before we make your own stuffed animal, can you tell me your name?')
        customer_name = input('Enter Your name:\n')
        print(f"Hi {customer_name}")

    def add_baddy_type(self):
        
        baddy_type = input('Enter Buddy Type:\n')
        self.orders.append({"type": baddy_type})
        print(f'cart contains: {len(self.cart_obj)} items')

        return baddy_type

    def add_baddy_color(self, buddy_type):
        baddy_color = input('Enter Color:\n')
        self.orders[0].get(buddy_type)
        self.orders[0].update({"Colours": baddy_color})
        return baddy_color
        
    def add_baddy_acces(self, buddy_type):
        baddy_acc_no = input('Enter The No. Of Accessories:\n')
        self.orders[0].get(buddy_type)
        self.orders[0].update({"Accessories": [{"total": int(baddy_acc_no), "name": ""}]})
        self.cart_obj.append({"oder_name": self.orders})
        print(f'{self.cart_obj}')

        return baddy_acc_no

        
    def __str__(self):
        return 'this is Customer instance'


# 'accessories': [{"total": 3, "name": ""},]

def main():
    
    # class instances
    
    datavalidator = DatastoreValidator()
    datastore = Datastore()
    customer = Customer()
    
    # getnameditem = datastore.get_item_from_datastore('office')    
    
    # validating data from store
    # assert datavalidator.validate_datastore_type('office') == True

    customername = customer.register_customer_name()
    customername
    bbuddiescount = int(input('How many Bible Buddies do you want today?\n'))
    
    if bbuddiescount > 3:
        print('bbuddiescount greater than required')
        

    # while bbuddiescount < 3: TODO: implement this

    # getting all data in store
    print(f'For Bibble buddy 1, what type would you like:')
    alldatastore = datastore.get_all_data_from_datastore_type()
    buddytype = customer.add_baddy_type()
    # print(buddytype)
    # assert 
    datavalidator.validate_datastore_type(buddytype) 
    # == True

    print(f'what colour will this one be:')
    # get all buddycolor
    buddycolor = datastore.get_all_data_from_datastore_colours()
    addbuddycolor = customer.add_baddy_color(buddytype)

    # addbuddycolor
    # assert 
    datavalidator.validate_datastore_colours(addbuddycolor)
    #  == True

    print(f'How many accessories - you can choose 0 t0 4:')
    buddyaccess = customer.add_baddy_acces(buddytype)
    # buddyaccess



main()
# ////budy acces loop index.