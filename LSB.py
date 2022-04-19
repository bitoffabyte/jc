import wave
import os.path

def encode(Audiopath, string_to_encode): 
	'''
	Encode function
	'''
	print("\nEncoding....")
	# read wave audio file
	audio = wave.open(Audiopath, mode="rb")
	# Read frames and convert to byte array
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	# Enter the secret text message
	print(string_to_encode)
	# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
	string_to_encode = string_to_encode + int((len(frame_bytes)-(len(string_to_encode)*8*8))/8) *'#'
	# Convert text to bit array
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string_to_encode])))
	# Replace LSB of each byte of the audio data by one bit from the text bit array
	for i, bit in enumerate(bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit
	# Get the modified bytes	
	frame_modified = bytes(frame_bytes)

	# Save it into a file
	dirname = os.path.dirname(Audiopath)
	newAudio = wave.open(dirname + "/OutputLSB.wav", 'wb')
	newAudio.setparams(audio.getparams())
	newAudio.writeframes(frame_modified)

	newAudio.close()
	audio.close()

	return dirname + "\OutputLSB.wav"

def decode(decoded_audio):
	'''
	Decode function
	'''
	print("\nDecoding...")
	audio = wave.open(decoded_audio, mode='rb')
	# Convert audio to byte array
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))		
	# Extract the LSB of each byte
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	# Convert byte array back to string
	string = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted),8))
	# Cut off at the filler characters
	decoded = string.split("###")[0]
	audio.close()
	return "Decoding completed with hidden message: " + decoded