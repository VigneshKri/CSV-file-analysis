import csv
car_fields = ['car_model', 'company', 'year', 'price', 'kms_driven', 'fuel_type']
car_db = 'quikr_car.csv'
#index = 890
def display():
    print('1.Add new data')
    print('2.search data')
    print('3.update data ')
    print('4.delete data')
    print('5.quit')

def add_data():
    global car_db
    global car_fields

    car_data = []
    for field in car_fields:

        value = input("enter "+field+":")
        car_data.append(value)
    with open(car_db, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([car_data])
    print("Added new data")
    print("press any key to continue")
    return

def search_data():
    global car_db
    global car_fields
    print("search car")
    roll = input("enter model name to search:")
    print(roll)
    with open(car_db, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    #print("car found")
                    print('car_model',row[0])
                    print('company',row[1])
                    print('year',row[2])
                    print('price',row[3])
                    print('kms-driven',row[4])
                    print('fuel-type',row[5])
                    break
                else:
                    print('car not found')
    input("press any key to continue")

def update_data():
    global car_db
    global car_fields
    print("update data")
    roll = input("enter the car model to update")
    index = None
    updated_data = []
    with open(car_db, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) >0:
                if roll == row[0]:
                    index = counter
                    print('car data found at ', index)
                    car_data = []
                    for field in car_fields:
                        value = input("enter"+field+":")
                        car_data.append(value)
                    updated_data.append(car_data)
                else:
                    updated_data.append(row)
                    counter += 1
        if index is not None:
            with open(car_db, "w", encoding='utf=8') as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("car model not found")
        input("press any key to continue")


def delete_data():
    global car_db
    global car_fields

    print("delete data")
    model = input("enter the car model")
    found = False
    updated_data = []
    with open(car_db, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if model != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    found = True
        if found is True:
            with open(car_db, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
                print("car model", model, "deleted successfully")
        else:
            print("model not found")
        input("press any key to continue")


while True:

    display()
    choice = input("enter your choice:")
    if choice == '1':
        add_data()
    elif choice == '2':
        search_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        delete_data()
    else:
        break

print("thank you")

