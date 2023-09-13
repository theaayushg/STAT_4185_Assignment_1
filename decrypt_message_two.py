encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Create an empty string to store the decrypted message
decrypted_message = ""

start = 0
end = len(encrypted_message) - 2
while start <= end:
    decrypted_message += encrypted_message[start]
    if start != end:
        decrypted_message += encrypted_message[end]
    start += 2
    end -= 2
decrypted_message += encrypted_message[-3]
decrypted_message += encrypted_message[-1]

print(decrypted_message)
