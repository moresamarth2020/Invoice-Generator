def invoice_generator():
    print("----- INVOICE GENERATOR -----\n")

    customer_name = input("Customer Name: ")
    items = []

    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == "done":
            break

        quantity = int(input("Quantity: "))
        price = float(input("Price per item: "))

        items.append({
            "item": item_name,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        })
        print("Item added!\n")

    print("\n--------- INVOICE ---------")
    print("Customer:", customer_name)
    print("---------------------------")

    grand_total = 0
    for item in items:
        print(f"{item['item']} | Qty: {item['quantity']} | ₹{item['total']}")
        grand_total += item["total"]

    tax = grand_total * 0.05
    final_amount = grand_total + tax

    print("---------------------------")
    print("Subtotal:", grand_total)
    print("Tax (5%):", tax)
    print("Total Payable:", final_amount)
    print("---------------------------")

invoice_generator()
