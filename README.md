# 📥 snap_ripper

`snap_ripper` is a Python tool that helps you download all your exported Snapchat Memories — including both images and videos — directly from your `memories_history.html` file. It uses your authenticated session cookies to follow Snapchat's temporary links and download the actual media hosted on AWS servers.

---

## 🚀 What It Can Do

- ✅ Parse `memories_history.html` from Snapchat's data export
- ✅ Authenticate using your real Snapchat cookies
- ✅ Follow secure redirect links to real AWS-hosted media files
- ✅ Automatically download and save `.jpg`, `.png`, and `.mp4` files
- ✅ Name files neatly (e.g., `memory_0001.jpg`, `memory_0002.mp4`)

---

## 📋 Requirements

- Python 3.7+
- Internet connection
- The following Python packages:
  - `requests`
  - `beautifulsoup4`

### Install dependencies:

```bash
pip install -r requirements.txt
````

### `requirements.txt` file content:

```
requests
beautifulsoup4
```

---

## 📂 What You Need

Place the following files in the same directory:

1. **`memories_history.html`** — Exported from [Snapchat Memories](https://my.snapchat.com/memories)

2. **`www.snapchat.com_cookies.json`** — Exported using a browser extension like:

   * [EditThisCookie (Chrome)](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)
   * [Cookie-Editor (Firefox)](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)

3. **`scan_with_cookies.py`** — The Python script provided in this repository.

---

## 🧑‍💻 How to Use

```bash
python3 scan_with_cookies.py
```

Downloaded media will be saved to a folder called:

```
snapchat_memories/
```

Each file will be named like:

```
memory_0001.jpg
memory_0002.mp4
memory_0003.png
```

---

## 🔐 Important Notes

* The tool uses your **browser cookies** to authenticate your session. These cookies **contain sensitive data**, so **never share** your JSON cookie file.
* Snapchat’s memory links **expire after 7 days**, so run the script soon after downloading your data.
* **My Eyes Only content is not included** in Snapchat's data export — you'll need to manually back that up.

---

## 📦 Coming Soon

* [ ] Resume failed downloads
* [ ] Option to download only videos or only images
* [ ] Filenames based on date/time
* [ ] Automatic ZIP archive after download

---

## 🧑‍🎓 License

MIT License

---

## 🙏 Acknowledgments

Built with ❤️ in Python by \[Your Name]
Powered by Open Source and Coffee ☕

```

---

Let me know if you’d like:
- A logo for the project
- To turn this into a Python package or CLI tool
- Instructions for bundling it into an `.exe` for non-Python users
```

