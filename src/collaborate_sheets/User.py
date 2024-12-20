class User:
	def __init__(self, name: str) -> None:
		self.__name: str = name

	def __eq__(self, value: object, /) -> bool:
		pass
