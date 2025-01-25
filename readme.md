# Job Listing QnA Chatbot 

This repository contains a **Question-and-Answer (QnA) chatbot** powered by **Generative AI (GenAI)** to help users query job listings effectively. The chatbot stores multiple job listings in a **vector database**, allowing users to ask specific and contextual questions about those listings. It utilizes **LangChain** and **LangSmith** for AI workflows and debugging, **Streamlit** for a user-friendly interface, and **AstraDB** for managing vectorized data.

## Key Features

- **Query Job Listings**: Users can query specific job listings saved in the vector database, such as salary, requirements, benefits, location, and more.
- **Generative AI with Llama3**: Provides detailed and context-aware responses to user queries.
- **Fast Inference with ChatGroq**: Ensures low-latency and efficient responses.
- **LangChain Integration**: Seamlessly orchestrates AI workflows for complex question-answering processes.
- **LangSmith for Monitoring and Debugging**: Offers tools to debug and monitor AI workflow performance.
- **GoogleGenAIEmbedding for Semantic Search**: Powers the chatbot’s understanding of natural language queries.
- **AstraDB as a Vector Database**: Stores job listings in vectorized form for fast and accurate retrieval.
- **Streamlit Frontend**: Provides an interactive and easy-to-use web-based interface.

## How It Works

1. **Job Listings Storage**: Multiple job listings, including details such as job titles, descriptions, requirements, and benefits, are saved as vectorized data in **AstraDB**.
2. **Query Input**: Users interact with the chatbot through the **Streamlit** interface, asking specific questions about job listings (e.g., "What is the salary for the software engineer role?").
3. **Embedding Generation**: The query is converted into a **semantic embedding** using **GoogleGenAIEmbedding**.
4. **Data Retrieval**: The embedding is compared with stored vectors in **AstraDB** to find the most relevant job listing(s).
5. **Response Generation**: **Llama3** processes the retrieved data and generates a natural language response.
6. **Monitoring**: **LangSmith** tracks and logs performance to ensure the chatbot works efficiently.
7. **Output**: The chatbot provides a clear, context-aware response on the Streamlit interface.

## Technologies Used

| Component              | Technology/Library         | Description                                           |
|------------------------|----------------------------|-----------------------------------------------------|
| **Frontend**           | Streamlit                 | Web-based interface for user interaction.           |
| **Language Model**     | Llama3                    | Generates detailed responses based on retrieved data.|
| **Inference Engine**   | ChatGroq                  | Enables fast and efficient AI inference.            |
| **Workflow Orchestration** | LangChain              | Handles AI pipeline management and logic.           |
| **Monitoring**         | LangSmith                 | Tracks and debugs AI workflow performance.          |
| **Embedding**          | GoogleGenAIEmbedding      | Converts queries into embeddings for vector search. |
| **Database**           | AstraDB                  | Stores job listings in vectorized form.             |

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kunal356/job-QnA-chatbot-with-db.git
cd job-QnA-chatbot-with-db
```

### 2. Install Dependencies
Ensure Python is installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add the following keys:

```env
# ChatGroq
GROQ_API_KEY=<your_chatgroq_api_key>

# GoogleGenAIEmbedding
GOOGLE_API_KEY=<your_google_genai_embedding_key>

# AstraDB
ASTRA_DB_APPLICATION_TOKEN=<your_astra_db_token>
ASTRA_DB_ID=<your_astra_db_id>
ASTRA_DB_NAMESPACE=<your_astra_db_namespace>
ASTRA_DB_API_ENDPOINT=<your_astra_db_endpoint>

# LangChain
LANGCHAIN_API_KEY=<your_langchain_api_key>

# LangSmith
LANGSMITH_API_KEY=<your_langsmith_api_key>
```

Replace `<your_..._key>` with your actual API keys.

### 4. Run the Application
Launch the chatbot using Streamlit:
```bash
streamlit run app.py
```

The app will be accessible at `http://localhost:8501`.

## Project Structure

```
job-QnA-chatbot-with-db/
│
├── app.py                   # Main entry point (Streamlit app)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variable setup
├── embeddings/              # Embedding generation logic
├── database/                # AstraDB integration and job storage
├── langchain/               # LangChain workflows and configurations
├── utils/                   # Helper functions and utilities
└── README.md                # Project documentation
```

