'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the “compressed” string would not become smaller than the original
string, your method should return the original string.
'''
class StringCompression(object):
	def __init__(self, given_input, is_compressed):

		if is_compressed:
			self.compressed_string = given_input
			self.decompress()

		else:
			self.string = given_input
			self.createMap()
			self.compressed_string = self.compressedString()

	def createMap(self):
		self.compressed_map = []
		letter = self.string[0]
		rep = 1

		for candLetter in self.string[1:]:
			# if we see the same letter count
			if candLetter == letter:
				rep += 1
			# if we see something different store value and start new count
			else:
				self.compressed_map.append((letter, rep))
				letter = candLetter
				rep = 1

		# takes care of the last guy
		self.compressed_map.append((letter, rep))

	def compressedString(self):
		compression = ''
		for tup in self.compressed_map:
			compression += "%s%s" % (tup[0], tup[1])
		return compression

	def decompress(self):
		decompress = ''
		for letter, freq in zip(name[0::2], name[1::2]):
			for num in range(int(freq)):
				decompress += letter

		self.string = decompress

	def get_string(self):
		return self.string

	def get_compressed_string(self):
		if len(self.compressed_string) < len(self.string):
			return self.compressed_string
		else:
			return self.string