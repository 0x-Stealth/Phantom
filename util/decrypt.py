from Cryptodome.Cipher import AES


GCM = AES.MODE_GCM


OFF = -16

class AES256Decrypt:


    @staticmethod
    def decrypt_data(data : bytes , key : bytes):
        # explaining maybe?
        # ok so basically
        # the first 3 bytes are the length of the init vector
        # the next 12 bytes are the init vector
        # the rest is the encrypted data
        # so we get the length of the init vector
        # then we get the init vector
        # then we get the encrypted data
        # then we decrypt the encrypted data
        # then we return the decrypted data



        pay = data [ 15 : ]

        init_vector = data[ 3 : 15 ]


        cipher = AES.new(key , GCM , init_vector)


        return cipher.decrypt(pay)[:OFF].decode()
    # acro your code is so bad
    # i can't even
    # i can't even
    #ok






        
# Bro I can't even test this because I don't have a proxy, and it's horrible opsec on my part to just rawdog it
# I'm sure it works though
    # Maybe(?)
    # I dunno
    # I'm not a bot developer
    # I'm not even a developer, atleast I don't think I am
    # I'm just a guy who knows how to code
    # At what point do you become a developer?
    # I don't know
    # not being able to use discord is nice, i get stuff done
    # but im alone with my thoughts
    # and that's not good
    # i need to be distracted
    # i need to be distracted
    #this playlist goes kinda hard tho https://open.spotify.com/track/5kBWHClnccth6MyPeGVKpm

