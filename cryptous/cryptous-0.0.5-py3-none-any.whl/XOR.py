class XOR:
	@classmethod
	def __get_key(cls, key_chars):
		key_dec = []
		for char in key_chars:
			key_dec.append(ord(char))
		return key_dec

	@classmethod
	def __XOR(cls, content, key):
		encrypted_content = []
		for i in range(len(content)):
			char = content[i]
			key_index = i % len(key)
			encrypted_content.append(char^key[key_index])
		return encrypted_content

	@classmethod
	def Encryption(cls, inp, key, type_of_entry="text"):
		assert type_of_entry in ["text", "file"], "type_of_entry peut prendre les valeures : 'text' ou 'file'"

		if type_of_entry == "text":
			plain_text = [ord(char) for char in inp]
		elif type_of_entry == "file":
			plain_text = [ord(char) for char in open(inp, "r").read()]

		key = cls.__get_key(key)
		encrypted_text = cls.__XOR(plain_text, key)

		if type_of_entry == "text":
			return " ".join([str(nb) for nb in encrypted_text])
		elif type_of_entry == "file":
			open(inp, "w").write(" ".join([str(nb) for nb in encrypted_text]))

	@classmethod
	def Decryption(cls, inp, key, type_of_entry="text"):
		assert type_of_entry in ["text", "file"], "type_of_entry peut prendre les valeures : 'text' ou 'file'"
	
		if type_of_entry == "text":
			encrypted_text = [int(nb) for nb in inp.split(" ")]
		elif type_of_entry == "file":
			encrypted_text = [int(nb) for nb in open(inp, "r").read().split(" ")]

		key = cls.__get_key(key)
		plain_text = cls.__XOR(encrypted_text, key)

		if type_of_entry == "text":
			return "".join([chr(int(char)) for char in plain_text])
		elif type_of_entry == "file":
			open(inp, "w").write("".join([chr(int(char)) for char in plain_text]))
