ItemsInCart=0

# if ItemsInCart!=2:
#     raise Exception("Products Cart count not matching")

# if ItemsInCart != 2:
#    pass
# assert(ItemsInCart==2)

#try and catch
try:
    with open('text.txt','r') as reader:
        reader.read()
except Exception as e:
    print("some how i reached this block because there is a failure in try blok")

try:
    with open('tloxt.txt','r') as reader:
        reader.read()
except Exception as e:
    print("failed as file name is wrong. except block because there is a failure in try blok")

try:
    with open('text5dg.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally: #simiar to java , no matter weather exception got occured or not
    print("finlay block ! cleaning up the resources")