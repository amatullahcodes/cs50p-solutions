def main():
    x = input("How are you? ")
    convert(x)

def convert(x):
    print(x.replace(":)","😊").replace(":(","😔"))
main()