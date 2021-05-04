import PIL.Image
import PIL.TiffTags

def dumpexif(im, fix = True):
    exif = im.getexif()

    if fix:
        ImageWidthExifTag = 0x0100
        if (ImageWidthExifTag not in exif):
            exif[ImageWidthExifTag] = im.width

        ImageLengthExifTag = 0x0101
        if (ImageLengthExifTag not in exif):
            exif[ImageLengthExifTag] = im.height

    for tag, value in sorted(exif.items()):
        tag_info = PIL.TiffTags.lookup(tag)
        if (tag_info.name not in ['ExifIFD']):
            if isinstance(value, bytes):
                value = value.decode('utf-8')

            print(f'{tag_info.name}: {value}')
