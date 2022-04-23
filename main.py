

from analyzer import analyze


def main():
    print('What would you like to analyze?') 
    user_choise = input('Books / Cryptocurrency? [1 / 2]: ')
    while True: 
        if user_choise == '1':
            analyze('bestsellers.csv')
            break
        elif user_choise == '2':
            analyze('cryptocurrency.csv')
            break
        else:
            print('Please select [1 / 2]: ')

if __name__ == "__main__":
    main()