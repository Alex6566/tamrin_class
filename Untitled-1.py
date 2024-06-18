
class Calculator:
    def __init__(self , n1 , n2 , type):

        match type:

            case '+':
                print('Result: ' , end='')
                print(self.sum(n1 , n2))

            case '-':
                print('Result: ' , end='')
                print(self.sub(n1 , n2))

            case '*':
                print('Result: ' , end='')
                print(self.mult(n1 , n2))

            case '/':
                print('Result: ' , end='')
                print(self.div(n1 , n2))

    def sum(self , n1 , n2):

        return float(n1) + float(n2)

    def sub(self , n1 , n2):

        return float(n1) - float(n2)

    def mult(self , n1 , n2):

        return float(n1) * float(n2)

    def div(self , n1 , n2):

        return float(n1) / float(n2)

def getNum():

    try:
        n1 = float(input('num 1: '))
        n2 = float(input('num 2: '))

        return [n1 , n2]

    except:
        
        print('Error')


while True:

    print('''
          
1- sum
2- sub
3- mult
4- div
5- exit
          
''')
    
    command = input('Enter your choice: ').lower()

    if command == '1' or command == 'sum':

        nums = getNum()

        Calculator(nums[0] , nums[1] , '+')

    elif command == '2' or command == 'sub':

        nums = getNum()

        Calculator(nums[0] , nums[1] , '-')

    elif command == '3' or command == 'mult':

        nums = getNum()

        Calculator(nums[0] , nums[1] , '*')

    elif command == '4' or command == 'div':

        nums = getNum()

        Calculator(nums[0] , nums[1] , '/')

    elif command == '5' or command == 'exit':

        break

    else:

        pass