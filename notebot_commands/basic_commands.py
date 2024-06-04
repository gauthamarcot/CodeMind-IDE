import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

class CommandHandler:
    def handle_command(self, command, data):
        try:
            if command == "/sort":
                lines = data.strip().split('\n')
                sorted_lines = sorted(lines)
                return "\n".join(sorted_lines)
            elif command == "/reverse":
                lines = data.strip().split('\n')
                reversed_lines = list(reversed(lines))
                return "\n".join(reversed_lines)
            elif command == "/uppercase":
                return data.upper()
            elif command == "/count":
                lines = data.strip().split('\n')
                word_count = sum(len(line.split()) for line in lines)
                return f"Word count: {word_count}"
            else:
                return f"Unknown command: {command}"
        except Exception as e:
            logging.error(f"Error handling command '{command}': {e}")
            return f"Error handling command '{command}'"
