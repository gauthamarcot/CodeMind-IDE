# CodeMind IDE

![CodeMind_Logo](https://github.com/gauthamarcot/notebot/assets/43777597/a9121bbc-016e-4d0c-a1c3-95657fbd5f44)

CodeMind IDE is a powerful integrated development environment designed to enhance your coding productivity. It features real-time code watching, project-specific AI suggestions, intra-team chat, and command invocation from the text area.

## Features

- **Code Watcher**: Always watches the code users type and provides real-time feedback.
- **Interactive ASCII AI Figure**: An AI character that interacts with users, providing suggestions in an ASCII format.
- **Intra-team Chat**: A chat window for communication within the local area network.
- **Command Prompt**: Use `/` to invoke commands directly from the text area.
- **AI Prompt Text Area**: A dedicated area for interacting with the AI.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gauthamarcot/codemind-ide
    ```

2. Navigate to the project directory:
    ```sh
    cd codemind-ide
    ```

3. Install frontend dependencies:
    ```sh
    cd frontend
    npm install
    ```

4. Install backend dependencies:
    ```sh
    cd ../backend
    npm install
    ```

5. Install AI dependencies:
    ```sh
    cd ../ai
    pip install -r requirements.txt
    ```

## Usage

1. Build the React frontend:
    ```sh
    cd frontend
    npm run build
    ```

2. Start the backend server:
    ```sh
    cd ../backend
    node src/server.js
    ```

3. Start the AI service:
    ```sh
    cd ../ai
    python app.py
    ```

4. Run the Electron application:
    ```sh
    npm start
    ```

## Packaging

To create a `.deb` or `.dmg` package:

1. Ensure all dependencies are installed and the application is built.
2. Use Electron Builder to package the application:
    ```sh
    npx electron-builder
    ```

## Example

1. Open the application and type the following in the text area:
    ```sh
    console.log('Hello, World!');
    ```
2. The Code Watcher will provide real-time feedback and suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Contact

For questions or support, please contact [gouthamarcot@gmail.com](mailto:gouthamarcot@gmail.com).
