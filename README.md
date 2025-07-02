# clipboard-tools

A simple Python tool for interacting with the macOS clipboard using PyObjC.

## Features

- List available clipboard types
- Dump HTML content from clipboard to file

## Motivation

I recently encountered a situation where I couldn't view some content on my clipboard in my editor or by using `pbpaste`. I learned that on MacOS, if the clipboard content doesn't specifically contain the `public.utf8-plain-text` type, then `pbpaste` will not display it.

This repo helps to inspect and extract clipboard content.

## Testing

You can create a bookmarklet in your browser to test this tool. Use the following JavaScript code to copy HTML content to the clipboard that is missing the `public.utf8-plain-text` type.

```javascript
javascript: (async () => {
  const blob = new Blob(["<b>Injected HTML</b>"], { type: "text/html" });
  await navigator.clipboard.write([new ClipboardItem({ "text/html": blob })]);
  alert("Clipboard set!");
})();
```

## Requirements

- Python 3.13+
- [PyObjC](https://pyobjc.readthedocs.io/en/latest/) (installed automatically via dependencies)
- [uv](https://docs.astral.sh/uv/) (recommended package manager)

## Installation

Using uv (recommended):

```sh
git clone https://github.com/mdmartinez/clipboard-tools.git
cd clipboard-tools
uv sync
```

Or using pip:

```sh
git clone https://github.com/mdmartinez/clipboard-tools.git
cd clipboard-tools
pip install .
```

## Usage

### List Clipboard Types

Show all available clipboard data types:

```sh
uv run info
```

#### Example `info` Output on Image Clipboard

```
public.file-url
CorePasteboardFlavorType 0x6675726C
dyn.ah62d4rv4gu8y6y4grf0gn5xbrzw1gydcr7u1e3cytf2gn
NSFilenamesPboardType
dyn.ah62d4rv4gu8yc6durvwwaznwmuuha2pxsvw0e55bsmwca7d3sbwu
Apple URL pasteboard type
com.apple.finder.noderef
fndf
public.utf16-external-plain-text
CorePasteboardFlavorType 0x75743136
public.utf8-plain-text
NSStringPboardType
com.apple.icns
CorePasteboardFlavorType 0x69636E73
public.tiff
NeXT TIFF v4.0 pasteboard type
```

### Dump HTML Content

Extract HTML content from clipboard and save to `clipboard.html`:

```sh
uv run dump
```

Will attempt to default to `clipboard.txt` if no HTML content is found.

## Project Structure

- `get_clipboard_types.py` – Lists clipboard types using AppKit
- `dump_clipboard_content.py` – Extracts HTML content from clipboard
- `pyproject.toml` – Project configuration and dependencies

## License

MIT License

## Other Tools

The CLI tool [pbv](https://github.com/chbrown/macos-pasteboard) can also be used to view clipboard content when `public.utf8-plain-text` is missing. This tool is more convenient as a direct replacement for `pbpaste`.
