"""
Abby Snyder
MET CS 521 A2
Fall 2020
Final Project
"""

#user-defined function to import dogData.csv
def data(fileName):
    breeds = []
    f = open(fileName, "r")
    csv = f.read()
    csv = csv.split("\n") #split up data by line
    for index,line in enumerate(csv):
        if index != 0: #ignores header row
            line = line.split(",") #split up each attribute in each line
            breeds.append(Dog(line[0], line[1], line[2], line[3], line[4]))
    f.close()
    return breeds

#if data file is missing, craete a dog breed csv (for try block)
def create_csv():
    f = open("dogData.csv", "w")
    f.write("Breed,Size,Coat,Shedding,Activity Level" + "\n")
    f.write("Australian Cattle Dog,M,Short,Moderate,High" + "\n")
    f.write("Basenji,S,Smooth,Low,High" + "\n")
    f.write("Bernese Mountain Dog,XL,Medium,Moderate,High" + "\n")
    f.write("Boxer,L,Smooth,Moderate,High" + "\n")
    f.write("Chihuahua,XS,Short,Low,Low" + "\n")
    f.write("Collie,M,Long,Moderate,Moderate")
    f.close()

def validContinue(response):
    valid = ["YES", "NO"]
    if response in valid:
        return True
    else: 
        return False
    
def writeOutput(output):
    f = open("breeds.txt", "w")
    f.write(output)
    f.close()

#user-defined class gives the charactaristics(attributes) of what "dog" is in the program.
#Breed is the 1 private attribute (can't be changed), the rest of the 4 are public attributes
class Dog:
    def __init__(self, breed, size, coat, shedding, activityLevel):
        self.__breed = breed
        self.size = size
        self.coat = coat
        self.shedding = shedding
        self.activityLevel = activityLevel
        
    def validSize(size):
        valid = ["XS", "S", "M", "L", "XL"]
        if size in valid:
            return True
        else: 
            return False

    def validCoat(coat):
        valid = ["SHORT", "MEDIUM", "LONG", "SMOOTH", "WIRE"]
        if coat in valid:
            return True
        else: 
            return False

    def validActivity(activity):
        valid = ["LOW", "MODERATE", "HIGH"]
        if activity in valid:
            return True
        else: 
            return False        
    
    #private functions 
    def matchSize(self, size):
        size = size.upper()
        #the size the user inputs matches the size of the data
        if size == self.size:
            return True
        else:
            return False
    
    def matchCoat(self, coat):
        coat = coat.upper()
        #the coat the user inputs matches the coat of the data
        if coat == self.coat.upper():
            return True
        else:
            return False
        
    def matchActivityLevel(self, activityLevel):
        activityLevel = activityLevel.upper()
        #the activityLevel the user inputs matches the activityLevel of the data
        if activityLevel == self.activityLevel.upper():
            return True
        else:
            return False
        
    def matchBreed(self, breed):
        breed = breed.upper()
        #the breed the user inputs matches the breed of the data
        if breed == self.breed.upper():
            return True
        else:
            return False
        
    
    #class level public function
    def detail():
        return "breed, size, coat, shedding, activityLevel"
    
    #string representaion of an object
    #defining what happens when you print out "dog"
    def __repr__(self):
        output = f"Dog's breed: {self.__breed}\n"
        output += f"Dog's size: {self.size}\n"
        output += f"Dog's coat: {self.coat}\n"
        output += f"Dog's shedding quality: {self.shedding}\n"
        output += f"Dog's activity level: {self.activityLevel}\n"
        return output
    
#try block for FileNotFoundError
try:    
    start_Breeds = data("dogData.csv")
except FileNotFoundError:
    create_csv()
    #input file
    start_Breeds = data("dogData.csv")

if __name__ == "__main__": #for unit tests
    response = ""
    while response != "NO":
        breeds = start_Breeds
        available = []
        response = input("What size dog are you looking for (XS, S, M, L, XL)?: ").upper().strip()
        while not Dog.validSize(response):
            print("I'm sorry, your input is valid")
            response = input("What size dog are you looking for (XS, S, M, L, XL)?: ").upper().strip()
        for breed in breeds:
            if breed.matchSize(response):
                available.append(breed)
        print(f"Total of remaining breeds: {len(available)}")
        response = input("What kind of coat are you look for (short, medium, long, smooth, wire): ").upper().strip()
        while not Dog.validCoat(response):
            print("I'm sorry, your input is valid")
            response = input("What kind of coat are you look for (short, medium, long, smooth, wire)?: ").upper().strip()
        breeds = available
        available = []
        for breed in breeds:
            if breed.matchCoat(response):
                available.append(breed)
        print(f"Total of remaining breeds: {len(available)}")
        breeds = available
        available = []
        response = input("What activity level your dog will have (low, moderate, high)?: ").upper().strip()
        while not Dog.validActivity(response):
            print("I'm sorry, your input is valid")
            response = input("What activity level your dog will have (low, moderate, high)?: ").upper().strip()
        for breed in breeds:
            if breed.matchActivityLevel(response):
                available.append(breed)
        print(f"Total of remaining breeds: {len(available)}")
        #file output
        fileOutput = ""
        for dog in available:
            fileOutput += str(dog) + "\n"
            print(dog)
        writeOutput(fileOutput)
        response = input("Would you like to find another dog, yes or no? ").upper().strip()
        while not validContinue(response):
            print("I'm sorry, I do not understand")
            response = input("Would you like to find another dog, yes or no? ").upper().strip()