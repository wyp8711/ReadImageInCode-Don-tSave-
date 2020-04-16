'''
When we want to create an image & read the image in Bytes.
for example: Create an image by matplotlib, then send the image by email

The ole method:
	Image ->Save ->Read(Bytes) ->Doing work
The new method:
	Image ->---- ->Read(Bytes) ->Doing work
-
There are 2 examples(matplotlib,PIL)
-
https://wyp8711.blogspot.com/
'''
#---------------------------------------------------
import io
from matplotlib import pyplot as plt
#---------------------------------------------------
#----------Create figure----------------------------
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot([1,2,3,4,5,6,7,8,9],'r')
ax2.plot([9,8,7,6,5,4,3,2,1],'b')
fig.suptitle("Test")
fig.savefig('out.png')
#---------------------------------------------------
#----------Operate in matplotlib--------------------
obj = io.BytesIO()
fig.savefig(obj,format='png')
byte_a = obj.getvalue()
print('byte_a --> Type:',str(type(byte_a)))
#---------------------------------------------------
#----------Operate in PIL---------------------------
from PIL import Image
img = Image.open('out.png')
size = img.size
obj = io.BytesIO()
img.save(obj, 'png')
byte_b = obj.getvalue()
print('byte_b --> Type:',str(type(byte_b)))
#---------------------------------------------------
#----------Read the file----------------------------
file = open('out.png','rb')
byte_c = file.read()
print('byte_c --> Type:',str(type(byte_c)))
#---------------------------------------------------
#----------They are the same.-----------------------
Image.open(io.BytesIO(byte_a)).show()
Image.open(io.BytesIO(byte_b)).show()
Image.open(io.BytesIO(byte_c)).show()
#---------------------------------------------------
