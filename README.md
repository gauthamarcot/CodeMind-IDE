# notebot


NoteBot is an advanced text editor application integrated with GPT-2, offering an interactive experience with an ASCII AI character. NoteBot can process natural language commands and assist with coding, note-taking, and text processing tasks.

## Features

- **Code Editor Interface**: A user-friendly text area for writing and editing code or notes.
- **Interactive ASCII AI Character**: An AI character that interacts with users through ASCII art, changing its appearance based on interactions.
- **Command Parsing**: Recognizes and processes commands from the text area.
- **GPT-2 Integration**: Uses GPT-2 to provide responses and process commands.
- **Command Handling**: Supports various commands such as `/sort`, `/reverse`, `/uppercase`, and `/count`.

## Installation

1. Clone the repository:
    ```sh
    git clone [https://github.com/yourusername/notebot.git](https://github.com/gauthamarcot/notebot)
    ```
2. Navigate to the project directory:
    ```sh
    cd notebot
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python notebot.py
    ```
2. Interact with the AI by typing commands or queries in the text area.
3. Use the specific question area for more interactive and targeted queries.

## Commands

- **/sort**: Sorts the lines above the command.
- **/reverse**: Reverses the lines above the command.
- **/uppercase**: Converts the text above the command to uppercase.
- **/count**: Counts the number of words in the text above the command.

## Example

1. Open the application and type the following in the text area:
    ```
    /sort
    line 3
    line 1
    line 2
    ```
2. The lines will be sorted:
    ```
    line 1
    line 2
    line 3
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Contact

For questions or support, please contact [gouthamarcot@gmail.com](mailto:gouthamarcot@gmail.com).
