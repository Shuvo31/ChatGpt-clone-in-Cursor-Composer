from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# HTML template for the chat UI
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT Clone</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.13.6/dist/full.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
</head>
<body class="bg-gray-900 text-white">

    <div class="container mx-auto mt-10">
        <h1 class="text-3xl font-bold mb-5 text-center">ChatGPT Clone</h1>
        <div id="chat-container" class="border border-gray-800 rounded-lg p-5 max-w-xl mx-auto mb-4 overflow-y-auto" style="height: 400px;">
            <!-- Chat messages will be dynamically inserted here -->
        </div>
        <form id="chat-form" class="flex justify-center">
            <input type="text" id="user-input" class="input input-bordered w-full max-w-xs text-black" placeholder="Type your message..." autocomplete="off" required>
            <button type="submit" class="btn btn-primary ml-2">Send</button>
        </form>
    </div>

    <script>
        document.getElementById('chat-form').addEventListener('submit', async (event) => {
            event.preventDefault();
            const userInput = document.getElementById('user-input').value;
            if (!userInput) return;

            addMessageToChat('You', userInput);

            document.getElementById('user-input').value = '';  // Clear input field

            try {
                const response = await axios.post('/chat', { message: userInput });
                addMessageToChat('ChatGPT', response.data.reply);
            } catch (error) {
                addMessageToChat('Error', 'Failed to get response from GPT-4o.');
            }
        });

        function addMessageToChat(sender, message) {
            const chatContainer = document.getElementById('chat-container');
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('my-2');
            messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    </script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_chat_ui():
    return html_content

@app.post("/chat", response_class=JSONResponse)
async def chat(request: Request):
    form_data = await request.json()
    user_message = form_data.get("message")

    try:
        # Use OpenAI's GPT-4o model to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response['choices'][0]['message']['content']
        return {"reply": reply}

    except Exception as e:
        return {"reply": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)



