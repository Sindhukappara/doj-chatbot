# doj-chatbot
# Department of Justice Virtual Assistant

An interactive chatbot for the Department of Justice website using RAG (Retrieval Augmented Generation) approach with local deployment capabilities.

## Features

- Interactive chat interface using Streamlit
- RAG implementation with Gemini
- Local database storage using SQLite
- User feedback system
- Response caching and improvement system

## Project Structure
doj_chatbot/
│── database/
│ ├── db_setup.py
│ └── db_viewer.py
├── models/
│ ├── rag_model.py
│ └── feedback_processor.py
├── utils/
│ └── helpers.py
├── app.py
└── requirements.txt

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/doj-chatbot.git
cd doj-chatbot
python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
python database/db_setup.py
streamlit run app.py
Access the application at http://localhost:8501
```
##Features
DOJ Information: Access information about various DOJ divisions
Case Status: Check pendency of cases through NJDG
Legal Services: Information about eFiling, ePay, and Tele Law Services
Feedback System: Continuous improvement through user feedback
Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
Your Name - sindhukappara@gmail.com
Project Link: https://github.com/Sindhukappara/doj-chatbot
