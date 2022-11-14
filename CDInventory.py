#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Andrew Mann, 2022-Nov-13, Added functionality by changing list to dictionary
#------------------------------------------#

# Declare variabls
lstTbl = {} #Creates dictionary for list of lists
lstRow = {} #Creates dictionary for list of row data
strFileName = 'cd_inventory.txt'  # data storage file
objFile = None  # file object



print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('Please choose from the following options:')
    print('L - LOAD EXISTING FILE', 'A - ADD CD TO INVENTORY', 'i - PRINT CURRENT INVENTORY', 'D - DELETE CD FROM CURRENT INVENTORY','S - SAVE CURRENT CD INVENTORY TO FILE', 'X - EXIT', sep='\n')
    user_input = input('\nl, a, i, d, s or x: ').lower()
    
    # option 1: Load file
    if user_input =='l': 
        # TODO Add the functionality of loading existing data
            objFile = open(strFileName, 'r')
            print()
            print('Existing File Content:')
            for row in objFile:
                print (row)
            objFile.close()            
            pass        
        
        # option 2: add new album
    elif user_input == 'a':
            print('PLEASE ASSIGN ALBUM #: ')
            album_id = input()
            artist_name = input('ENTER ARTIST NAME: ')
            album_name = input('ENTER ALBUM NAME: ')
            lstTbl[album_id] = [artist_name.title(), album_name.title()]
            print('Album has been successfully added!')

     # option 3: Display current inventory
    elif user_input == 'i':

            print('\nCURRENT INVENTORY')
            with open(strFileName, 'r') as file:
                for row in file:
                    lstRow = row.strip().split(',')
                    lstTbl[lstRow[0]] = [lstRow[1], lstRow[2]]
                for key, values in lstTbl.items():
                        artist, album = values
                        print(f"{key} | {album} by {artist}")
                
    
    # option 4: delete album from inventory
    elif user_input == 'd':
        del_album = input('Please enter album ID: ')
        for key, values in lstTbl.items():
            if key == del_album:
                artist, album = values
                print(f"{album} by {artist} will now be deleted.")
                lstTbl.pop(del_album)
                break

    # option 5: save data to file cd_inventory.txt
    elif user_input == 's':
         with open(strFileName, 'w+') as file:
            for key, values in lstTbl.items():
                artist, album = values
                file.write(f'{key},{artist},{album}\n')
         print('Saved!')
         
 

       #option 6: Exit the program if the user chooses so
    elif user_input == 'x':
        print('\nNOW EXITING.........')
        break
    
    else:
        print('\nInvalid input please try again')