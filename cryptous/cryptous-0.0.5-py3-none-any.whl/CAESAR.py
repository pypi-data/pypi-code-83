class CAESAR:
	@classmethod
	def __format_list(cls, L):
		shift = max([len(str(s)) for s in L])
		for i in range(len(L)):
			nb = str(L[i])
			while len(nb) < shift:
				nb = "0" + nb
			L[i] = nb
		L[-1] = str(int(L[-1]))
		return L

	@classmethod
	def __cut_list(cls, L, shift):
		L = "".join(L)
		new_L, buffer, it = [], "", 0
		for char in L:
			buffer += char
			it += 1
			if it == shift:
				new_L.append(buffer)
				buffer, it = "", 0
		if len(buffer) > 0:
			new_L.append(buffer)
		return new_L

	@classmethod
	def __CAESAR(cls, content, key):
		encrypted_content = []
		for i in range(len(content)):
			encrypted_content.append(int(content[i])+key)
		return encrypted_content

	@classmethod
	def Encryption(cls, inp, key, type_of_entry="text", frequency_analysis_protection=False):
		assert type_of_entry in ["text", "file"], "type_of_entry peut prendre les valeures : 'text' ou 'file'"
	
		if type_of_entry == "text":
			plain_text = [ord(char) for char in inp]
		elif type_of_entry == "file":
			plain_text = [ord(char) for char in open(inp, "r").read()]

		if frequency_analysis_protection:
			plain_text = cls.__format_list(plain_text)
			plain_text = cls.__cut_list(plain_text, 4)
		encrypted_text = cls.__CAESAR(plain_text, key)

		if type_of_entry == "text":
			return " ".join([str(nb) for nb in encrypted_text])
		elif type_of_entry == "file":
			open(inp, "w").write(" ".join([str(nb) for nb in encrypted_text]))

	@classmethod
	def Decryption(cls, inp, key, type_of_entry="text", frequency_analysis_protection=False):
		assert type_of_entry in ["text", "file"], "type_of_entry peut prendre les valeures : 'text' ou 'file'"
	
		if type_of_entry == "text":
			encrypted_text = [int(nb) for nb in inp.split(" ")]
		elif type_of_entry == "file":
			encrypted_text = [int(nb) for nb in open(inp, "r").read().split(" ")]
		
		plain_text = cls.__CAESAR(encrypted_text, -key)
		if frequency_analysis_protection:
			plain_text = cls.__format_list(plain_text)
			plain_text = cls.__cut_list(plain_text, 3)

		if type_of_entry == "text":
			return "".join([chr(int(char)) for char in plain_text])
		elif type_of_entry == "file":
			open(inp, "w").write("".join([chr(int(char)) for char in plain_text]))
