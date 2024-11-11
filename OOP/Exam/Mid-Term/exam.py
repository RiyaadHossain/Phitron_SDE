class Star_Cinema:
    hall_list = []

    def __init__(self):
        pass

    @classmethod
    def entry_hall(cls,new_hall):
        cls.hall_list.append(new_hall)

    def __str__(self):
        return "Welcome to Star Cinema"
        

class Hall(Star_Cinema):
    hall_history = []

    def __init__(self, hall_no,rows, cols ):

        if hall_no in self.hall_history:
            print(f"\nError: Hall No '{hall_no}' already opened")
            return

        if rows > 10 or rows < 5:
            print("\nRows must be within range 5 - 10")
            return
        
        if cols > 10 or cols < 5:
            print("\nCols must be within range 5 - 10")
            return

        self.__hall_no = hall_no 
        self.rows  =rows +1 
        self.cols =cols +1
        self.__show_list =[] # Private to prevent accessing from outside class
        self._seats =dict() # Protected to allow accessing inside class and subclass
        self.hall_history.append(hall_no)

        Star_Cinema.entry_hall(self)
        print("\nSuccess: Hall Opened!!!")

    @staticmethod
    def is_list_of_tuples(arg):
        return isinstance(arg, list) and all(isinstance(item, tuple) for item in arg)

    def entry_show(self, id, moive_name, time):
        if id not in self.hall_history:
            print(f"\nError: Hall No '{id}' not exist!")
            return

        show_info = (id, moive_name, time)

        if show_info in self.__show_list:
            print(f"\nError: Show '{moive_name}' already running on time: '{time}'")
            return

        self.__show_list.append(show_info)

        seat_info = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self._seats[id] = seat_info

        print(f"\nSuccess: Show '{moive_name}' added!")

    def book_seat(self, id, choosen_seats):
        if len(choosen_seats) == 0:
            print("\nNo seat choosen")
            return
        
        if self.is_list_of_tuples(choosen_seats) == False:
            print("\nChoosen seats must be a list of tuple")
            return

        id = int(id)
        if id not in self.hall_history:
            print(f"\nError: Hall No {id} not exist!")
            return

        choosen_seats = set(choosen_seats)

        booked_seats = []
        for seat in choosen_seats:
            row = seat[0]
            col = seat[1]

            if row < 1 or row > self.rows or col < 1 or col > self.cols:
                print(f"\nError: Invalid seat row {row}, col {col}")
                return
            elif self._seats[id][row][col] == 0:
                booked_seats.append(seat)
                self._seats[id][row][col] = 1
            else: 
               print(f"\nError: Seat {seat} is already booked")
               return
    
        print("\nSuccess: Booking Completed!!!!")
        print("You booked seats:", *booked_seats)

    def view_show_list(self):
        print("Currently Running:")
        for show in self.__show_list:
            print(f'Id: {show[0]} Moive: {show[1]}')

    def available_seats(self, id):
        id = int(id)
        if id not in self.hall_history:
            print(f"Hall No {id} not exist!")
            return

        availabele = []
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self._seats[id][i][j] == 0:
                    availabele.append((i,j))

        if len(availabele) == 0:
            print(f"No available seats of id {id}")     
            return
        
        print("Available seats:")
        print(availabele)

    def __str__(self):
        return f'Hall No:{self.__hall_no} Rows:{self.rows} Cols:{self.cols}'

my_hall = Hall(1, 5, 5)
my_hall2 = Hall(2, 5, 5)

my_hall.entry_show(1, "On the Judgement Day", "After Barjakh")
my_hall.entry_show(2, "Crossing Pulsirat", "After JudgementDay")	
my_hall.entry_show(1, "To Jannah", "After Safely passed the sirat")	


firtTime = True
while True:
    if firtTime:
        firtTime = False
        print("\nWelcome to Star Cinema")


    print("\nCoose an option: ")
    print("\t1. View all running Shows")
    print("\t2. View available seats")
    print("\t3. Book a seats")
    print("\t4. Quit")

    cmd = int(input("\tType Here: "))

    if cmd == 1:
        my_hall.view_show_list()
    elif cmd == 2:
        id = input("\nType show id: ")
        my_hall.available_seats(id)
    elif cmd == 3:
        id = input("\nType show id: ")
        choosen_seats = []
        while True:
            print("\t1. Continue Booking")
            print("\t2. Confirm Booking")

            cmd2 = int(input("\tType Here: "))

            if cmd2 == 1:
                row = int(input("\t\tType row: "))
                col = int(input("\t\tType col: "))
                choosen_seats.append((row, col))
            else:
                break
        my_hall.book_seat(id, choosen_seats)

    else: 
        break