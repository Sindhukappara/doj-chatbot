import streamlit as st

def main():
    st.title("Department of Justice Virtual Assistant")
    
    # Chat interface
    query = st.text_input("How can I help you?")
    
    if query:
        st.write(f"You asked: {query}")
        # Placeholder for chatbot response
        st.write("Bot: I'm here to help with DOJ-related queries.")
        
        # Feedback buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍"):
                st.success("Thank you for the feedback!")
        with col2:
            if st.button("👎"):
                st.error("Sorry for the inconvenience")

if __name__ == "__main__":
    main()
