def main():
    x = input("Please Input File Name and Its Extension: ").strip().lower()

    filetype(x)

def filetype(n):
    y = n.endswith

    if y(".jpg") or y(".jpeg"):
        print("image/jpeg")
    elif y(".gif"):
        print("image/gif")
    elif y(".png"):
        print("image/png")
    elif y(".pdf"):
        print("application/pdf")
    elif y(".txt"):
        print("text/plain")
    elif y(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
