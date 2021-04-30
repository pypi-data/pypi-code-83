from taskhub.server import serve
address = "127.0.0.1"

if __name__ == "__main__":
    serve(
        port=2333, 
        passwd="1qaz2wsx", 
        back_end_url="http://{}/api/grab/web/data/".format(address))
