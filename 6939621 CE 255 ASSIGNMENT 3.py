#6939621
#Koduah Shmammah Yeboah
#COMPUTER APPLICATION ASSIGNMENT 3
#https://github.com/KoduahShammah


Car =["Toyota Vitz","Ferrari 488","lamborghini track","Maruti Suzuki","Toyota Corolla","Chevrolet Equinox","Toyota Sienna","Toyota Land Cruiser Prado",
      "Lexus RX","Toyota Tundra","Toyota Tacoma","Toyota Sequoia","Toyota Matrix","Nissan Pathfinder",
      "Nissan Sentra","Ferrari Portofino","Nissan Versa","Nissan Patrol","Nissan Titan","Nissan Frotier",
      "Hyundai Accent","Hyundai Elantra","Hyundai Tucson","Hyundai Sonata","Hyundai Santa Fe","Honda Civic","Honda Accord","Honda Pilot","Honda Odyssey",
      "Ferrari Laferrari"]
Models=["1999","2003","2005","2012","2019","2021","2022"]
Price=[90000,625000,150000,830000,750000,178000,238000]
CarModelPrice=[]
print("Welcome to Shammah's car Dealership")
order=input("Which car would you like to buy?")
if order in Car:
   model=input("Please enter the model of the car you would like to buy.")
   if model in Models:
     if model=="1999":
      print("The price of the vehicle chosen is GHS",Price[0])
     elif model=="2003":
      print("The price of the vehicle chosen is GHS",Price[1])
     elif model=="2005":
      print("The price of the vehicle chosen is GHS",Price[2])
     elif model=="2012":
      print("The price of the vehicle chosen is GHS",Price[3])     
     elif model=="2019":
      print("The price of the vehicle chosen is GHS",Price[4])
     elif model=="2021":
      print("The price of the vehicle chosen is GHS",Price[5])
     elif model=="2023":
      print("The price of the vehicle chosen is GHS",Price[6])
   else:
     print("This model is not available")
else:
 print("This vehicle is not available")
 
      
    