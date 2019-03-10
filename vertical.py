import numpy as np
from PIL import Image
# need to put the .jpg files in one by one.  Want to find a way to get everthing in a spacific directory.
images_list = [#path to .jpg]
imgs = [ Image.open(i) for i in images_list ]
# Take the size of the smallest .jpg
min_img_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
# Resizes all .jpg files to the size of the smallest .jpg
img_merge = np.vstack( (np.asarray( i.resize(min_img_shape,Image.ANTIALIAS) ) for i in imgs ) )
# Merges all .jpg files into an array.
img_merge = Image.fromarray( img_merge)
# Saves the new array "filename".jpg
img_merge.save( 'vert_compiled.jpg' )
