from crud import create_customer, create_product, create_order, get_customers, get_orders, get_products, update_product_price, delete_customer

def make_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    create_customer(name, email)
    print(f"Customer {name} created!")


def make_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter the quantity: "))
    create_product(name, price, stock)
    print(f"Product {name} added!")


def make_order():
    customer_id = int(input("Enter customer ID to create order for: "))
    product_quantities = {}

    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == "done":
            break
    quantity = int(input(f"Enter quantity for {product_name}: "))
    product_quantities[product_name] = quantity

    try:
        create_order(customer_id, product_quantities)
        print(f"Order Created for customer ID {customer_id}")
    except Exception as e:
        print(f"Failed to create order: {e}")


def main():
    while True:
        print("===Store Manegement System")
        print("1. Create Customer")
        print("2. Create Product")
        print("3. Create Order")
        print("4. View Customers")
        print("5. View Customers")
        print("6. View Orders")
        print("7. Update Product Price")
        print("8. Delete Customer")
        print("9. Exit")

        option = input("Select an option (1 - 9): ")

        if option == "1":
            make_customer()
        elif option == "2":
            make_product()
        elif option == "3":
            make_order()
        elif option == "4":
            print("Customer: ", get_customers())
        elif option == "5":
            print("Products: ", get_products())
        elif option == "6":
            print("Order: ", get_orders())
        elif option == "7":
            product_id = int(input("Enter product ID to update price: "))
            new_price = float(input("Enter new price: "))
            update_product_price(product_id, new_price)
            print("New Price Updated!")
        elif option == "8":
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
            print("Customer Deleted!")
        elif option == "9":
            print("Exiting the application!")
            break
        else:
            print("Invalid Choice, Try Again")

if __name__ == "__main__":
    main()
