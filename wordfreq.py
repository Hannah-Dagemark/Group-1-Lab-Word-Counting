from enum import Enum


class CharType(Enum):
	NONE = 0
	DIGIT = 1
	ALPHA = 2
	WHITESPACE = 3
	SYMBOL = 4


def char_type(char: str) -> CharType:
	if char.isdigit():
		return CharType.DIGIT
	elif char.isalpha():
		return CharType.ALPHA
	elif char == " " or char == "	":
		return CharType.WHITESPACE
	return CharType.SYMBOL


def tokenize(lines: list[str]) -> list[str]:
	result = []
	for line in lines:
		word_type = CharType.NONE
		current_word = []
		for i, char in enumerate(line.strip().lower()):
			if len(current_word) == 0:
				ct = char_type(char)
				if ct == CharType.WHITESPACE:
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


def countWords(words, stopWords = []):
	dict = {}
	for word in words:
		if word not in stopWords:
			if word in dict.keys():
				dict[word] += 1
			else:
				dict[word] = 1
	return(dict)

def printTopMost(frequencies,n):
    list = []
    
    for word,freq in frequencies.items():
        list.append((word,freq))
    list = sorted(list, key=lambda x: -x[1])
    for i in range (0, n):
        if len(list)-1 >= i:
	        print(list[i][0].ljust(19),str(list[i][1]).rjust(5))