import sys
import wordfreq
import urllib.request





def main():
    stop_word_file = sys.argv[1]
    word_file = sys.argv[2]
    amount_of_words = int(sys.argv[3])

    if "https" in word_file:
        response = urllib.request.urlopen(word_file)
        lines = response.read().decode("utf8").splitlines()
    else:
        inp_file = open(word_file, encoding="utf-8")
        lines = inp_file.readlines()
        inp_file.close()
    tokenized = wordfreq.tokenize(lines)

    stop_word_lines = open(stop_word_file, encoding="utf-8")
    stop_words = stop_word_lines.read().split("\n")
    stop_word_lines.close()

    counted_words = wordfreq.countWords(tokenized, stop_words)

    wordfreq.printTopMost(counted_words, amount_of_words)


main()