import ctypes

folder = input("Inform intire path of the folder to hid")

hid_flag = 0x02

ret = ctypes.windll.kernel32.SetFileAttributesW(folder,'hidden.txt',hid_flag)

if ret:
    print("File hidden")
else:
    print("File not hidden")

