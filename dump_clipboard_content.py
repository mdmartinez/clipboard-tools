# dump_html_clipboard.py
from AppKit import NSPasteboard

def main():
    pb = NSPasteboard.generalPasteboard()
    html_data = pb.stringForType_("public.html") # public.html is the macOS UTI (Uniform Type Identifier) for HTML content

    if html_data is not None:
        with open("clipboard.html", "w", encoding="utf-8") as f:
            f.write(html_data)
        print("Clipboard HTML dumped to clipboard.html")
        return 0

    # Fall back to plain text if no HTML
    text_data = pb.stringForType_("public.utf8-plain-text")
    if text_data is not None:
        with open("clipboard.txt", "w", encoding="utf-8") as f:
            f.write(text_data)
        print("Clipboard text dumped to clipboard.txt")
        return 0

    print("No text or HTML content found in clipboard")
    return 1

if __name__ == "__main__":
    main()
