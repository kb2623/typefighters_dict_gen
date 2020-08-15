import re
from argparse import ArgumentParser


argsparser = ArgumentParser(description='Generate custome dictionay for TypeFighters game.', add_help=False)
argsparser.add_argument('-o', '--out', dest='out_file', type=str, default='out_dict.txt', required=False, help='Name of the output file.')
argsparser.add_argument('-h', '-?', '--help', dest='help', action='store_true', required=False, help='Print this message.')
argsparser.add_argument('documents', metavar='FILES', type=str, nargs='+', help='Input files with text.')


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


def remove_digits(data):
	r"""Remove all digits from data list.

	Args:
		data (List[str]): List of data.

	Returns:
		List[str]: List of data without digigts.
	"""
	data, ndata = [''.join(x for x in i if x.isalpha()) for i in data], []
	for e in data:
		if e is '': continue
		elif e is None: continue
		else: ndata.append(e)
	return ndata


def process(out_file='', documents=None, *args, **kwargs):
	r"""Process the inpurt courpses.

	Args:
		out_file (str): Path and file name of the output.
		documents (list): List of file names to process and combine into corpus.
		args (list): TODO.
		kwargs (dict): TODO.
	"""
	if documents is None: return
	data, wmatcher = [], re.compile(ur'\w+', re.UNICODE)
	for doc in documents:
		e = None
		with open(doc, 'r') as file: e = file.read()
		e = wmatcher.findall(e.decode('utf8'))
		data.extend(e)
	data = u' '.join(x for x in sorted(list(set(remove_digits(data))), cmp=cmp_func)).encode('utf-8').replace(' ', '\n')
	with open(out_file, 'w') as file: file.write(data)


if __name__ == '__main__':
	args = argsparser.parse_args()
	if args.help: argsparser.print_help()
	else: process(**vars(args))


# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
