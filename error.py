# try:
#     f = open('test.txt', 'w')
#     f.write("Just a random text line")
# #Using wrong mode will give an OS Error
# except OSError:
#     print("Hey you have an OSError please check again")
# finally:
#     print("I always run regardless of any error")

def ask_for_int():
    try:
        num = int(input("Enter an integer"))
    except:
        print("Input is not an integer")
    finally:
        print("End of try/except/finally")

ask_for_int()