def main():
    height = int(input("Height: "))
    pyramid(height)
    

def pyramid(n):
    #For each row in square
    for i in range(n):
        print("#" * (i + 1))
    
if __name__ == "__main__":

    main()    