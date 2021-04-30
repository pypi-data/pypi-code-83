class RSA:
	@classmethod
	def __format_list(cls, L):
		shift = max([len(str(s)) for s in L])
		for i in range(len(L)):
			nb = str(L[i])
			while len(nb) < shift:
				nb = "0" + nb
			L[i] = nb
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
	def __inverse_modulaire(cls, e, m):
		for d in range(1, m):
			if (e * d) % m == 1:
				return d

	@classmethod
	def __pgcd(cls, nb1, nb2):
		while nb2 > 0:
			nb1, nb2 = nb2, nb1 % nb2
		return nb1

	@classmethod
	def __RSA(cls, content, key):
		new_content = []
		for nb in content:
			new_content.append((int(nb)**key[1] % key[0]))
		return new_content

	@classmethod
	def get_keys(cls, p, q, e=None):
		assert p * q > 9999, "p * q must be superior to 9999"

		Tn = (p - 1) * (q - 1)
		if e is not None:
			assert cls.__pgcd(e, Tn) == 1, "e et (p - 1) * (q - 1) doivent être premiers entre eux"
		else:
			for e in range(2, Tn):
				if cls.__pgcd(e, Tn) == 1: break
		
		return {"public_key": (p * q, e), "private_key": (p * q, cls.__inverse_modulaire(e, Tn))}

	@classmethod
	def Encryption(cls, inp, key, type_of_entry="text"):
		assert type_of_entry in ["text", "file"], "type_of_entry peut prendre les valeures : 'text' ou 'file'"
	
		if type_of_entry == "text":
			plain_text = [ord(char) for char in inp]
		elif type_of_entry == "file":
			plain_text = [ord(char) for char in open(inp, "r").read()]
	
		plain_text = cls.__format_list(plain_text)
		plain_text = cls.__cut_list(plain_text, 4)
		encrypted_text = cls.__RSA(plain_text, key)

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

		plain_text = cls.__RSA(encrypted_text, key)
		plain_text = cls.__format_list(plain_text)
		plain_text = cls.__cut_list(plain_text, 3)
		
		if type_of_entry == "text":
			return "".join([chr(int(char)) for char in plain_text])
		elif type_of_entry == "file":
			open(inp, "w").write("".join([chr(int(char)) for char in plain_text]))
