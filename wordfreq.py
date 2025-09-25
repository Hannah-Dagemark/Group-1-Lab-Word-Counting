from enum import Enum


class CharType(Enum):
	NONE = 0
	DIGIT = 1
	ALPHA = 2
	SPACE = 3
	SYMBOL = 4


def char_type(char: str) -> CharType:
	if char.isdigit():
		return CharType.DIGIT
	elif char.isalpha():
		return CharType.ALPHA
	elif char == " ":
		return CharType.SPACE
	return CharType.SYMBOL


def tokenize(lines: list[str]) -> list[str]:
	result = []
	for line in lines:
		word_type = CharType.NONE
		current_word = []
		for i, char in enumerate(line.lower()):
			if len(current_word) == 0:
				ct = char_type(char)
				if ct == CharType.SPACE:
					continue
				if ct == CharType.SYMBOL:
					result.append(char)
					continue
				word_type = ct
			current_word.append(char)
			if i+1 >= len(line) or word_type != char_type(line[i+1]):
				result.append("".join(current_word))
				current_word = []
	return result
