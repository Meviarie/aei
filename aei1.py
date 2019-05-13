import codecs, re 
from clp3 import clp

def word_stat(filename):
	'''
	Zwraca posortowaną malejąco statystykę wystąpień słów
	w pliku w postaci listy par (słowo, liczba).
	'''

	# Funkcje pomocnicze

	def _words_from_line(line):
		words = re.split('[\W\d]+', line)
		return [w.lower() for w in words if w]

	def _sort_stat(stat):
		"Sortuje malejąco listę par według drugiego elementu."
		return sorted(stat, key=lambda p: p[1], reverse=True)

	d = dict()
	n = 1
	nr = 1

	file = open(filename, 'r', encoding="utf8")
	for line in file:
		words = _words_from_line(line)
		if words:
			for word in words:
				if word in d.keys():
					d[word] = d[word]+1
				else:
					d[word] = n
		else:
			result = list(d.items())
			print('Tekst nr', nr,  ': \n')
			nr=nr+1
			n=1
			d.clear()
			print(_sort_stat(result),'\n')
	return 1
print(word_stat('tekstyaei.txt'))



#później: liczymy słownik z listą wyrazów ułożoną tak, że mamy tekst i w nim listę wyrazów i częstość występowania każdego z nich
#znaleźć swoje teksty z zajęć
