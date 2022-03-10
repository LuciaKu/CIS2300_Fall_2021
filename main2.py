import car 
def main():
    car_year_model=""
    car_make=""
    car_speed=0
    
    myCar=car.Car(car_year_model,car_make,car_speed)

    car_year_model=int(input("Enter your car's year model:\n"))
    car_make=input("Enter your car's make:\n")
   
    print("Your car's year model is: ", car_year_model,", your car's make is: ",car_make,", and your car's initial speed is: ",car_speed)
    
    for x in range(1,6):
        myCar.accelerate()
        print("Your car's "+str(x)+" accelerated speed is:",myCar.get_speed())
        
    for x in range(1,6):
        myCar.brake()
        print("Your car's "+str(x)+" braked speed is:",myCar.get_speed())
        
main()