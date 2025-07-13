# 📚 Chatbot Streamlit từ tài liệu trong repo

Triển khai chatbot sử dụng:
- Streamlit
- LangChain
- FAISS
- OpenAI GPT

## 🚀 Cách chạy local
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
streamlit run app.py
```

## ☁️ Deploy trên Streamlit Community Cloud
1. Fork hoặc clone repo này
2. Đảm bảo file `docs/data.txt` chứa dữ liệu bạn muốn
3. Deploy trên https://share.streamlit.io/deploy
4. Thiết lập biến môi trường `OPENAI_API_KEY` trong trang deploy (cấu hình Secrets)
