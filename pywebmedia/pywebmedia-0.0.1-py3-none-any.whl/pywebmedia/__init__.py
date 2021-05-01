import shutil
import requests

class PyWebMedia():
    class download():
        def favicon(domain, file_name, save_location):
            try:
                url = 'https://www.google.com/s2/favicons?domain=' + domain
                response = requests.get(url, stream=True)
                Save = save_location + file_name + ".ico"
                with open(Save, 'wb') as OUTPUT:
                    shutil.copyfileobj(response.raw, OUTPUT)
                    print("Connecting to " + url)
                    print("File Downloaded SucessFully.")
            except Exception as Error:
                print(Error)
                print("Failed To Download!")

        def image(url, file_name, format, save_location):
            try:
                print("Connecting to " + url)
                response = requests.get(url, stream=True)
                Save = save_location + file_name + format
                with open(Save, 'wb') as OUTPUT:
                    shutil.copyfileobj(response.raw, OUTPUT)
                    print("File Downloaded SucessFully.")
            except Exception as Error:
                print(Error)
                print("Failed To Download!")

        def video(url, file_name, format, save_location):
            try:
                print("Connecting to " + url)
                response = requests.get(url, stream=True)
                Save = save_location + file_name + format
                with open(Save, 'wb') as OUTPUT:
                    shutil.copyfileobj(response.raw, OUTPUT)
                    print("File Downloaded SucessFully.")
            except Exception as Error:
                print(Error)
                print("Failed To Download!")

        def gif(url, file_name, save_location):
            try:
                print("Connecting to " + url)
                response = requests.get(url, stream=True)
                Save = save_location + file_name + ".gif"
                with open(Save, 'wb') as OUTPUT:
                    shutil.copyfileobj(response.raw, OUTPUT)
                    print("File Downloaded SucessFully.")
            except Exception as Error:
                print(Error)
                print("Failed To Download!")

        def audio(url, file_name, format, save_location):
            try:
                print("Connecting to " + url)
                response = requests.get(url, stream=True)
                Save = save_location + file_name + format
                with open(Save, 'wb') as OUTPUT:
                    shutil.copyfileobj(response.raw, OUTPUT)
                    print("File Downloaded SucessFully.")
            except Exception as Error:
                print(Error)
                print("Failed To Download!")
