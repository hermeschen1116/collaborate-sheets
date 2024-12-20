from src.collaborate_sheets.Database import Database


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

	menu_key: int = int(input("> "))

	match(menu_key):
		case 1:
			user_name: str = input("> ")
			# TODO: function to create a user
		case 2:
			user_name, sheet_title = input("> ").split(' ')
			# TODO: function to create a sheet
		case 3:
			user_name, sheet_title = input("> ").split(' ')
			# TODO: function to print a sheet
		case 4:
			user_name, sheet_title = input("> ").split(' ')
			# TODO: function to modify a sheet
		case 5:
			user_name, sheet_title, access_right = input("> ").split(' ')
			# TODO: function to modify access right
		case 6:
			user_name, sheet_title, collaborator_name = input("> ").split(' ')
			# TODO: function to add collaborator
		case 7:
			print("Goodbye!")
			break
		case _:
			print("Invalid menu key.")
			continue

	print()
