import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter

# 🚀 Cấu hình
st.title("📚 Chatbot từ tài liệu trong repo")
st.write("Nhập câu hỏi và chatbot sẽ trả lời dựa trên nội dung tài liệu.")

# 🧩 Đọc dữ liệu
with open("docs/data.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# ✂️ Tách đoạn văn
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(raw_text)

# 🧠 Tạo embedding và index
embeddings = OpenAIEmbeddings()  # cần thiết lập biến môi trường OPENAI_API_KEY
docsearch = FAISS.from_texts(texts, embeddings)

# 🔍 Tạo chain
llm = ChatOpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

# 💬 Giao diện hỏi đáp
question = st.text_input("Câu hỏi:")

if question:
    answer = qa_chain.run(question)
    st.markdown("#### ✅ Trả lời:")
    st.write(answer)
