import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_astradb import AstraDBVectorStore
from langchain_community.callbacks import StreamlitCallbackHandler

load_dotenv()


def create_vector_embedding():
    if "vectors" not in st.session_state:
        with st.spinner("Loading Database..Please wait....."):
            st.session_state.embeddings = GoogleGenerativeAIEmbeddings(
                model="models/text-embedding-004")
            st.session_state.vector_store = AstraDBVectorStore(
                embedding=st.session_state.embeddings,
                namespace=os.environ['ASTRA_DB_NAMESPACE'],
                collection_name="newcollection",
                token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
                api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
            )


def main():
    groq_api_key = os.getenv('GROQ_API_KEY')
    llm = ChatGroq(groq_api_key=groq_api_key, model='Llama3-8b-8192')

    prompt = ChatPromptTemplate.from_template(
        """
        I have provided you various job alerts.
        Answer the questions based on the provided jobs only.
        Please provide the most accurate response based on the question.
        <context>
        {context}
        </context>
        Question:{input}
        """
    )

    st.set_page_config(
        page_title="Job Listings Q&A Using Llama3", page_icon='🦜')
    st.title("🦜Job Listings Q&A Using Llama3")

    if "vector_store" not in st.session_state:
        create_vector_embedding()
        st.write("Vector Database is ready...")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hello!! I am your helpful assistant. How can I help you today??"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input(
        placeholder="Ask me any question related to jobs.")

    if user_query:
        docs = st.session_state.vector_store.similarity_search(
            user_query, k=25)
        chain = load_qa_chain(llm=llm, chain_type='stuff',
                              verbose=True, prompt=prompt)
        st.session_state.messages.append(
            {"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        with st.chat_message("assistant"):
            streamlit_callback = StreamlitCallbackHandler(st.container())
            response = chain.invoke({"input_documents": docs, "input": user_query},
                                    return_only_outputs=True,  callbacks=[streamlit_callback])
            st.session_state.messages.append(
                {"role": "assistant", "content": response['output_text']})
            st.write(response['output_text'])


if __name__ == '__main__':
    main()
