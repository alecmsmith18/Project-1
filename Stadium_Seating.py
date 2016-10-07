def main():
    seat_A()
    seat_B()
    seat_C()
def seat_A():
    ticket_A = int(input("Enter total amount of A Tickets sold: "))
    class_a = 20 * ticket_A
    print("Stadium's A Seating is:")
    print("$", format(class_a, ',.2f'))
def seat_B():
    ticket_B = int(input("Enter total amount of B Tickets sold: "))
    class_b = 15 * ticket_B
    print("Stadium's B Seating is:")
    print("$", format(class_b, ",.2f"))
def seat_C():
    ticket_C = int(input("Enter total amount of C Tickets sold: "))
    class_c = 10 * ticket_C
    print("Stadium's C Seating is:")
    print("$", format(class_c, ',.2f'))
main()