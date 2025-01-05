

# if __name__ == '__main__':
#     # Example usage
#     restaurant = Restaurant()
#     restaurant.add_menu_item("Pasta", 12.00)
#     restaurant.add_menu_item("Pizza", 15.00)
#     restaurant.add_menu_item("Salad", 8.00)
#
#     # Create a bill for table 1
#     bill = restaurant.create_bill(1, "Alice")
#     bill.add_item(restaurant.menu[0])  # Pasta
#     bill.add_item(restaurant.menu[1])  # Pizza
#
#     # Print the bill
#     bill.print_bill()
#
#     # Split the bill into 2
#     split_bills = restaurant.split_bill(bill, 2)
#     for i, split_bill in enumerate(split_bills, start=1):
#         print(f"\nSplit Bill {i}:")
#         split_bill.print_bill()