from pystegy.utils import imageTool , NoMessage, BadKey
import argparse
import sys
import os


__all__ = ["stegyImage"]

class stegyImage():

    def encode(self, message, src=None, key=None, topics=None, dest = None):
        """hide text inside image data, text can be crypted with key.
        file image could be either given or randomly picked on flicker

        Args:
            message (str): text to hide
            src (str, optional): os path format for source image file. if 'None', random image is picked from flickr. Defaults to None.
            key (str, optional): message encoding key . Defaults to None.
            topics (str, optional): comma separated list of topics used on flickr search for random image. Defaults to None.
            dest (str, optional): os path format for result image file. MUST be 'png' filepath. Defaults to './data/result.png'.
            
        Returns:
            str: path of image file generated

        Raise:
            NoMessage if image havent encrypted datas
            BadKey if the given key is bad
        """
        im = imageTool()
        if src is None:
            if topics is None:
                lst = None
            else:
                lst = topics.split(',')
            im.randomImageAsPng(lst)
        else:
            im.fileReadAsPNG(src, downscale=True)

        im.mark(message, key)

        if dest is None:
            dest = './data/result.png'

        return im.fileWritePNG('', dest)

    def decode(self, filePath, key=None):
        """decode hidden message from image file

        Args:
            filePath (str): path og image file to be decoded
            key (str, optional): message decoding key. Defaults to None.

        Returns:
            [type]: [description]
        """
        im = imageTool()

        im.fileReadAsPNG(filePath)
        return im.read(key)


def main():
    st = stegyImage()
    texte = "un texte qui doit rester secret"
    key = '1a clé d€s champs'

    # fp = st.encode(texte, './data/papillon.jpg', key = key)
    
    fp = st.encode(texte, dest = './data/myresult.png')
    print(fp)

    fp = st.encode(texte, key = key, topics= 'papillon')
    # fp = st.encode(texte, key=key)
    mess = st.decode(fp, key)
    print("------------------------------------")
    fp = st.encode(texte)
    mess = st.decode(fp)
    print("------------------------------------")
    print()
    print(mess)

    # create a image with no message at all
    fp = st.encode("", topics= 'papillon')
    # should raise exception
    try :
        mess = st.decode(fp, key)
    except NoMessage :
        print ('ok, there is no message in it')
        

    fp = st.encode("aaaaaa", key='toto', topics= 'papillon')
    # should raise exception
    try :
        mess = st.decode(fp, key = 'titt')
    except BadKey :
        print ('ok, bad key exceoptioin')
        try :
            mess = st.decode(fp, key = 'toto')
            print('decoded ok with good key')
        except BadKey :
            print ('ok, bad key exceoptioin')
        



if __name__ == "__main__":
    main()
# if __name__ == "__main__":
#     # execute only if run as a script
#     parser = argparse.ArgumentParser(
#         description="write a message in a picture file / read a message from a picture file")
#     # parser.add_argument('-m', '--message', help='the message to write (if none : message is read from the file)')
#     parser.add_argument('-k', '--key', default=None,
#                         help='the encryption key (string)')
#     parser.add_argument('-t', '--topics', default=None,
#                         help='comma separated list of random selected image topics')
#     parser.add_argument(
#         'file_or_message', help='message : hide a message in a randomly choosen picture OR file : extract message from image file (could be http url or filesystem path)')
#     args = parser.parse_args()

#     if not(os.path.isfile(args.file_or_message)):
#         st = stegyImage()
#         fileGenerated = st.encode(args.file_or_message,
#                                  key=args.key, topics=args.topics)
#         sys.stdout.write(fileGenerated)
#     else:
#         st = stegyImage()
#         mess = st.decode(args.file_or_message, key=args.key)
#         sys.stdout.write(mess)

#     sys.stdout.flush()
#     sys.exit()
