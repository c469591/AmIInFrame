
# Am I In Frame NVDA Add-on

Check if current focus is inside a frame (iframe) for a better web browsing experience.

## Download

* You can
[click here to download the latest version](https://github.com/c469591/AmIInFrame/raw/main/am_i_in_frame%20V1.0.nvda-addon)
of this NVDA add-on.
* You can also visit the GitHub repository page
[Click here to go to the Am I In Frame GitHub repository](https://github.com/c469591/AmIInFrame)

### Compatibility

Tested with NVDA 2024.1 and above

## Features

* One-key check: Press a hotkey to know if you're inside a frame
* Nested frame support: Detects multiple nested frame levels
* Frame name display: Shows frame names if available
* Multi-language support: Traditional Chinese, Simplified Chinese, English

## Keyboard Shortcuts

### Default Shortcut

* NVDA+Shift+M: Check if current focus is inside a frame (corresponds to the 'M' key for frame navigation in browse mode)

### Custom Shortcuts

You can customize the shortcut through NVDA's "Input Gestures" dialog, under the "Am I In Frame" category.

## Usage

### Basic Usage

1. While browsing a webpage, press `NVDA+Shift+M`
2. The add-on will speak whether you're inside a frame
3. If inside a frame, it will also tell you the frame name (if available)

### Speech Examples

* Not in a frame: "Not in frame"
* In a single frame: "In frame" or "In frame: {frame name}"
* In nested frames: "In 2 nested frames"

## What is a Frame (iframe)?

A frame is another webpage embedded within a webpage, commonly found in:

* Advertisement blocks
* Embedded video players (e.g., YouTube)
* Social media share buttons
* Third-party login forms
* Online editors

When browsing inside a frame, some NVDA navigation features may be limited to that frame's scope. Knowing whether you're in a frame can help you navigate web pages more effectively.

## Changelog

### V1.0

1. Initial release
2. Support for checking if inside a frame
3. Support for detecting multiple nested frames
4. Support for displaying frame names
5. Multi-language support: Traditional Chinese, Simplified Chinese, English
