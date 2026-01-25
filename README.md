# Helwan Chem ChatBot 🧪

A conversational AI assistant powered by LangChain and Streamlit, specializing in Metal Surface Treatment and Corrosion Chemicals for Helwan Chem Factory. This chatbot leverages advanced language models to provide expert guidance on chemical products and industrial applications.

## Overview

The Helwan Chem ChatBot is an intelligent assistant designed to help users learn about Helwan Chem Factory's products and services. Built with modern AI technologies, it combines:

- **LangChain Framework**: For building LLM-powered applications with prompt templates and message chains
- **Streamlit**: For creating an interactive web-based user interface
- **Groq API**: For fast and efficient language model inference
- **RAG (Retrieval-Augmented Generation)**: For knowledge-enhanced responses

The chatbot maintains conversation context and provides specialized knowledge about metal surface treatment and corrosion prevention chemicals.

## Features

✨ **Key Features:**

- 🤖 **AI-Powered Conversations**: Powered by OpenAI/GPT models via Groq API
- 💬 **Chat History**: Maintains conversation context across multiple exchanges
- 🧪 **Specialized Knowledge**: Expert in Metal Surface Treatment and Corrosion Chemicals
- 🎨 **Modern UI**: Polish Streamlit interface with custom styling and Helwan Chem branding
- 🌍 **Multilingual Support**: Arabic slogan "المعالجة هي الأساس" (Treatment is the Foundation)
- 📚 **Knowledge-Enhanced**: Integration with RAG evaluation tools for improved responses

## Project Structure

```
HelwanChemBasicChatBot/
├── chatBot.py              # Main Streamlit chatbot application
├── main.py                 # Entry point script
├── ChatBotEval.ipynb       # Evaluation notebook for chatbot performance
├── RAG_Eval.ipynb          # RAG evaluation and testing notebook
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project configuration (Python 3.13+)
├── LICENSE                 # Project license
└── README.md              # This file
```

## Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager
- GROQ_API_KEY environment variable (for LLM access)

### Setup Steps

1. **Clone or navigate to the project directory:**
```bash
cd HelwanChemBasicChatBot
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
   - Create a `.env` file in the project root
   - Add your GROQ API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

### Running the Chatbot

Launch the Streamlit application:
```bash
streamlit run chatBot.py
```

The application will open in your browser at `http://localhost:8501`

### Interacting with the Bot

1. Type your question about Helwan Chem Factory or its products in the chat input
2. The chatbot responds with specialized knowledge about chemical treatments and corrosion prevention
3. Conversation history is maintained throughout your session

### Example Queries

- "What metal surface treatments do you offer?"
- "How can I prevent corrosion in industrial applications?"
- "What are the properties of your chemical products?"
- "Tell me about Helwan Chem Factory"

## Development

### Running Evaluation Notebooks

The project includes Jupyter notebooks for evaluation and testing:

**ChatBot Evaluation:**
```bash
jupyter notebook ChatBotEval.ipynb
```

**RAG Evaluation:**
```bash
jupyter notebook RAG_Eval.ipynb
```

These notebooks help assess chatbot performance and RAG (Retrieval-Augmented Generation) effectiveness.

## Dependencies

Key packages used in this project:

| Package | Purpose |
|---------|---------|
| `langchain-groq` | LLM integration with Groq |
| `langchain-core` | Core LangChain abstractions |
| `langchain-community` | Community-contributed integrations |
| `streamlit` | Web UI framework |
| `langgraph` | Graph-based LLM workflows |
| `sentence-transformers` | Embedding models for RAG |
| `langchain-chroma` | Vector database for embeddings |
| `langchain-tavily` | Web search integration |
| `pypdf` | PDF document processing |

See [requirements.txt](requirements.txt) for the complete dependency list.

## Configuration

### Model Settings

The chatbot is configured to use:
- **Model**: OpenAI/GPT-OSS-20B via Groq
- **Temperature**: 0 (deterministic responses)
- **System Role**: Chemical Assistant specializing in Metal Surface Treatment and Corrosion Chemicals

You can modify these settings in [chatBot.py](chatBot.py#L76-L81).

### UI Customization

The interface features custom CSS styling:
- Helwan Chem company colors and logo
- Responsive chat bubble design
- Arabic language support
- Professional dark/light theme

Modify the CSS in [chatBot.py](chatBot.py#L15-L69) to customize the appearance.

## API Requirements

### Groq API

This project requires a valid GROQ_API_KEY:

1. Sign up at [console.groq.com](https://console.groq.com)
2. Generate an API key
3. Add it to your `.env` file

## Troubleshooting

| Issue | Solution |
|-------|----------|
| API Key Error | Ensure `GROQ_API_KEY` is set in `.env` file |
| Port Already in Use | Change port with `streamlit run chatBot.py --server.port 8502` |
| Module Not Found | Verify all dependencies installed: `pip install -r requirements.txt` |
| Memory Issues | The chatbot loads embeddings models; ensure sufficient RAM (~4GB recommended) |

## Future Enhancements

🚀 Potential improvements:

- Integration with Helwan Chem product database
- Advanced RAG with company-specific documents
- Multi-language support (Arabic, English, French)
- Analytics dashboard for chat usage
- Persistent chat history with database
- Improved context window management
- Integration with CRM systems

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Support

For issues, questions, or suggestions:
- Review the troubleshooting section above
- Check the Jupyter notebooks for examples
- Consult LangChain documentation: https://python.langchain.com
- Streamlit documentation: https://docs.streamlit.io

## Project Information

- **Project Name**: HelwanChemBasicChatBot
- **Version**: 0.1.0
- **Python**: 3.13+
- **Status**: Active Development

---

**Made with ❤️ for Helwan Chem Factory**