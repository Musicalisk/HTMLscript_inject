# HTML Script Injector

A simple Python utility that automates the process of injecting custom code (from a Markdown file) into multiple HTML files simultaneously. It specifically targets the closing `</body>` tag to ensure your scripts load at the correct time.

## 🚀 Features
- **GUI Selection**: Uses native file explorers to select folders and script files.
- **Safety First**: 
    - Creates new files prefixed with `Output-` rather than overwriting originals.
    - Skips files that already contain the script to prevent duplicates.
    - Validates the presence of the `</body>` tag before attempting injection.
- **Batch Processing**: Handles all `.html` files within a selected directory.

## 🛠️ Requirements
- Python 3.x
- `tkinter` (usually included with standard Python installations)

## 📖 How to Use
1. **Run the script**: Execute the `.py` file.
2. **Select Folder**: When prompted, select the directory containing your HTML files.
3. **Select Script**: Select the `.md` file containing the code/text you want to inject.
4. **Check Results**: The console will display a summary of files updated, skipped, or missing the required tags. Your new files will appear in the same directory with the `Output-` prefix.

## 🔍 Function Breakdown
- `folder_select()`: Opens a folder picker.
- `script_select()`: Opens a file picker filtered for `.md` files.
- `define_script(s)`: Reads the content of the selected Markdown file.
- `inject_script(f, s)`: The core logic that searches for `</body>`, performs the replacement, and saves the new output files.
