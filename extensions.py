def main():
    f = input("Enter your file name: ").lower().strip()
    name(f)
def name(f):
    match f:
        case f if f.endswith((".jpg", ".jpeg", ".png")):
            print("image/jpeg")
        case f if f.endswith(".pdf"):
            print("application/pdf")
        case f if f.endswith(".txt"):
            print("text/plain")
        case f if f.endswith(".gif"):
            print("image/gif")
        case _:
            print("application/octet-stream")

main()
