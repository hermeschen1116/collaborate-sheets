# implement an object for sheet

from enum import Enum
from typing import List

from collaborate_sheets.User import User

class AccessRight(Enum):
	WRITABLE = "Writable"
	READONLY = "ReadOnly"

class Sheet:
	def __init__(self, owner: User) -> None:
		self.__sheet: List[List[int]] = []
		self.__owner: User = owner
		self.__access_right: AccessRight = AccessRight.WRITABLE
		self.__collaborators: List[User] = []

	def print_sheet(self) -> None:
		if len(self.__sheet) == 0:
			p
