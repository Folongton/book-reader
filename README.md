Here's a description for your `README.md`:

---

# Screen Capture and Text Recognition App

This project is a Python application that automates screen capturing, text recognition, and text formatting using OpenAI's ChatGPT API. It is designed to detect specific text on the screen, capture a predefined region, extract text from images, and organize the results into a formatted text file. The app is modular and includes unit tests to ensure reliability and ease of use.

---

## Features

1. **Automated Screen Capturing**:
   - Captures the full screen every 3 seconds until specific text is detected.
   - Detects duplicate consecutive screenshots to determine the end of a sequence.

2. **Text Recognition with OCR**:
   - Uses Tesseract OCR to identify text in images.
   - Filters for specific target text, with optional case-insensitivity.

3. **Region-Based Screen Capture**:
   - Captures a predefined region of the screen when specific text is found.
   - Saves captured regions to a specified folder for further processing.

4. **Text Extraction and Formatting**:
   - Extracts text from captured images.
   - Combines all extracted text into a single file.
   - Sends the text to OpenAI's ChatGPT API for formatting, improving readability.

5. **Keyboard Automation**:
   - Simulates key presses (e.g., turning pages) to automate navigation during the process.

6. **Modular Design**:
   - Easy to integrate, test, and extend.

7. **Unit Tests**:
   - Comprehensive test suite included, covering all major functionalities.

---

## How It Works

1. **Initialization**:
   - The app starts capturing full-screen images every 3 seconds.
   - When the specified text is found in a screenshot, it:
     - Simulates a key press to turn the page.
     - Captures the defined screen region and saves the image.
   - This process continues until two consecutive screenshots are identical.

2. **Post-Capture Processing**:
   - All region images are processed with Tesseract OCR to extract text.
   - Extracted text from all images is combined into a single file.

3. **ChatGPT Formatting**:
   - The combined text file is sent to the ChatGPT API with a prompt to format it for easier reading.
   - The formatted text is saved to another file.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/screen-capture-text-recognition.git
   cd screen-capture-text-recognition
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or venv\Scripts\activate (Windows)
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - **Windows**: [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
   - **macOS**: `brew install tesseract`.
   - **Linux**: `sudo apt-get install tesseract-ocr`.

4. Set up your OpenAI API key:
   - Export your API key:
     ```bash
     export OPENAI_API_KEY="your_openai_api_key"
     ```
   - Or pass it directly to the app during execution.

---

## Usage

Run the application with:

```bash
python app.py
```

### Configuration

- **Target Text**: Specify the text the app will look for on the screen.
- **Region**: Define the region to capture as `(x, y, width, height)`.
- **Folder Paths**: Configure where screenshots and text files are saved.
- **API Key**: Provide your OpenAI API key for ChatGPT integration.

---

## Example Workflow

1. The app scans your screen for the specified target text (e.g., "Chapter").
2. When the text is found:
   - The app presses a key to turn the page.
   - Captures a specific region of the screen and saves it.
   - Repeats the process until no new pages are detected.
3. Extracted text is saved into a text file and sent to ChatGPT for formatting.
4. The formatted output is saved to a separate file for easy reading.

---

## Tests

Unit tests are included to ensure the reliability of:
- Screen capturing
- OCR text detection
- ChatGPT API integration

Run tests using:

```bash
pytest
```

---

## Dependencies

- `pyautogui` – For screen capturing and keyboard automation.
- `pillow` – Image processing library.
- `pytesseract` – OCR functionality via Tesseract.
- `openai` – ChatGPT API integration.
- `pytest` – For running unit tests.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

--- 

Let me know if you'd like to include any additional sections or make changes!