import random
def main():
    w = int(input('How wide would you like the map to be? '))
    h = int(input('How high would you like the map to be? '))
    file_name = input('What is the name of the file? ')
    image_prefix = input('What is the image prefix?')
    image_count = int(input('How many images? '))
    #takes all user input
    f = open(f'{file_name}', 'w') #opens a file with given filename in write mode
    f.write(image_prefix) #writes the given image_prefix as first line
    f.write('\n') #new line
    for i in range(h): #iterates through rows

        for j in range(w): #iterates through columns
            line = f'{random.randint(0, image_count-1)},' #chooses a random number to represent one of the images
            f.write(line) #writes the number representation with a ',' at the end
        f.write('\n') #prints a new line after each row is done being printed




    f.close() #closes file



main() #calls main function
