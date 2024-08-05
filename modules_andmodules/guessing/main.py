from my_functions import set_number, check

def main():
    comp = set_number()
    i = 0
    while True:
        n = int(input("Введите ваше число:"))
        i += 1

        is_true = check(Computer=comp, value=n)
        
        if is_true:
            print ("Siz sandy taptynyz!")
            break 
        else:
            if i < 3:
              print( "Dagy araket kylynyz")
            else:
                print("Siz utuldunuz!")
                print(f"Computer oilogon san = {comp}")
                break

if __name__ =="__main__":
    main()