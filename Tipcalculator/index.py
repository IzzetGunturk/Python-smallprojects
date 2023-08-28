def calculate_tip(bill_amount, tip_percentage, person_amount):
    total_bill = bill_amount * (tip_percentage / 100)
    total_per_person = total_bill / person_amount
    return total_bill, total_per_person

devide = "\n---------------------------------------------------------------------\n"

def main():
    try:
        bill_amount = float(input("Enter the bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage: %"))
        person_amount = int(input("Enter the number of persons: "))

        print(devide)

        total_bill, total_per_person = calculate_tip(bill_amount, tip_percentage, person_amount)
        
        total_everything = total_bill + bill_amount
        
        print(f"Total tip: ${total_bill:.2f}")
        print(f"Tip per person: ${total_per_person:.2f}")
        print(f"Total (bill + tip): ${total_everything:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
