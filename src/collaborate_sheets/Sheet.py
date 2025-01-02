from enum import Enum
from typing import List


class Accessibility(Enum):
	EDITABLE = True
	READONLY = False

# change following 2 lines to make users can be notified
_can_notify = False
_user_type = str

class Sheet:
	def __init__(self, owner: str, title: str) -> None:
		self.__sheet: List[List[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.__title: str = title
		self.__owner: _user_type = owner
		self.__accessibility: Accessibility = Accessibility.EDITABLE
		self.__collaborators: List[_user_type] = []

	def _notify_all(self, *args, **kwargs) -> None:
		"""
		prototype function for Observer Pattern.

		"""
		if not _can_notify:
			return
		try:
			self.__owner.update(*args, **kwargs)
			for user in self.__collaborators:
				user.update(*args, **kwargs)
		except Exception as e:
			print("notify faild")
			print(e)
	
	@property
	def title(self) -> str:
		return self.__title

	def is_collaborator(self, user_name: str) -> bool:
		return user_name == self.__owner or user_name in self.__collaborators

	def print(self) -> None:
		print("\n".join([", ".join([str(e) for e in row]) for row in self.__sheet]))

	def edit_content(self, row: int, column: int, value: float) -> bool:
		if self.__accessibility == Accessibility.READONLY:
			print("This sheet is not accessible.")
			return False

		if row < 0 or row >= len(self.__sheet):
			print(f"Row must within range [0, {len(self.__sheet)}).")
			return False

		if len(self.__sheet) != 0 and column < 0 or column >= len(self.__sheet[0]):
			print(f"Column must within range [0, {len(self.__sheet[0])}).")
			return False

		self.__sheet[row][column] = value
		self._notify_all()
		return True

	def change_accessibility(self, accessibility: Accessibility) -> None:
		if accessibility == self.__accessibility:
			print("Accessibility is not changed.")

		self.__accessibility = accessibility

	def add_collaborator(self, user_name: str) -> bool:
		if user_name == self.__owner:
			print(f"User {user_name} is the owner of this sheet.")
			return False

		if user_name in self.__collaborators:
			print(f"User {user_name} has already been a collaborator.")
			return False

		self.__collaborators.append(user_name)
		return True
