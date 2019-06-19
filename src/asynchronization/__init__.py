from os.path import abspath, join, dirname, basename

# sys.dont_write_bytecode = True
# sys.path.insert(0, join(dirname(__file__)))

if __name__ == "__main__":
	print(dirname(__file__))
	print(abspath(__file__))
	print(basename(__file__))
	print(dirname(abspath(__file__)))