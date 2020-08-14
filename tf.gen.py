import re
import sys


def help():
	print('Usage:')
	print('python tf.gen.py [FILES]')


def cmp_func(a, b):
	r"""Comparator for sorting list of stirngs.

	Args:
		a (str): First string.
		b (str): Second string.

	Returns:
		int: Value of comparation.
	"""
	if len(a) == len(b): return cmp(a, b)
	else: return cmp(len(a), len(b))


def process(*args):
	r"""Process the inpurt courpses.

	Args:
		args (list): List of file names to process and combine into corpus.
	"""
	data = []
	for doc in args:
		e = None
		with open(doc, 'r') as file: e = file.read().lower()
		e = re.findall(r'\w+', e)
		data.extend(e)
	data.sort()
	data = '\n'.join(map(str, sorted(list(set(data)), cmp=cmp_func)))
	with open('out.txt', 'w') as file: file.write(data)


if __name__ == '__main__':
	if len(sys.argv) < 2: help()
	else: process(*sys.argv[1:])


# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
