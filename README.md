# 🎥 YT-DLP TOOLKIT 

![Language](https://img.shields.io/badge/Language-Python-red)
![Platform](https://img.shields.io/badge/Platform-Windows-white)
![Tool](https://img.shields.io/badge/Backend-yt--dlp-red)
![License](https://img.shields.io/badge/License-MIT-white)

A high-performance, visually optimized CLI wrapper for **yt-dlp**, featuring a professional **Red & White** aesthetic. This toolkit automates media downloading with smart folder management, metadata embedding, and a persistent user workflow.

Created by **Chaitanya Kumar Sathivada**.

---

## 🛠️ Key Features

- **Smart Folder Logic:** Automatically creates sub-folders for playlists while keeping single video downloads clean in the root directory (eliminates the "NA" folder bug).
- **Dynamic Path Detection:** Automatically identifies the current Windows User profile to set the default `Downloads` path.
- **Embedded Metadata:** Full support for embedding thumbnails, artist information, and media tags directly into the files.
- **Optimized Modes:**
  - **Option 1 (MP3):** High-fidelity audio extraction with metadata.
  - **Option 2 (MP4):** Video downloads recoded for maximum compatibility.
  - **Option 3 (Art):** Extracts high-resolution album/video cover art only.
- **In-App Settings:** Update your download destination on the fly without restarting the toolkit.
- **Looping Workflow:** Stay within your selected mode to paste multiple URLs; use `/back` to return to the main menu.

---

## 🎨 Visual Interface

The toolkit uses a restricted high-contrast color scheme:
- **RED:** System branding, ASCII Logo, Borders, and UI Accents.
- **WHITE:** User Inputs, URL prompts, Success messages, and Credits.
- **BLACK:** Command-line background.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.x**
- **yt-dlp:** Must be installed and added to your System PATH.
- **FFmpeg:** Required for MP3 conversion and metadata embedding.

### Running from Source
1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/yt-dlp-toolkit.git
   ```
   ```
   cd yt-dlp-toolkit
   ```
2. Install the Dependencies:
   Navigate to the downloaded repo on File Explorer and run the file named as `FirstRun.bat`.
   This will install the required dependencies with just one click. Don't worry – it's safe. You can check the code if required.
3. Launch the toolkit:
   ```
   python yt-dlp-toolkit.py
   ```

### Building the Standalone EXE
To package the toolkit as a single runnable file with a custom icon:
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
3. Build the executable:
   ```
   python -m PyInstaller --onefile --console --icon=icon.ico yt-dlp-toolkit.py
   ```
4. Locate your standalone app in the `/dist` folder.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Built for efficiency. Designed for style.*
