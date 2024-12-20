from collaborate_sheets.Database import Database

database: Database = Database()

while True:
	print("""
---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
7. Quit
----------------------------------
	""")

	menu_key: str = input("> ")

	match menu_key:
		case "1":
			user_name: str = input("> ").strip()
			database.create_user(user_name)
		case "2":
			user_name, sheet_title = input("> ").strip().split(" ")
			database.create_sheet(user_name, sheet_title)
		case "3":
			user_name, sheet_title = input("> ").strip().split(" ")
			database.print_sheet(user_name, sheet_title)
		case "4":
			user_name, sheet_title = input("> ").strip().split(" ")
			database.edit_sheet(user_name, sheet_title)
		case "5":
			user_name, sheet_title = input("> ").strip().split(" ")
			database.change_sheet_accessibility(user_name, sheet_title)
		case "6":
			user_name, sheet_title = input("> ").strip().split(" ")
			database.add_sheet_collaborator(user_name, sheet_title)
		case "7":
			print("Goodbye!")
			break
		case _:
			print("Invalid menu key.\n")
			continue

	print()
