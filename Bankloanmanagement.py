class Loan:
    def __init__(self, customer_id, loan_amount, interest_rate, loan_term):
        self.customer_id = customer_id
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100 / 12  # Convert to monthly interest rate
        self.loan_term = loan_term * 12  # Convert years to months

    def calculate_interest(self):
        # Calculate total interest over the loan term
        interest = self.loan_amount * self.interest_rate * self.loan_term
        return interest

    def generate_payment_schedule(self):
        # Monthly payment calculation using the amortizing loan formula
        if self.loan_term > 0:
            monthly_payment = (self.loan_amount * self.interest_rate) / (1 - (1 + self.interest_rate) ** -self.loan_term)
            return monthly_payment
        return 0

class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

class Bank:
    def __init__(self):
        self.customers = {}
        self.loans = {}

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.customer_id} added.")
        else:
            print("Customer ID already exists.")

    def update_customer(self, customer_id, name=None, address=None):
        customer = self.customers.get(customer_id)
        if customer:
            if name:
                customer.name = name
            if address:
                customer.address = address
            print(f"Customer {customer_id} updated.")
        else:
            print("Customer not found.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} deleted.")
        else:
            print("Customer not found.")

    def add_loan(self, loan):
        if loan.customer_id in self.customers:
            self.loans[loan.customer_id] = loan
            print(f"Loan for Customer {loan.customer_id} added.")
        else:
            print("Customer not found. Please add customer first.")

    def update_loan(self, customer_id, loan_amount=None, interest_rate=None, loan_term=None):
        loan = self.loans.get(customer_id)
        if loan:
            if loan_amount:
                loan.loan_amount = loan_amount
            if interest_rate:
                loan.interest_rate = interest_rate / 100 / 12  # Convert to monthly interest rate
            if loan_term:
                loan.loan_term = loan_term * 12  # Convert years to months
            print(f"Loan for Customer {customer_id} updated.")
        else:
            print("Loan not found.")

    def delete_loan(self, customer_id):
        if customer_id in self.loans:
            del self.loans[customer_id]
            print(f"Loan for Customer {customer_id} deleted.")
        else:
            print("Loan not found.")

    def display_customers(self):
        if not self.customers:
            print("No customers found.")
        else:
            print("\nCustomer ID   Name                Address")
            print("===============================================")
            for customer in self.customers.values():
                print(f"{customer.customer_id:<15}{customer.name:<20}{customer.address:<20}")

    def display_loans(self):
        if not self.loans:
            print("No loans found.")
        else:
            print("\nCustomer ID   Loan Amount    Interest Rate (%)    Loan Term (Years)")
            print("=============================================================")
            for loan in self.loans.values():
                interest_rate = loan.interest_rate * 100 * 12  # Convert back to annual percentage
                loan_term_years = loan.loan_term // 12  # Convert months to years
                print(f"{loan.customer_id:<15}{loan.loan_amount:<15.2f}{interest_rate:<20.2f}{loan_term_years:<20}")

    def get_customer_details(self, customer_id):
        customer = self.customers.get(customer_id)
        loan = self.loans.get(customer_id)
        
        if customer:
            print(f"Customer ID: {customer.customer_id}")
            print(f"Name: {customer.name}")
            print(f"Address: {customer.address}")

            if loan:
                print(f"Loan Amount: {loan.loan_amount}")
                print(f"Interest Rate: {loan.interest_rate * 100 * 12:.2f}%")
                print(f"Loan Term: {loan.loan_term // 12} years")
            else:
                print("No loan found for this customer.")
        else:
            print("Customer not found.")

def main():
    bank = Bank()

    while True:
        print("\n=== Bank Loan Management System ===")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Add Loan")
        print("5. Update Loan")
        print("6. Delete Loan")
        print("7. Calculate Interest")
        print("8. Generate Payment Schedule")
        print("9. View Customer and Loan Details")
        print("10. Display All Customers")
        print("11. Display All Loans")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            customer = Customer(customer_id, name, address)
            bank.add_customer(customer)

        elif choice == "2":
            customer_id = input("Enter customer ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            bank.update_customer(customer_id, name, address)

        elif choice == "3":
            customer_id = input("Enter customer ID to delete: ")
            bank.delete_customer(customer_id)

        elif choice == "4":
            customer_id = input("Enter customer ID for the loan: ")
            loan_amount = float(input("Enter loan amount: "))
            interest_rate = float(input("Enter interest rate (as a percentage): "))
            loan_term = int(input("Enter loan term (in years): "))
            loan = Loan(customer_id, loan_amount, interest_rate, loan_term)
            bank.add_loan(loan)

        elif choice == "5":
            customer_id = input("Enter customer ID to update loan: ")
            loan_amount = input("Enter new loan amount (leave blank to skip): ")
            interest_rate = input("Enter new interest rate (leave blank to skip): ")
            loan_term = input("Enter new loan term in years (leave blank to skip): ")
            bank.update_loan(customer_id,
                             float(loan_amount) if loan_amount else None,
                             float(interest_rate) if interest_rate else None,
                             int(loan_term) if loan_term else None)

        elif choice == "6":
            customer_id = input("Enter customer ID to delete loan: ")
            bank.delete_loan(customer_id)

        elif choice == "7":
            customer_id = input("Enter customer ID to calculate interest: ")
            loan = bank.loans.get(customer_id)
            if loan:
                interest = loan.calculate_interest()
                print(f"Total interest over the loan term: {interest:.2f}")
            else:
                print("Loan not found.")

        elif choice == "8":
            customer_id = input("Enter customer ID to generate payment schedule: ")
            loan = bank.loans.get(customer_id)
            if loan:
                monthly_payment = loan.generate_payment_schedule()
                print(f"Monthly Payment: {monthly_payment:.2f}")
            else:
                print("Loan not found.")
        elif choice == "9":
            customer_id = input("Enter customer ID to view details: ")
            bank.get_customer_details(customer_id)

        elif choice == "10":
            bank.display_customers()

        elif choice == "11":
            bank.display_loans()

        elif choice == "12":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()