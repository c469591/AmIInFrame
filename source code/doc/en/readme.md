### Am I In Frame NVDA Add-on

This is a simple NVDA add-on with just one function:
Check if the current cursor position is inside a frame (iframe).
This add-on was developed to facilitate website accessibility testing. Currently, NVDA only has functions to jump to a frame or leave a frame.
When you use the web search function to jump to a certain position, there is no simple way to know if you are inside a frame. This makes it difficult to determine whether the content you are viewing belongs to the website itself or is embedded from another website.

#### (Quick Note) What is a Frame?

A frame is a way to dynamically embed content from other websites into a webpage.
For example, embedding YouTube videos or Facebook posts. This is a common practice on many government websites, especially in Taiwan. They often like to publish important announcements on social platforms, and then lazily embed the Facebook posts directly into their government websites instead of rewriting the content.
As a result, NVDA (screen reader) users often encounter messy images, links, and like counts while browsing. This is often because the frame contains embedded content from other websites that were not designed with accessibility in mind.

### Download

* [Click here to download the latest version](https://github.com/c469591/AmIInFrame/raw/main/am_i_in_frame%20V0.1.nvda-addon)

### Compatibility

NVDA 2024.1+

### Keyboard Shortcuts

* NVDA+Shift+M: Check if current focus is inside a frame

### Features

* One-key check for frame status
* Nested frame detection support
* Speaks frame names
* Multi-language support (Traditional Chinese, Simplified Chinese, English)

### Changelog

#### V0.1

* Initial release
* Support for checking if inside a frame
* Support for detecting multiple nested frames
* Support for displaying frame names
* Multi-language support: Traditional Chinese, Simplified Chinese, English

### License

GPL v2
