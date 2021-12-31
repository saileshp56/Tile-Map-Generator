import pygame

def main():
    while True: #allows user to try as many times as they want
        try:
            file_name = input('What is the name of your file? ')
            f = open(file_name, 'r') #opens file
            break #exits while loop
        except FileNotFoundError: #if file not found
            print('File does not exist')

    file_data = f.read()

    list_data = file_data.strip().split('\n')

    outter_list = []
    for element in list_data:
        row = []
        for item in (element.split(',')):
            try:
                row.append(int(item)) #appends all integer values

            except ValueError:
                row.append(item) #if can't be int()'d, just append as is

        if len(row) > 1:
            row.pop() #to remove the '' at index -1 of each row after the first row which contains the prefix
        outter_list.append(row) #append the entire row, to make a multimensional list


    prefix = outter_list[0][0] #prefix is first index of first inner list
    outter_list.pop(0) #removes prefix list

    int_list = []
    for element in outter_list:
        row = []
        for var in element:
            if isinstance(var, int) == False or int(var) < 0: #if the file did not have integers
                print('Invalid identifier character, setting to 0')
                row.append(0) #replace with 0
            else:
                row.append(var)
        int_list.append(row)
    outter_list = int_list[:] #copies to outter_list


    number_of_images = []
    for row in outter_list:
        for num in row:
            if num not in number_of_images:
                number_of_images.append(num) #makes list of the numbers (each appearing once)
    number_of_images.sort() #sorts from least to greatest

    image_list = []
    try:
        temp = min(number_of_images) - 1 #sets to 1 below the smallest occuring number in the file
    except ValueError:
        print('You input an empty list, I will fill it for you')
        outter_list.append([1,2,3]) #fills outter_list
        number_of_images = [1,2,3] #fills number_of_images
        temp = min(number_of_images) - 1
    
    
    while temp < min(number_of_images) and temp > -1: #if the minimum number is greater than 0, then do while temp is less than the minimum number
        image_list.append(temp) #adds to image list so there are no gaps in indexing
        temp +=1 #increments
        
    for num in number_of_images:
        try:
            image_list.append(pygame.image.load(f'{prefix}{num}.gif'))
            if num != (temp+1): #if the existing number is not consecutive
                
                image_list.pop() #then remove the object
                while temp < (num - 1): #until the existing number is consecutive
                    temp += 1 #increment temp
                    image_list.append(temp) #append temp
                image_list.append(pygame.image.load(f'{prefix}{num}.gif')) #re-add the object
                
            temp = num #update temp
                
        except FileNotFoundError: #if the file does not exist
            print(f'{prefix}{num}.gif does not exist, terminating program now.')
            quit() #terminates program

    

    j = 0
    try:
        (dimension, _) = image_list[j].get_size()
    except AttributeError: #if it is just one of the integers I appended earlier

        while isinstance(image_list[j], int): #until the index returns an object
            j = j + 1 #keep incrementing

        (dimension, _) = image_list[j].get_size() #store size, just need 1 dimension
        
        
    window = pygame.display.set_mode((dimension * len(outter_list[0]), dimension * (len(outter_list)))) #sets pygame window to width * dimension and height * dimension

    for i in range(len(outter_list)):
        y = i * dimension #sets y coordinate

        counter = 0
        for num in outter_list[i]: #loops through the rows

            window.blit(image_list[num], (counter * dimension, y)) #blits each image using index of the for loop's num variable
            #since they were made to naturally line up

            counter += 1 #increments counter


    f.close() #closes file

    pygame.display.update()
    pygame.time.delay(15000)  # keeps window open for 15 seconds
    pygame.quit()

main() #calls main function
