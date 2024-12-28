from typing import List, Optional

from collaborate_sheets.Sheet import Accessibility, Sheet

from IfNotNone import IfNotNull, WhenNull
from collaborate_sheets.Existence import *

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

	def _detectExistence(self, option: Existence, name=None, title=None) -> bool:
		"""
		check the user and(or) sheet (not) exists
		set option as: (take user as example)
			USER.TRUE :     if you expect user with `name` exists
			USER.FALSE:     if you expect user with `name` not yet exists
			(don't set it): if you don't care existence of user with `name`
		if there are multiple item to check, use `or` operator.
		:param option: expected state, like `USER.TRUE | SHEET.FALSE` means user should exist but sheet shouldn't
		:param name: user name to check
		:param title: sheet title to check
		:return: True iff the existence meets your expectation
		"""
		classes = [USER, SHEET]
		detect = [
			self.__is_user,
			self.__contain_sheet
		]
		args = [(name,), (title,)]
		msg = [
			[f"User {name} is not existed.", f"User {name} has already existed."],
			[f"Sheet {title} is not existed.", f"Sheet {title} has already existed."]
		]
		for i in range(2):
			if option & classes[i].CARE == 0 or args[i][0] is None:
				continue
			exist = detect[i](*args[i])
			should = (classes[i].SHOULD & option != 0)
			if should and not exist:
				print(msg[i][0])
				return False
			elif not should and exist:
				print(msg[i][1])
				return False
		return True

	def _getAccessableSheet(self, name, title) -> Optional[Sheet]:
		"""
		get sheet if the user with `name` can access the sheet `title`
		:param name: user name
		:param title: sheet title
		:return: the required sheet if user can access the sheet, None else.
		"""
		doIt = self._detectExistence(USER.TRUE | SHEET.TRUE, name, title)
		if not doIt:
			return None
		sheet_index: Optional[int] = self.__find__sheet(title)
		target_sheet: Sheet = self.__sheets[sheet_index]
		if not target_sheet.is_collaborator(name):
			print(f"User {name} don't have right to access this sheet.")
			return None
		return target_sheet

	def create_sheet(self, name: str, title: str) -> None:
		# if not self.__is_user(name):
		# 	print(f"User {name} is not existed.")
		# 	return

		# if self.__contain_sheet(title):
		# 	print(f"Sheet {title} has already existed.")
		# 	return
		if not self._detectExistence(USER.TRUE | SHEET.FALSE, name, title):
			return

		self.__sheets.append(Sheet(name, title))
		print(f"Create a new sheet titled {title} for user {name}.")

	def print_sheet(self, name: str, title: str) -> None:
		# if not self.__is_user(name):
		# 	print(f"User {name} is not existed.")
		# 	return

		# sheet_index: Optional[int] = self.__find__sheet(title)
		# if sheet_index is None:
		# 	print(f"Sheet {title} is not existed.")
		# 	return

		# target_sheet: Sheet = self.__sheets[sheet_index]
		# if not target_sheet.is_collaborator(name):
		# 	print(f"User {name} don't have right to access this sheet.")
		# 	return
		# if not self._detectExistence(USER.TRUE | SHEET.TRUE, name, title):
		# 	return
		target_sheet: Sheet = self._getAccessableSheet(name, title)
		if target_sheet is None:
			return

		print()
		target_sheet.print()

	def edit_sheet(self, name: str, title: str) -> None:
		# if not self.__is_user(name):
		# 	print(f"User {name} is not existed.")
		# 	return
		#
		# sheet_index: Optional[int] = self.__find__sheet(title)
		# if sheet_index is None:
		# 	print(f"Sheet {title} is not existed.")
		# 	return
		#
		# target_sheet: Sheet = self.__sheets[sheet_index]
		# if not target_sheet.is_collaborator(name):
		# 	print(f"User {name} don't have right to access this sheet.")
		# 	return
		target_sheet: Sheet = self._getAccessableSheet(name, title)
		if target_sheet is None:
			return

		print()
		target_sheet.print()
		print()

		row, column, statement = input("Input (row, column, value)\n> ").strip().split(" ")
		try:
			new_value: float = eval(str(statement))
			if target_sheet.edit_content(int(row), int(column), new_value):
				print()
				target_sheet.print()
		except BaseException:
			print(f"Invalid statement {statement}.")

	def change_sheet_accessibility(self, name: str, title: str) -> None:
		# if not self.__is_user(name):
		# 	print(f"User {name} is not existed.")
		# 	return
		#
		# sheet_index: Optional[int] = self.__find__sheet(title)
		# if sheet_index is None:
		# 	print(f"Sheet {title} is not existed.")
		# 	return
		#
		# target_sheet: Sheet = self.__sheets[sheet_index]
		# if not target_sheet.is_collaborator(name):
		# 	print(f"User {name} don't have right to access this sheet.")
		# 	return
		target_sheet: Sheet = self._getAccessableSheet(name, title)
		if target_sheet is None:
			return

		accessibility: str = input("Input either 'ReadOnly' or 'Writable'\n> ").strip()
		match accessibility:
			case "ReadOnly":
				target_sheet.change_accessibility(Accessibility.READONLY)
			case "Writable":
				target_sheet.change_accessibility(Accessibility.EDITABLE)
			case _:
				print("Accessibility must be 'ReadOnly' or 'Writable'.")

	def add_sheet_collaborator(self, name: str, title: str) -> None:
		# if not self.__is_user(name):
		# 	print(f"User {name} is not existed.")
		# 	return

		# sheet_index: Optional[int] = self.__find__sheet(title)
		# if sheet_index is None:
		# 	print(f"Sheet {title} is not existed.")
		# 	return

		# target_sheet: Sheet = self.__sheets[sheet_index]
		# if not target_sheet.is_collaborator(name):
		# 	print(f"User {name} don't have right to access this sheet.")
		# 	return
		target_sheet: Sheet = self._getAccessableSheet(name, title)
		if target_sheet is None:
			return

		collaborator: str = input("Input a user to share to\n> ").strip()
		if not self.__is_user(collaborator):
			print(f"User {collaborator} is not existed.")
			return

		if target_sheet.add_collaborator(collaborator):
			print(f"Share user {name}'s sheet {title} with user {collaborator}.")
