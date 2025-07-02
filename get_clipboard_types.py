from AppKit import NSPasteboard

def main():
    pb = NSPasteboard.generalPasteboard()
    types = pb.types()
    for t in types:
        print(t)

if __name__ == "__main__":
    main()
