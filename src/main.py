from typing import Optional
from collaborate_sheets.Database import Database


def checkValid(info: str, tokenNum: int=2) -> list[Optional[str]]:
	"""
	Check if input, split by space, is same of tokenNum.
	:param info: string printed before waiting for input
	:returns: list of given token, contains None if have error.
	"""
	inp = input(info).strip().split()
	if tokenNum == 2 and len(inp) != 2:
		print("Invalid input, make sure both user name and sheet name don't contain space.")
		return [None, None]
	elif tokenNum == 1 and len(inp) != 1:
		print("Name should not contain space.")
		return [None]
	elif tokenNum != len(inp):
		print(f"Token number should be {tokenNum}, get {len(inp)}")
		return [None for c in range(tokenNum)]
	return inp



OPTIONS = """
---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
7. Quit
----------------------------------
"""

if __name__ == '__main__':
	database: Database = Database()
	
	info_sheet = "Input user name and sheet name, splited by space (e.g. \"name title\")\n"
	
	while True:
		print(OPTIONS)
	
		menu_key: str = input("> ")

		# check valid input
		buf: list[str] = []
		user_name: str = ""
		if menu_key == "1":
			buf = checkValid("Input user name without space\n> ", tokenNum=1)
			user_name = buf[0]
		elif menu_key in "23456":
			buf = checkValid(info_sheet + "> ")
			user_name, sheet_title = buf
		if user_name is None:
			continue

		# act based on [menu_key]
		match menu_key:
			case "1":
				database.create_user(user_name)
			case "2":
				database.create_sheet(user_name, sheet_title)
			case "3":
				database.print_sheet(user_name, sheet_title)
			case "4":
				database.edit_sheet(user_name, sheet_title)
			case "5":
				database.change_sheet_accessibility(user_name, sheet_title)
			case "6":
				database.add_sheet_collaborator(user_name, sheet_title)
			case "7":
				print("Goodbye!")
				break
			case _:
				print("Invalid menu key.\n")
				continue

	print()
