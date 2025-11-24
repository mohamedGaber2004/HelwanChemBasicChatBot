from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ===========================
#  Page Setup
# ===========================
st.set_page_config(page_title="Helwan Chem ChatBot", page_icon="🧪", layout="centered")

# ===========================
#  Custom CSS (New Polished Theme)
# ===========================
st.markdown("""
<style>

/* Global page style */
.stApp {
    background-color: #ffffff !important;
    padding-top: 20px;
}

/* Center container for logo & title */
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

/* Logo styling */
.logo-img {
    margin-bottom: 5px;
}

/* Arabic slogan */
@import url('https://fonts.googleapis.com/css2?family=Reem+Kufi&display=swap');

.slogan {
    font-family: 'Reem Kufi', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #000000;
    margin-top: 5px;
    margin-bottom: 15px;
    line-height: 1.3; /* improves readability */
}

/* Title */
h1 {
    color: #0f8a2f !important;
    font-weight: 900 !important;
    text-align: center !important;
}

/* Separator line */
.hr-line {
    width: 70%;
    height: 2px;
    background-color: #0f8a2f55;
    margin: 10px auto 5px auto;
    border-radius: 1px;
}

/* ---- Chat Bubble Styling ---- */

/* Chat container padding */
.stChatMessage {
    padding: 12px !important;
    border-radius: 13px !important;
    margin-bottom: 12px !important;
    background-color: #0f8a2f55;
}

/* User bubble */
.stChatMessage.user {
    background-color: #ffffff ;
    border: 1px solid #0f8a2f33 ;
}

/* Assistant bubble */
.stChatMessage.assistant {
    background-color: #ffffff ;
    border: 1px solid #dcdcdc ;
}

/* Make text black everywhere */
.stMarkdown, .stMarkdown p, .stChatMessage p {
    color: #000000 !important;
}

/* ---- Input Bar ---- */
.stChatInputContainer {
    background-color: #0f0f0f !important;
    border-top: 1px solid #333;
}

/* Input text */
.stChatInputContainer input {
    background-color: #ffffff !important;
    border: 2px solid #0f8a2f !important;
    border-radius: 25px !important;
    padding: 12px 20px !important;
    color: black !important;
    font-weight: 500 !important;
}

/* Send button */
.stChatInputContainer button {
    background-color: #0f8a2f !important;
    color: white !important;
    border-radius: 50% !important;
    padding: 12px !important;
    margin-left: 8px;
}

</style>
""", unsafe_allow_html=True)

# ===========================
#  Header: Logo + Slogan
# ===========================
st.markdown("""
<div class="centered">
    <img src="https://hc.helwanchem.com.eg/uploads/2019/01/logo-e1548365872947.png" width="140" class="logo-img">
    <div class="slogan">المعالجة هي الأساس</div>
</div>
<div class="hr-line"></div>
""", unsafe_allow_html=True)

# ===========================
#  LLM Setup
# ===========================
llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

# ===========================
#  Title
# ===========================
st.title("Helwan Chem ChatBot")

# ===========================
#  Chat History
# ===========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a Chemical Assistant specializing in Metal Surface Treatment and Corrosion Chemicals for Helwan Chem Factory.")
    ]

# Display previous messages
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# ===========================
#  User Input
# ===========================
prompt = st.chat_input("Ask me anything about Helwan Chem Factory or its products!")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # AI response
    with st.chat_message("assistant"):
        out = llm.invoke(st.session_state.messages)
        st.markdown(out.content)
        st.session_state.messages.append(AIMessage(content=out.content))
