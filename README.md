# TailorTalk 🤖💬

![TailorTalk Interface]("C:/Users/sohel/OneDrive/Pictures/Screenshots/Screenshot 2024-08-25 185327.png")

## Overview 🌟

TailorTalk is an interactive chatbot application designed to provide a seamless conversational experience. Built with Streamlit and Groq, TailorTalk allows users to engage in meaningful conversations with an AI model, and it supports dynamic customization of system prompts and response lengths. Whether you're seeking answers to your queries or just having a chat, TailorTalk aims to offer a responsive and adaptable interaction.

## Features 🚀

- **Dynamic System Prompt**: Customize the system prompt in real-time to adjust the chatbot's behavior and focus. ✍️
- **Response Length Control**: Adjust the length of responses by specifying the maximum number of lines. 📏
- **Model Selection**: Choose from multiple AI models to interact with, each offering unique capabilities. 🤖
- **Real-Time Interaction**: Enjoy fast and interactive conversations with the chatbot, powered by Groq's API. ⚡

## Installation 🛠️

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/tailortalk.git
    cd tailortalk
    ```

2. **Create a Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your Groq API key:
    ```plaintext
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage 🚀

1. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with TailorTalk**:
    - Open your browser and go to `http://localhost:8501`. 🌐
    - Use the sidebar to configure the chatbot's settings, including model selection and system prompt. 🛠️
    - Enter your questions in the input field and start chatting with the AI. 🗨️

## Code Structure 📂

- **`app.py`**: The main script that sets up the Streamlit interface and handles interactions with the Groq API. 📝
- **`requirements.txt`**: Lists the dependencies required for the project. 📦

## Configuration ⚙️

### Sidebar

- **Model Selection**: Choose from available AI models. Each model has its own set of features and token limits. 🔍
- **System Prompt**: Enter a custom system prompt to define the chatbot's behavior and personality. 🎭
- **Response Length**: Set the maximum number of lines for the chatbot's responses. 📏

### Customization

Feel free to modify the code to better fit your needs. Adjust the models, prompts, or response length limits according to your requirements. ✨

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue to discuss them first. 💡

## Acknowledgments 🙏

- **Groq**: For providing the powerful API that drives the chatbot interactions. 🏆
- **Streamlit**: For the easy-to-use framework that powers the web interface. 🚀
- **LangChain**: For the prompt templates and conversation management tools. 🛠️

For any issues or questions, please open an issue on the [GitHub repository](https://github.com/SoheliPaul/tailortalk/issues). 📝

