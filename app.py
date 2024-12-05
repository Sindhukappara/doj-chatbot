import streamlit as st
from knowledge_base import load_knowledge_base

def main():
    st.title("Department of Justice Virtual Assistant")
    
    # Load knowledge base
    kb = load_knowledge_base()
    
    # Chat interface
    query = st.text_input("How can I help you?")
    
    if query:
        # Search in knowledge base
        response = "I'm here to help with DOJ-related queries."
        st.write(f"Bot: {response}")
        
        # Feedback buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍"):
                st.success("Thank you for the feedback!")
        with col2:
            if st.button("👎"):
                st.error("Thank you for the feedback!")

if __name__ == "__main__":
    main()
