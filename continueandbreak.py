rate = 5
stock = 10
print("The rate of candies is " , rate, "rupees per candy")
x = int(input("please input the number of candies you want to buy"))
var = 1
cost = 1
while var <= x:
    if x > stock:
        print("THE AMMOUNT OF CANDIES ENTERED BY YOU IS GREATER THAN OUR STOCK ")
        print('WE ONLY HAVE' , stock , 'CANDIES\n PLEASE ENTER BETWEEN RANGE')
        print('SORRY FOR ENCONVIENCE')

        print('sorry we are out of stock')
        break

    print("candy" , var)
    cost=rate*var
    var+=1
    stock-=1
print('you have been cost of rupees' , cost)
print(' \tTHANK YOU FOR USING OUR SERVICES  \n \tWE WILL BE HAPPY TO SEE YOU AGAIN')
print('left candies are ' , stock)
