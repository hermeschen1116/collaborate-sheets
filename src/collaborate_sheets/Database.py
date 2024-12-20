from typing import List

from collaborate_sheets.Sheet import Sheet
from collaborate_sheets.User import User


class Database:
	def __init__(self) -> None:
		self.__sheets: List[Sheet] = []
		self.__users: List[User] = []

	def create_user(self, name: str) -> bool:
		if name in self.__users:
			return False
