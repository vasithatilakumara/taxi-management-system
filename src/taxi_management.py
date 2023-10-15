import sys
import os
"""
Overview
--------
During the process of designing and developing this program, careful consideration 
was given to its purpose and functionality. The initial step involved understanding 
the specific requirements and objectives of the program. This included defining the 
problem statement and identifying the core featuresa and their related classes in the program. 
Once the requirements were clear, then began the design process by outlining 
the high-level structure of the code and the main components it would consist of.

The next step was breaking down the problem into smaller, manageable tasks. This helped 
in creating a roadmap for development and allowed for a more organized approach. As I 
started writing the code, I focused on implementing class and there method to ensure 
that the program's components were cohesive and easy to maintain. The design also considered 
potential future expansions, allowing for flexibility in adding new features without major 
code rewrites.

However, there were few challenges specially in the CREDIT level and HD level. The part where program support both IDs and name 
is when things got complicated. Challenging part was to realising the best format for information storing in the record class since 
it will be a intrigal part in the program. After careful analysis, it was decided to handle all the informations from the txt files 
and store them in spearate list for each information type. 
[i.e: customer_ID = [], customer_name = [], customer_type = [], discount_rate = [], threshold = []] 
"""

'''
This class serves as the central data store for customer,location, services, packages and rate type information, and 
it provides methods to read data from files, search for specific data, and list the existing data. 
'''
class Records:
    customer_name = []
    customerID = []
    location_id = []
    locations = []
    rate_id = []
    rate_type = []
    rate_price = []
    customerType = []
    discount_rate = []
    threshold = []
    service_name = []
    service_id = []
    service_price = []
    package_id = []
    package_name = []
    package_services =[]
    bookings = []

    def __init__(self):
        pass
      
    @staticmethod
    def read_customers(name): 
        splitValue =[]       
        fname = name
        try:
            f = open(fname, 'r')

            with open(fname,'r') as f:
                for line in f.readlines():
                    for x in line.strip().split(","):
                        splitValue.append(x.strip())    
                    # create pre define list of customer name using the values from customer.txt           
                    Records.customerID.append(splitValue[0])
                    Records.customer_name.append(splitValue[1])
                    Records.customerType.append(splitValue[2])
                    Records.discount_rate.append(splitValue[3])

                    if len(splitValue) <= 4:
                        Records.threshold.append('0')
                    else:
                        Records.threshold.append(splitValue[4])
                    splitValue =[] 
            f.close()

        except OSError:
            print (f"Could not open/read file: {fname}")
            for i in range(0,100000000):
                pass
            sys.exit()

        
        return Records.customerID,Records.customer_name,Records.customerType,Records.discount_rate,Records.threshold  
      
    @staticmethod
    def read_locations(name):
        splitValue =[] 
        fname = name
        try:
            f = open(fname, 'r')
            
            with open(fname,'r') as f:
                # reader = f.readlines()
                for line in f.readlines():
                    for x in line.strip().split(","):
                        splitValue.append(x.strip())  
                    Records.location_id.append(splitValue[0])
                    Records.locations.append(splitValue[1])
                    splitValue =[] 
            f.close()
        except OSError:
            print (f"Could not open/read file: {fname}")
            for i in range(0,100000000):
                pass
            sys.exit()

        
        return Records.location_id,Records.locations    

    @staticmethod
    def read_rates(name):
        splitValue=[]
        fname = name
        try:
            f = open(fname, 'r')

            with open(fname,'r') as f:
                for line in f.readlines():
                        for x in line.strip().split(","):
                            splitValue.append(x.strip())    
                        # create pre define list of rate types using the values from customer.txt           
                        Records.rate_id.append(splitValue[0])
                        Records.rate_type.append(splitValue[1])
                        Records.rate_price.append(splitValue[2])
                        splitValue =[] 
            f.close()
        except OSError:
            print (f"Could not open/read file: {fname}")
            for i in range(0,100000000):
                pass
            sys.exit()
        
        return Records.rate_id,Records.rate_type, Records.rate_price  
    
    @staticmethod
    def read_serviceORpackages(name):
        splitValue=[]
        fname = name
        try:
            f = open(fname, 'r')
            with open(fname,'r') as f:
                for line in f.readlines():
                        for x in line.strip().split(","):
                            splitValue.append(x.strip())    
                        # create pre define list of rate types using the values from customer.txt           
                        if 'S' in splitValue[0]:
                            Records.service_id.append(splitValue[0])
                            Records.service_name.append(splitValue[1])
                            Records.service_price.append(splitValue[2])
                        elif 'P' in splitValue[0]:
                            Records.package_id.append(splitValue[0])
                            Records.package_name.append(splitValue[1])
                            Records.package_services.append(splitValue[2:len(splitValue)])
                        splitValue =[] 
            f.close()
        except OSError:
            print (f"Could not open/read file: {fname}")
            for i in range(0,100000000):
                pass
            sys.exit()
        
        return Records.service_id, Records.service_name, Records.service_price, Records.package_id,Records.package_name, Records.package_services
    
    @staticmethod
    def read_bookings(name):
        splitValue=[]
        fname = name
        try:
            f = open(fname, 'r')

            with open(fname,'r') as f:
                for line in f.readlines():
                        for x in line.strip().split(","):
                            splitValue.append(x.strip())    
                        # create pre define list of rate types using the values from customer.txt           
                        Records.bookings.append(splitValue)
                        splitValue =[] 
            f.close()
        except OSError:
            print (f"Could not open/read file: {fname}")
                    
        return Records.bookings
    
    @staticmethod
    def find_customer(c_value):
        if c_value in Records.customer_name:
            result = c_value
        else:
            result = ""
        return result

    @staticmethod
    def find_location(l_value):
        for i in Records.locations:
            if l_value in i:
                result = i
            else:
                result = ""
        return result

    @staticmethod
    def find_rate(r_value):
        for i in Records.rate_type:
            if r_value in i:
                result = i
            else:
                result = ""
        return result
    
    @staticmethod
    def find_service_packages(s_value):
        i = ""
        for i in Records.service_name, Records.package_name, Records.service_id, Records.package_id:
            if s_value in i:
                result = i[i.index(s_value)]
        return result

    @staticmethod
    def list_customer():
        for i in zip(Records.customerID,Records.customer_name,Records.customerType,Records.discount_rate,Records.threshold):
            print(', '.join(i))
        
    @staticmethod
    def list_locations():
        for a,b in zip(Records.location_id,Records.locations):
            print(f"{a}, {b}")   
   
    @staticmethod
    def list_rates():
        for a,b,c in zip(Records.rate_id,Records.rate_type,Records.rate_price):
            print(f"{a}, {b}, {c}")     

    @staticmethod
    def list_services():   
        for a,b,c in zip((Records.service_id + Records.package_id),(Records.service_name + Records.package_name),(Records.service_price + Records.package_services)):
            if isinstance(c,list):
                print(f"{a}, {b}, {str(c)[1:-1]}")
            else:
                print(f"{a}, {b}, {c}")   
        
    @staticmethod
    def list_bookings():        
        for i in Records.bookings:
            print(str(i)[1:-1])

'''
The Customer class serves as a base class for representing various types of customers with common attributes and allows 
for customization by subclasses to implement specific behaviors like discounts and displaying customer information.
'''     
class Customer:
    
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name

    def get_discount(self):
        pass  # To be implemented in subclasses

    def display_info(self):
        pass  # To be implemented in subclasses

    @property    
    def get_ID(self):
        return self.__ID
    @property 
    def get_name(self):
        return self.__name

'''
BasicCustomer class is tailored for customers with a fixed discount rate and provides methods to manage and display 
customer information, calculate discounts, and modify the discount rate for all Basic customers.
'''
class BasicCustomer(Customer):
    b_discountRate = 10
    def __init__(self,ID,name):
        super().__init__(ID, name)

    # calculate the discount of the basic customer according to there basic customer discount rate
    def get_discount(self, distance_fee):
        value=0
        if self.get_ID in Records.customerID:
            cus_d = float(Records.discount_rate[Records.customerID.index(self.get_ID)])
        else:
            cus_d = 0
        if BasicCustomer.b_discountRate == (cus_d*100):
            value = (self.b_discountRate / 100) * distance_fee
        elif BasicCustomer.b_discountRate != (cus_d*100):
            value = cus_d * distance_fee
        elif cus_d == 0:
            value = (self.b_discountRate / 100) * distance_fee
        return value

    def display_info(self):
        print("Customer ID:".ljust(20)+str(BasicCustomer.ID))
        print("Customer Name:".ljust(20)+(BasicCustomer.name))
        print("Basic Customer Discount:".ljust(20)+str(BasicCustomer.b_discountRate)+"%")

    def set_discount_rate(self, rate):
        BasicCustomer.b_discountRate = rate      

        for idx, val in enumerate(Records.customerType):
            if val == 'B':
                Records.discount_rate[idx] = str(BasicCustomer.b_discountRate)   

        print(f"Basic Customer discount is updated to {BasicCustomer.b_discountRate:.2f}")
        print()

    def get_clas_discount(self):
        return self.b_discountRate

'''
EnterpriseCustomer class is designed for customers who receive discounts based on distance and a threshold limit, 
and it provides methods to manage and display customer information, calculate discounts, and customize discount rates and 
threshold limits for individual customers or across all Enterprise customers.
'''
class EnterpriseCustomer(Customer):    
    DiscountRateO1 = 15
    DiscountRateO2 = 20
    threshold = 100

    def __init__(self,ID,name):
        super().__init__(ID, name)
        self.e_discountRate = 0

    # Calculate the discount of the enterprise customer when the calculated distance fee is passed
    def get_discount(self,e_distance_fee): 
        cutomer_discount = 0
        cutomer_discount = Records.discount_rate[Records.customerID.index(self.get_ID)]

        # Check if the customer discount is zero or class customer discount attribute is same 
        # as the entrerprise customer discount from the records stored in the Records class.
        if len(cutomer_discount) == 0 or float(cutomer_discount) == 0: 
            if e_distance_fee < self.threshold:
                e_discountRate =  float(self.DiscountRateO1 / 100) * e_distance_fee
            elif e_distance_fee >= self.threshold:
                e_discountRate = float(self.DiscountRateO2 / 100) * e_distance_fee
        elif float(EnterpriseCustomer.DiscountRateO1/100) != float(cutomer_discount): 
            if e_distance_fee < self.threshold:
                e_discountRate =  float(cutomer_discount) * e_distance_fee
            elif e_distance_fee >= self.threshold:
                e_discountRate = (float(cutomer_discount)+ 0.05) * e_distance_fee
        else:
            if e_distance_fee < self.threshold:
                e_discountRate =  (self.DiscountRateO1 / 100) * e_distance_fee
            elif e_distance_fee >= self.threshold:
                e_discountRate = (self.DiscountRateO2 / 100) * e_distance_fee            
        return e_discountRate
    
    def set_discount_rate(self,enterprise_customer,DiscountRateO1):
        discount_index = Records.customer_name.index(enterprise_customer)
        Records.discount_rate[discount_index] = DiscountRateO1
        EnterpriseCustomer.DiscountRateO1 = float(DiscountRateO1) * 100
        EnterpriseCustomer.DiscountRateO2 = (float(DiscountRateO1)+(5/100)) * 100        

    def set_threshold(self, threshold):
        EnterpriseCustomer.threshold = threshold
        for idx, val in enumerate(Records.customerType):
            if val == 'E':
                Records.threshold[idx] = str(EnterpriseCustomer.threshold)   

        print(f"Basic Customer discount is updated to {EnterpriseCustomer.threshold:.2f}")

    def display_info(self):
        print("Customer ID:".ljust(20)+str(self.get_ID))
        print("Customer Name:".ljust(20)+(self.get_name))
        print("Discount Rate 1:".ljust(20)+str(EnterpriseCustomer.DiscountRateO1)+"%")
        print("Discount Rate 2:".ljust(20)+str(EnterpriseCustomer.DiscountRateO2)+"%")
        print("Threshold:".ljust(20)+str(EnterpriseCustomer.threshold))
    
    def get_clas_discount(self):
        return self.DiscountRateO1, self.DiscountRateO2
    
    def get_threshold(self):
        return self.threshold

'''
Class Location is capable of storing and displaying information about different locations, plus ability to add new 
location to the records.
'''
class Location:

    def __init__(self, locationID, locationName):
        self.locationID = locationID
        self.locaionName = locationName

    def display_info(self):
        print("Location ID:".ljust(20)+str(self.locationID))
        print("Location Name:".ljust(20)+(self.locaionName))
    
    # This method allow user to add new location into the program
    def add_location(self,newlocation):
        if ',' in newlocation:
            locations = newlocation.split(',')
        else:
            locations = [newlocation]
        for i in range(0,len(locations)): 
            if locations[i].strip() in Records.locations:
                print(f"The location:{locations[i].strip()} is a existing location. It will not be added to the list.")        
            else:
                newlocation_id = int(Records.location_id[len(Records.location_id)-1][1]) + 1
                Records.location_id.append('L'+str(newlocation_id))
                Records.locations.append(locations[i].strip())            
                print(f"The new location: {locations[i].strip()} have been added.")

'''
Class Rate is capable of storing and displaying information about different rate types, plus ability add/update rate types
and there prices.
'''
class Rate:
    def __init__(self,rateID,rateName):
        self.rateID = rateID
        self.rateName = rateName
        self.price = 0

    """
    Function: add/update rate types and prices
    ---------------------------------
    The new entered rates and prices of the respective rates are added to the there respective list. Meanwhile,
    if the rates already exist the prices of the existing rate are used to update the price list of the respective
    existing rates.
    """
    @staticmethod
    def add_update():
        isNumber = False
        i=0
        rate_exist = False
        RateType = input("Enter the rate type/types [enter a valid type only, e.g. standard, peak, weekends, holiday]:").strip()    
        
        if ',' in RateType:
            rate = RateType.split(',')
        else:
            rate = [RateType]

        price = input("Enter the price of the entered rate type, [enter a valid type only with respective to the entered rate types, e.g 2.0, 2.5, 2.2] : ").strip()
        
        #While loop is used to validate the prices entered by the user. Ask the user to enter the price until the correct format is used
        while isNumber == False:  
            try:  
                # if Operations.is_number(newbasic_discount) and float(newbasic_discount) > 0:
                #     isNumber = True
                if len(price.split(',')) == 1:
                    if Operations.is_number(price) == False:
                        isNumber = False
                        raise InvalidInputError
                    elif (Operations.is_number(price) and float(price)>0):
                        price = [price]
                        isNumber = True 
                    else:
                        isNumber = False
                        raise InvalidInputError
                else:
                    #split the string and create a list of rates entered by the user
                    if ',' in price:
                        price = price.split(',')
                    else:
                        price = [price]                   
                        
                    if (len(rate) != len(price)):
                        isNumber = False
                        raise InvalidInputError
                    else:
                        for p in price:
                            if Operations.is_number(p) == False:
                                isNumber = False
                                raise InvalidInputError
                            elif (Operations.is_number(p) == True and float(p)<=0):
                                isNumber = False
                                raise InvalidInputError
                            elif (Operations.is_number(p) == True and p == 0):
                                isNumber = False
                                raise InvalidInputError 
                            else:
                                isNumber = True
            except InvalidInputError:
                print('Entered price format is invalid. Please enter a valid Price and check the number of price entries match the number of rate types entered above.')
                price = input("Enter a valid type only with respective to the entered rate types, [e.g 2.0, 2.5, 2.2] : ").strip()
        

        #for loop check the number if the user entered rate exist in the list or not. Then update or add accordingly
        for i in range(0,len(rate)): 
            if (rate[i].strip() in Records.rate_type):
                index = Records.rate_type.index(rate[i].strip())
                Records.rate_price[index] = str(price[i].strip())
                print(f"The price({price[i].strip()}) of the {rate[i].strip()} rate has been updated.")
            elif (rate[i].strip() in Records.rate_id):
                index = Records.rate_id.index(rate[i].strip())
                Records.rate_price[index] = str(price[i].strip())
                print(f"The price({price[i].strip()}) of the {rate[i].strip()} rate has been updated.")
            else:
                Records.rate_id.append('R' + str(len(Records.rate_id)+1))
                Records.rate_type.append(rate[i].strip())
                Records.rate_price.append(str(price[i].strip()))
                print(f"{rate[i].strip()} rate and the price({price[i].strip()})  had been added to the list")
        # #get the maximum character length of the rates from the rate list
        # max_rate_length = max(len(rate) for rate in ratesArray)
        # #display all the rates and their respective price
        # for rateType, Price in zip(ratesArray, priceArray):
        #     print(f"{rateType.ljust(max_rate_length+1)}: {Price}")

    def display_info(self):
        print("Rate ID:".ljust(20)+str(self.rateID))
        print("Rate Type:".ljust(20)+(self.rateName))
        print("Rate Price:".ljust(20)+str(self.price))

'''
Class Booking is designed to store and manage booking information, including customer details, departure and destination, 
trip distance, rate type, and a method for calculating associated costs and discounts.
'''
class Booking(Records):
    def __init__(self, customer, departure, destination, distance, rate):
        super().__init__()
        self.customer = customer
        self.departure = departure
        self.destination = destination
        self.distance = distance
        self.rate = rate
        self.basicFee = 4.2
        self.ratePrice = 0
        self.discount = 0

    # Method calculate the distance fee, discount according to the customer type and basic rate
    def compute_cost(self, distance, rateType,customerName,customerType,bookingCustomerID):      
        # calculate the distance fee according to the rate price from the rate file
        if rateType in Records.rate_type:
            i = Records.rate_type.index(rateType)
            self.ratePrice = Records.rate_price[i]      
        self.distanceFee = distance * float(self.ratePrice)    
       
        # calculate discount according to the customer type
        if customerType == 'E':
            customerInstance = EnterpriseCustomer(bookingCustomerID,customerName)
            self.discount = customerInstance.get_discount(self.distanceFee)
        elif customerType == 'B':
            customerInstance = BasicCustomer(bookingCustomerID,customerName)
            self.discount = customerInstance.get_discount(self.distanceFee)

        return self.distanceFee, self.basicFee, self.discount

'''
Class Service is designed to store and manage service information and service prices,
and a method to retrive the price of the service entered by the user.
'''   
class Service:
    def __init__(self, s_ID, s_Name, s_Price):
        self.s_ID = s_ID
        self.s_Name = s_Name
        self.s_Price = s_Price
        self.service_index = 0

    # get the corresponding price of the service entered by the user
    def get_service_price(self, name):
        for i in (Records.service_id,Records.service_name):
            if any(char.isdigit() for char in name):
                self.service_index = Records.service_id.index(name)
                self.s_Price = int(Records.service_price[self.service_index]) 
            else:
                self.service_index = Records.service_name.index(name)
                self.s_Price = int(Records.service_price[self.service_index]) 
        return self.s_Price

'''
Class Package is designed to store and manage package information,
and a method to calculate the price of the package according to the user input.
''' 
class Package(Service):
    def __init__(self,s_ID, s_Name, s_Price, p_ID, p_Name, p_Price):
        super().__init__(s_ID, s_Name, s_Price)
        self.p_ID = p_ID
        self.p_Name = p_Name
        self.p_Price = p_Price
        self.temp_price = []

    # calculate the corresponding price of the package entered by the user
    '''
    Initially check the packagename/ packageid, then output the respective services in the package.
    Then check the price of the each services and add them together. Using the sum of all the price 
    of the services multiple it by 0.8(80%) to calcaulate the price of the package.
    '''
    def get_package_price(self, name):
        i = ""
        k = ""
        a = ""        
        for i in Records.package_name, Records.package_id:
            if name in i:       
                for k in Records.package_services[i.index(name)]:
                    a = Records.service_id.index(k)
                    self.temp_price.append(int(Records.service_price[a]))
                self.s_Price = 0.8*sum(self.temp_price)
        return self.s_Price

class InvalidNameError(Exception):
    pass

class InvalidLocationError(Exception):
    pass

class InvalidRateTypeError(Exception):
    pass

class InvalidDistanceError(Exception):
    pass

class InvalidCustomerTypeError(Exception):
    pass

class InvalidServiceTypeError(Exception):
    pass

class InvalidInputError(Exception):
    pass

'''
Class Operations is the core of the program, managing booking, customer information, file handling, and user interaction 
through a menu system while ensuring data consistency and providing informative receipts for each trip.
'''
class Operations():
    custName = ""
    depL = ""
    desL = ""
    rate = ""
    distance = 0
    exit = False
    read_Customer = ""
    read_Locations = ""
    read_Rates = ""
    read_Service = ""

    @staticmethod
    def menu():
        print("Welcome to the RMIT taxi management system!")
        print()
        print('#'*40)
        print('You can choose from the following options:')
        print('1: Book a trip')
        print('2: Add/Update rate types and prices')
        print('3: Add new locations')
        print('4: Display existing customers')
        print('5: Display existing locations')
        print('6: Display existing rate types')
        print('7: Display the most Popular customer')
        print('8: Display a customer booking history')
        print('9: Display all the bookings')
        print('10: Display the existing services/packages')
        print('11: Adjust the discount rate of all Basic customers')
        print('12: Adjust the discount rate of an Enterprise customer')        
        print('0: Exit the program')
        print('#'*40)
        print()
        return input('Choose one option:')

    @staticmethod
    def contains_number(x):
        if ',' in x:
            string_value = x.split(',')
        else:
            string_value = [x]

        if len(string_value) > 1:
            for i in range(0,len(string_value)):
                return any(x.find(str(k)) for k in range(len(string_value[i])))                  
        else:
            return any(string_value.find(str(i)) for i in range(len(string_value)))

    @staticmethod
    def is_number(x):
        if ',' in x:
            price = x.split(','.strip())
        else:
            price = [x]
        if len(price) > 0:
            for i in range(0,len(price)):
                if isinstance(price[i], int) or isinstance(price[i], float):
                    return True
                #to check if it is a string
                try:
                    price[i] = float(price[i])
                    return True
                except Exception:
                    return False
        else:
            if isinstance(price, int) or isinstance(price, float):
                    return True
            #to check if it is a string
            try:
                price = float(price)
                return True
            except Exception:
                return False

    @staticmethod
    def book_trip():
        departure_exist = False
        destination_exist = False
        rate_exist = False
        extra_s = False
        multiple_destinations = False
        customer_validation = False
        service_fee = 0
        temp_destinations = []
        temp_distance = []
        destination_distance = []
        string_destination_distance = ''
        Instance = Booking(Operations.custName,Operations.depL,Operations.desL,Operations.distance,Operations.rate)   
        
        #input customer name
        custName = input("Enter the name of the customer [e.g. Huong]: ").strip()         

        # validate the customer namer to check if it is a number
        while customer_validation == False:
            try:
                # get the customer name if user entered the cutomer id
                if Operations.is_number(custName) & (custName in Records.customerID):
                    custName = Records.customer_name[Records.customerID.index(custName)] 
                    customer_validation = True
                # validate the customer name
                if custName.isalpha() == False:
                    customer_validation = False
                    raise InvalidNameError 
                else:
                    customer_validation = True               
            except InvalidNameError:
                print("Exception occurred: Name can only contain alphabetical characters")
                custName = input("Enter the name of the customer [e.g. Huong]:").strip()
        
        #input departure location
        depL = input("Enter the departure location [enter a valid location only, e.g. Melbourne]: " ).strip()
        # Check if the user entered departure location exist in the depature location list. if not re-enter until valid input entered
        while departure_exist == False:
            try:
                if (depL in Records.locations) or (depL in Records.location_id):
                    if any(char.isdigit() for char in depL) & (depL in Records.location_id):
                        depL = Records.locations[Records.location_id.index(depL)]
                    departure_exist = True   
                else:
                    departure_exist = False
                    raise InvalidLocationError
            except InvalidLocationError: 
                print('The departure location is not valid. Please enter a valid location.')     
                depL = input("Enter the departure location[enter a valid location only, e.g.Melbourne]:" ).strip() 
        

        # Allow multiple destinations entries by the user
        while multiple_destinations != True: 
            destination_exist = False
            actionValid = False
            desL = input("Enter the destination location [enter a valid location only, e.g. Melbourne]:").strip()  

            # Check if the destination in the location list. check if multiple desttination entries are not the same.
            # Check if the destination is not same as the departure. if these validation are violated, re-enter until 
            # Correct format is entered.      
            while destination_exist == False:
                try:
                    if any(char.isdigit() for char in desL) & (desL in Records.location_id):
                        desL = Records.locations[Records.location_id.index(desL)]
                    if (desL in Records.locations) & (depL != desL) & (desL not in temp_destinations): #& (depL not in temp_destinations) & (desL not in temp_destinations) : #changed here '''or (desL in Records.location_id) '''
                        destination_exist = True 
                    else:
                        destination_exist = False
                        raise InvalidLocationError
                except InvalidLocationError:
                    print('The destination location is not valid. Please enter a valid location.')
                    desL = input("Enter the destination location [enter a valid location only, e.g. Melbourne]:" ).strip()  
            
            # Use a temporary list to store multiple destination entered by the user. Help to reuse the temporary list 
            # for storing in the main list.              
            temp_destinations.append(desL) 

            distance = input("Enter the distance (km) [enter a positive number only, e.g. 12.5, 6.8]: ").strip() 
            # Validate the distance is ineteger or float value greater than or not equal to zero
            # Re-enter until correct format is entered.      
            while Operations.is_number(distance) == False or float(distance)<= 0:
                try:
                    if Operations.is_number(distance) == False or float(distance)<= 0:  
                        raise InvalidDistanceError
                    else:
                        pass         
                except InvalidDistanceError:
                    print('Distance needs to be a valid number. Please enter a valid distance')
                    distance = input("Enter the distance (km) [enter a positive number only, e.g. 12.5, 6.8]:").strip()  

            distance = float(distance)
            # Use a temporary list to store multiple distance entered by the user. Help to reuse the temporary list 
            # for calculaing the total distance and stored them in the final list. 
            temp_distance.append(distance)

            actionUser = input("Do you want to add another destination (y/n)?")
            # Check it the user want to enter another destination and exit or repeat according to the user input
            # If invalid format entered. Re-enter until correct format is entered.
            while actionValid != True:
                if actionUser == "y":
                    multiple_destinations = False
                    actionValid = True
                elif actionUser == "n":
                    multiple_destinations = True
                    actionValid = True
                else:
                    multiple_destinations = False
                    actionValid = False
                    actionUser = input("Invalid format. Enter either y or n : ")  

        rate = input("Enter the rate type[enter a valid type only, e.g. standard, peak, weekends, holiday]:").strip()
        
        # Check if the correct rate type is entered.If invalid format entered. Re-enter until correct format is entered.   
        while rate_exist == False:
            try:    
                if (rate in Records.rate_type) or (rate in Records.rate_id):
                    # if user enter the rateid get the rate type to display in the receipt
                    if rate in Records.rate_id:
                        rate = Records.rate_type[Records.rate_id.index(rate)]
                    rate_exist = True
                else:
                    rate_exist = False
                    raise InvalidRateTypeError
            except InvalidRateTypeError:
                print('The rate type is not valid. Please enter a valid rate type')
                rate = input("Enter the rate type[enter a valid type only, e.g. standard, peak, weekends, holiday]:")
        
        order_more = input("Do you want to add extra services or packages?")
        while extra_s == False:
            try:
                if order_more == 'y':
                    service_packages = input("Enter the service or package name/ID. (i.e: Internet, Snack, Drink, Entertainment, etc.): ")
                    if (service_packages in Records.service_id) or (service_packages in Records.service_name) or (service_packages in Records.package_id) or (service_packages in Records.package_name):
                        extra_s = True
                    else:
                        extra_s = False
                        raise InvalidServiceTypeError
                elif order_more == 'n':
                    service_packages = "-"
                    extra_s = True
                else:
                    extra_s = False
                    raise InvalidInputError
            except InvalidInputError:
                print("Enter input value is not valid. Please selecte y or n accordingly.")
                order_more = input("Do you want to add extra services or packages? (i.e., y, n): ")
            except InvalidServiceTypeError:
                print("Incorrect service or package name/ID entered. Please entered the correct service or package name/ID in the system.")
                order_more = 'y'

        # create object using the class package()
        Instance_service = Package("","","","","","")
        # calculate the servicefee or the packagefee according to the user input
        if (service_packages in Records.service_id) or (service_packages in Records.service_name):
            service_fee = Instance_service.get_service_price(service_packages)
        elif (service_packages in Records.package_id) or (service_packages in Records.package_name):
            service_fee = Instance_service.get_package_price(service_packages)
        # print("Instance price:",service_fee)

        # Find the servicename or packagename if user enter the serviceid or packageid 
        # Useful when priniting the receipt
        if (service_packages[0] == 'S') & (any(char.isdigit() for char in service_packages)):
            service_packages = Records.service_name[Records.service_id.index(service_packages)]
        elif (service_packages[0] == 'P') & (any(char.isdigit() for char in service_packages)):
            service_packages = Records.package_name[Records.package_id.index(service_packages)]
        
        # assign values to the booking class atrributes
        Instance.customer = custName
        Instance.departure = depL
        Instance.destination = temp_destinations
        Instance.distance = temp_distance
        Instance.rate = rate   
        destination_distance = [x for y in zip(Instance.destination,[str(a) for a in Instance.distance]) for x in y] #
       
        for i in range(len(destination_distance)):
            string_destination_distance += destination_distance[i]
            if i != len(destination_distance) - 1:
                string_destination_distance += ', '
        
        #check if the customer is a new member
        custExist = Instance.find_customer(Instance.customer)        
        
        # retrive customertype and customerid from the records class/ add details to record class if new customer
        if len(custExist) != 0:
            index = Records.customer_name.index(custExist)
            customerType = Records.customerType[index]
            bookingCustomerID = Records.customerID[index]
            print()
            print("Customer Type:"+customerType)
            print()
        elif len(custExist) == 0:
            customerType = 'B'
            bookingCustomerID = int(Records.customerID[len(Records.customerID)-1]) + 1
            Records.customerID.append(str(bookingCustomerID))
            Records.customer_name.append(Instance.customer)
            Records.customerType.append(customerType)
            Records.discount_rate.append('0.1')
            Records.threshold.append('0')

        # return the distancefee, basicfee and discount
        costs = Instance.compute_cost(sum(Instance.distance),Instance.rate,Instance.customer,customerType,bookingCustomerID)
        
        # calculate the total cost of the booking according to the 
        basic_fee = costs[1]
        distance_fee = costs[0]
        discount = round(costs[2],2)
        totCost = round((distance_fee - discount) + basic_fee + service_fee,2)
        
        # Use to append information to the customer history list. 
        customer_booking = [Instance.customer, Instance.departure] + destination_distance + [Instance.rate, service_packages, str(basic_fee), str(distance_fee), str(discount), str(totCost)]
        Records.bookings.append(customer_booking)

        # Display all the booking information
        print('_'*40)
        print()
        print('Taxi Receipt'.center(40))
        print('_'*40)
        print()
        print('Name:'.ljust(20)+ custName)
        print('Depature:'.ljust(20)+ depL)
        for destination, distance_destination in zip(temp_destinations,temp_distance):
            print('Destination:'.ljust(20) + str(destination)) 
            print('Distance:'.ljust(20)+f'{float(distance_destination):.2f}' +' (km)')    
        print('Rate:'.ljust(20)+ rate+' (AUD per km)')           
        print('Extra Service:'.ljust(20)+f'{service_packages}') 
        print('Service Price:'.ljust(20)+f'{service_fee:.2f}' +' (AUD)') 
        print('_'*40)
        print()
        print('Basic fee:'.ljust(20)+ f'{costs[1]:.2f}'+' (AUD)')
        print('Distance fee:'.ljust(20)+ f'{costs[0]:.2f}'+' (AUD)')
        print('Discount:'.ljust(20)+ f'{costs[2]:.2f}'+' (AUD)')
        print('_'*40)
        print()
        print('Total cost:'.ljust(20)+ f'{totCost:.2f}'+' (AUD)')   
        print()
    
    @staticmethod
    def run():
        # Main program
        Instance = Booking(Operations.custName,Operations.depL,Operations.desL,Operations.distance,Operations.rate)
        if len(sys.argv) == 1:
            Instance.read_customers('customers.txt')
            Instance.read_locations('locations.txt')
            Instance.read_rates('rates.txt')
            Instance.read_serviceORpackages('services.txt')
            Instance.read_bookings('bookings.txt')
            Operations.exit = False
        elif len(sys.argv) == 5:
            Instance.read_customers(sys.argv[1])
            Instance.read_locations(sys.argv[2])
            Instance.read_rates(sys.argv[3])
            Instance.read_serviceORpackages(sys.argv[4])
            Instance.read_bookings('bookings.txt')
            Operations.exit = False
        elif len(sys.argv) == 6:
            Instance.read_customers(sys.argv[1])
            Instance.read_locations(sys.argv[2])
            Instance.read_rates(sys.argv[3])
            Instance.read_serviceORpackages(sys.argv[4])
            Instance.read_bookings(sys.argv[5])
            Operations.exit = False
        else:
            print("Error: Wrong command line arguments format. \nPlease enter the correct format(i.e: python ProgFunA2_s4033457.py customers.txt locations.txt rates.txt services.txt bookings.txt )")
            Operations.exit = True

        
        while Operations.exit == False:
            Operations.exit = Operations.menu()
            if Operations.exit == "1":
                Operations.book_trip()
                Operations.exit = False
            elif Operations.exit == "2":
                Rate.add_update()
                Operations.exit = False
            elif Operations.exit == "3":
                # As per the assignemtnt 01 requirment, assumed that user enter the correct format
                newLocation = input("Enter the new locations, [e.g Geelong, Carlton, Southbank] : ")
                newLocation_instance = Location("","")
                newLocation_instance.add_location(newLocation)
                Operations.exit = False
            elif Operations.exit == "4":
                Records.list_customer()
                print()
                Operations.exit = False
            elif Operations.exit == "5":
                Records.list_locations()
                print()
                Operations.exit = False
            elif Operations.exit == "6":
                Records.list_rates()
                print()
                Operations.exit = False
            elif Operations.exit == "7":
                temp_customer = []
                temp_totalcost = []
                temp_totalcost_f = []
                customer = ""                

                # Compare all the total cost of the each cutomer using the cutomer history list and output the customer with the
                # maximum total cost. Display the customer name and the their maximum total cost to date
                for i in Records.bookings:
                    # Identify if the input is customer id and get the respective customer name
                    if i[0].isdigit():
                        name = Records.customer_name[Records.customerID.index(i[0])]
                    elif i[0].isdigit() == False:
                        name = i[0]  
                    #                         
                    if name in temp_customer:
                        index = temp_customer.index(i[0])   
                        temp_totalcost[index] = float(temp_totalcost[index]) + float(i[len(i)-1])
                    else:   
                        temp_customer.append(name) 
                        temp_totalcost.append(i[len(i)-1])    
                # convert all the total cost into float values to get the max value in the list
                # to get the max total cost from the total cost list
                for item in temp_totalcost:
                    temp_totalcost_f.append(float(item))
                print(f'Most valuable customer : {temp_customer[temp_totalcost_f.index(max(temp_totalcost_f))]}')
                print()
                print(f'Total amount spent : {max(temp_totalcost_f):.3f}')
                print()
                print()
                Operations.exit = False        
            elif Operations.exit == "8":
                display_booking = [] 
                display_departures = []
                display_destination = []
                display_services = []
                display_totCost = []
                customer_history = []
                destinations = []
                customer = ""
                departure = ""
                service = ""
                customer_validation = False
                i=0
                j=0
                k=0
                m=0

                customerName = input("Enter customer name: ").strip()
                # validate the customer namer to check if it is a number
                while customer_validation == False:
                    try:
                        # get the customer name if user entered the cutomer id                        
                        if Operations.is_number(customerName) & (customerName in Records.customerID):
                            customerName = Records.customer_name[Records.customerID.index(customerName)] 
                            customer_validation = True
                        elif customerName not in Records.customer_name:
                            customer_validation = False
                            raise InvalidInputError
                        elif Operations.is_number(customerName) & (customerName not in Records.customerID):
                            customer_validation = False
                            raise InvalidInputError
                        
                        # validate the customer name
                        if customerName.isalpha() == False:
                            customer_validation = False
                            raise InvalidNameError 
                        else:
                            customer_validation = True               
                    except InvalidNameError:
                        print("Exception occurred: Name can only contain alphabetical characters")
                        customerName = input("Enter the name of the customer [e.g. Huong]:").strip()
                    except InvalidInputError:
                        print("Exception occurred: Invalid name")
                        customerName = input("Enter the name of the customer [e.g. Huong]:").strip()

                column = [" ","Departure","Destination", "Service","Total Cost"]
                
                for i in Records.bookings:
                    destinations = []
                    # get the customer name if user entered the cutomer id
                    customer = i[0]
                    departure = i[1]
                    service = i[len(i)-5]
                    if Operations.is_number(i[0]) & (i[0] in Records.customerID):
                        customer = Records.customer_name[Records.customerID.index(i[0])]
                    if any(char.isdigit() for char in i[1]) & (i[1] in Records.location_id):
                        departure = Records.locations[Records.location_id.index(i[1])] 
                    for char in i[2:(len(i)-6)]:
                        if Operations.is_number(char) == False:
                            if any(char.isdigit() for char in char) & (char in Records.location_id):                        
                                destinations.append(Records.locations[Records.location_id.index(char)])
                            elif not any(char.isdigit() for char in char) & (char in Records.locations) :
                                destinations.append(char)
                    if any(char.isdigit() for char in i[len(i)-5]) & (i[len(i)-5] in Records.service_id):
                        service = Records.service_name[Records.service_id.index(i[len(i)-5])]
                    elif any(char.isdigit() for char in i[len(i)-5]) & (i[len(i)-5] in Records.package_id):
                        service = Records.package_name[Records.package_id.index(i[len(i)-5])]  
                    customer_history.append({'Customer':customer,'Departure': departure,'Destination':', '.join(map(str, destinations)),'Service' : service,'Total Cost':i[len(i)-1]}) 

                # print(customer_history)
                # Use to append information to the customer history list.        
                # custHistory.append({'Customer':customerName,'Departure': depL,'Destination':tempDesString,'Total Cost':round(totCost,2)})  
                
                # Extract all the booking detail of the user entered customer from the customer history list 
                # and prepare these information for the required dispplay format
                for m in range(len(customer_history)):
                    if customer_history[m].get('Customer') == customerName: 
                        k+=1
                        display_booking.append(f'Booking {k}') 
                        display_departures.append(customer_history[m].get('Departure'))
                        display_destination.append(customer_history[m].get('Destination')) 
                        display_services.append(customer_history[m].get('Service'))
                        display_totCost.append(customer_history[m].get('Total Cost')) 
                table = [display_booking,display_departures,display_destination,display_services,display_totCost]

                                
                # Check if the customer have any bookings under there name. Display the booking details 
                # or produce a message informing they don't have any bookings under their name
                if len(display_departures) != 0:
                    '''
                    Get the maximum variable length to left justify in proper format. Therefor there 
                    won't be any inconsistencies when printing according to the required format
                    '''
                    maxVariable_length = max(len(des) for des in display_destination)
                    if maxVariable_length<15:
                        maxVariable_length = 15
                    for i in range(len(table)) :
                        print(f"{column[i]:<15}", end=" ")
                        for j in range(len(table[i])) :        
                            print(str(table[i][j]).ljust(maxVariable_length+5), end=" ")
                        print() 
                else:
                    print(f'There is no bookings for {customerName} in the system')

                print()
                print()
                Operations.exit = False
            elif Operations.exit == "9":
                Records.list_bookings()
                print()
                Operations.exit = False            
            elif Operations.exit == "10":
                # print(Records.list_services)
                # print the existing service and details
                Records.list_services() 
                print()                    
                Operations.exit = False
            elif Operations.exit == "11":          
                validate = False
                newbasic_discount = input("Enter the new Basic Customer discount rate:")

                while validate == False:
                    try:
                        if Operations.is_number(newbasic_discount) and float(newbasic_discount) > 0:
                            validate = True                            
                        else:
                            validate = False
                            raise InvalidInputError
                    except InvalidInputError:
                        print("Invalid input format. Input should a number and greater than 0.")
                        newbasic_discount = input("Enter the new Basic Customer discount rate:")
                Instance_basic = BasicCustomer("","")
                Instance_basic.set_discount_rate(float(newbasic_discount))
                Operations.exit = False
            elif Operations.exit == "12":
                validate = False
                validate_customer = False
                validate_discount_1 = False

                #input customer name
                enterprise_customer = input("Enter the name of the customer [e.g. Huong]: ").strip() 

                # if Operations.is_number(enterprise_customer) & (enterprise_customer in Records.customerID):
                #     enterprise_customer = Records.customer_name[Records.customerID.index(enterprise_customer)] 
                # print(enterprise_customer)

                #validate the customer name with customized exception
                while validate_customer == False:                    
                    try:
                        if Operations.is_number(enterprise_customer) & (enterprise_customer in Records.customerID):
                            enterprise_customer = Records.customer_name[Records.customerID.index(enterprise_customer)]
                            validate_customer = False 
                        if enterprise_customer.isalpha() == False :
                            validate_customer = False
                            raise InvalidInputError   
                        elif enterprise_customer not in Records.customer_name:
                            validate_customer = False
                            raise InvalidNameError 
                        elif Records.customerType[Records.customer_name.index(enterprise_customer)] != 'E':
                            validate_customer = False
                            raise InvalidCustomerTypeError 
                        else:
                            validate_customer = True           
                    except InvalidInputError:
                        print("Exception occurred: Name can only contain alphabetical characters")
                        enterprise_customer = input("Enter the name of the customer [e.g. Huong]:").strip()
                    except InvalidNameError:
                        print("Customer is not in the system. Please select a customer already in the system.")
                        enterprise_customer = input("Enter the name of the customer [e.g. Huong]:").strip()
                    except InvalidCustomerTypeError:
                        print("Invalid customer type. Please enter a enterprise customer name.")
                        enterprise_customer = input("Enter the name of the customer [e.g. Huong]:").strip()

                discount_1 = input("Enter the new Enterprise Customer first discount rate (e.g., 0.2 which corresponds to 20'%' discount rate):")

                # user entered discount rate is validate using customized exception
                while validate_discount_1 == False:
                    try:
                        if Operations.is_number(discount_1) == False or float(discount_1) <= 0:
                            validate_discount_1 = False 
                            raise InvalidInputError                           
                        else:
                            validate_discount_1 = True
                            
                    except InvalidInputError:
                        print("Invalid input format. Input should a number and greater than 0.")
                        discount_1 = input("Enter the new Enterprise Customer first discount rate:")

                Instance_enterprise = EnterpriseCustomer("","")
                Instance_enterprise.set_discount_rate(enterprise_customer,discount_1)

                Operations.exit = False
            elif Operations.exit == "0":
                f = open('customers.txt', 'w')
                i = ""
                for i in zip(Records.customerID,Records.customer_name, Records.customerType, Records.discount_rate, Records.threshold):
                    # print(i)
                    # print(', '.join(i))
                    f.write(', '.join(i) + '\n')
                f.close()

                f = open('locations.txt', 'w')
                i = ""
                for i in zip(Records.location_id,Records.locations):
                    # print(i)
                    # print(', '.join(i))
                    f.write(', '.join(i) + '\n')
                f.close()

                f = open('rates.txt', 'w')
                i = ""
                for i in zip(Records.rate_id,Records.rate_type,Records.rate_price):
                    # print(i)
                    # print(', '.join(i))
                    f.write(', '.join(i) + '\n')
                f.close()
                
                f = open('bookings.txt', 'w')
                i = ""
                for i in Records.bookings:
                    f.write(str(i)[1:-1] + '\n')
                    
                f.close()
                Operations.exit = True
            elif Operations.exit.isdigit():
                print('In valid menu item. Please select numbers from the menu')
                print()
                print()
                Operations.exit = False
            else:
                Operations.exit = False

if __name__ == "__main__":
    operations = Operations()
    operations.run()





