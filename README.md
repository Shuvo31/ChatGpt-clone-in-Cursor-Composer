# FastAPI ChatGPT Clone

This project is a simple ChatGPT clone using FastAPI and the OpenAI API with the GPT-4o model. The application is designed as a single-file project (`main.py`) and uses Daisy UI for a clean, dark-mode chat interface.

## Features

- **FastAPI** for backend server implementation.
- **OpenAI GPT-4o** for generating chatbot responses.
- **Daisy UI** for a styled, dark-mode chat interface.
- **Hot-reloading** for easy development.

## Prerequisites

Make sure you have Python 3.7+ installed.

## Getting Started

1. **Clone the Repository** or **Download the `main.py` File**.

2. **Install the Required Packages**:

   Install all dependencies using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up the Environment Variable**:

   Create a `.env` file in the same directory as `main.py` and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

   Alternatively, you can set the environment variable in your terminal:

    - **On Linux/macOS**:
      ```bash
      export OPENAI_API_KEY=your_openai_api_key_here
      ```

    - **On Windows**:
      ```bash
      set OPENAI_API_KEY=your_openai_api_key_here
      ```

4. **Run the Application**:

   Use `uvicorn` to run the FastAPI application with reload enabled:

    ```bash
    uvicorn main:app --reload --host 127.0.0.1 --port 8000
    ```

   This command starts the server at `http://127.0.0.1:8000`.

## Usage

- Open your web browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).
- Type your message into the input box and click "Send" to interact with the ChatGPT clone.

## Project Structure

All code is contained in a single file: `main.py`.

- **Backend**: The backend is built using FastAPI and listens for user messages.
- **Frontend**: The frontend uses Tailwind CSS and Daisy UI for a simple and clean chat interface.
- **API Integration**: The app integrates with the OpenAI API to generate responses using the GPT-4o model.

## Troubleshooting

- If you see a warning like `You must pass the application as an import string to enable 'reload' or 'workers'`, ensure you are running the app with `uvicorn main:app --reload`.

- Make sure the OpenAI API key is correctly set in your environment.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is open-source and available under the MIT License.
