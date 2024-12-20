from typing import List, Optional

from collaborate_sheets.Sheet import Accessibility, Sheet


class Database:
	def __init__(self) -> None:
		self.__sheets: List[Sheet] = []
		self.__users: List[str] = []

	def __is_user(self, name: str) -> bool:
		return name in self.__users

	def create_user(self, name: str) -> None:
		print()
		if self.__is_user(name):
			print(f"User {name} has already existed.")
			return

		self.__users.append(name)
		print(f"Create a new user named {name}.")

	def __find__sheet(self, title: str) -> Optional[int]:
		for index, sheet in enumerate(self.__sheets):
			if title == sheet.title:
				return index

		return None

	def __contain_sheet(self, title: str) -> bool:
		return self.__find__sheet(title) is not None

	def create_sheet(self, name: str, title: str) -> None:
		if not self.__is_user(name):
			print(f"User {name} is not existed.")
			return

		if self.__contain_sheet(title):
			print(f"Sheet {title} has already existed.")
			return

		self.__sheets.append(Sheet(name, title))
		print(f"Create a new sheet titled {title} for user {name}.")

	def print_sheet(self, name: str, title: str) -> None:
		if not self.__is_user(name):
			print(f"User {name} is not existed.")
			return

		sheet_index: Optional[int] = self.__find__sheet(title)
		if sheet_index is None:
			print(f"Sheet {title} is not existed.")
			return

		target_sheet: Sheet = self.__sheets[sheet_index]
		if not target_sheet.is_collaborator(name):
			print(f"User {name} don't have right to access this sheet.")
			return

		print()
		target_sheet.print()

	def edit_sheet(self, name: str, title: str) -> None:
		if not self.__is_user(name):
			print(f"User {name} is not existed.")
			return

		sheet_index: Optional[int] = self.__find__sheet(title)
		if sheet_index is None:
			print(f"Sheet {title} is not existed.")
			return

		target_sheet: Sheet = self.__sheets[sheet_index]
		if not target_sheet.is_collaborator(name):
			print(f"User {name} don't have right to access this sheet.")
			return

		print()
		target_sheet.print()
		print()

		row, column, statement = input("> ").strip().split(" ")
		try:
			new_value: float = eval(str(statement))
			if target_sheet.edit_content(int(row), int(column), new_value):
				print()
				target_sheet.print()
		except BaseException:
			print(f"Invalid statement {statement}.")

	def change_sheet_accessibility(self, name: str, title: str) -> None:
		if not self.__is_user(name):
			print(f"User {name} is not existed.")
			return

		sheet_index: Optional[int] = self.__find__sheet(title)
		if sheet_index is None:
			print(f"Sheet {title} is not existed.")
			return

		target_sheet: Sheet = self.__sheets[sheet_index]
		if not target_sheet.is_collaborator(name):
			print(f"User {name} don't have right to access this sheet.")
			return

		accessibility: str = input("> ").strip()
		match accessibility:
			case "ReadOnly":
				target_sheet.change_accessibility(Accessibility.READONLY)
			case "Writable":
				target_sheet.change_accessibility(Accessibility.EDITABLE)
			case _:
				print("Accessibility must be 'ReadOnly' or 'Writable'.")

	def add_sheet_collaborator(self, name: str, title: str) -> None:
		if not self.__is_user(name):
			print(f"User {name} is not existed.")
			return

		sheet_index: Optional[int] = self.__find__sheet(title)
		if sheet_index is None:
			print(f"Sheet {title} is not existed.")
			return

		target_sheet: Sheet = self.__sheets[sheet_index]
		if not target_sheet.is_collaborator(name):
			print(f"User {name} don't have right to access this sheet.")
			return

		collaborator: str = input("> ").strip()
		if not self.__is_user(collaborator):
			print(f"User {collaborator} is not existed.")
			return

		if target_sheet.add_collaborator(collaborator):
			print(f"Share user {name}'s sheet {title} with user {collaborator}.")
