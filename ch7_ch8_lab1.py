#My name is Jacob Baker and this is Chapter 7 and 8 Lab 1 which I am completing on July 1
import csv


def file_read():
    print("The contents of the file is:\n)")
    with open("file_example.csv") as file:
          for line in file:
              print(file_example)

def file_write():
    first_name = input("Enter the first name:  ")
    last_name = input("Enter the last name:  ")
    street_address = input("Enter the street address:   ")
    city_name = input("Enter the city:   ")
    state_name = input("Enter the state:  ")
    zip_code = input("Enter the zip code:     ")

    try:
        with open(file_name, "a", newline='')as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, street_address, city_name, state_name, zip_code])
            print("Entry created in file.")
    except Exception as e:
        print
    
    
    


def file_pull():
    file_name = input("What is the name of the file you wish to work with?   ")
    mode = input("Are you going to (r)ead the file or (w)rite the file?  ")
    if mode == "r":
        file_read()
    elif mode == "w":
        file_write()
    else:
        print("Invalid value is entered. Please try again.")

def main():
    file_pull()

main()
              
