def encrypt_decrypt(inFile, outFile):
	fr = open(inFile, "rb")
	fw = open(outFile, "wb")
	count = 0

	try:
		byte1 = fr.read(1)

		while byte1 != b'':
			count += 1
			
			byte2 = fr.read(1)
			
			if byte2 != b'':
				count += 1
				#swap bytes
				fw.write(byte2)
				fw.write(byte1)		

			else:
				fw.write(byte1)
				break

			if count % 10000 == 0:
				print(str(count / 1000) + "KB done...")

			byte1 = fr.read(1)		       

	finally:
		fr.close()
		fw.close()

#encrypt_decrypt(inFile, outFile)
#print("Done...")

print("\n\n*** Simple encryption started... ***\n")
inFile = input("Enter Target file name with full path: ")
outFile = inFile[0:inFile.rfind('.')] + "-BYTE_CORRUPTED" + inFile[inFile.rfind('.'):]

encrypt_decrypt(inFile, outFile)
print("Done...\n")