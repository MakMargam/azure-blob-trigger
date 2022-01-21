import logging

import azure.functions as func
from PIL import Image

def main(myblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    with open('new_blob','w+b') as local_blob:
        local_blob.write(myblob.read())

    new_size=200, 200
    im = Image.open(local_blob.name)
    im.thumbnail(new_size)
    im.convert("RGB").save('new_blob_thumb.jpg', quality=95)

    new_thumbfile = open('new_blob_thumb.jpg', 'rb')
    outputblob.set(new_thumbfile.read())
