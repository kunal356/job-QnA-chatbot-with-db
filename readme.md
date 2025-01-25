# Job QnA Chatbot with Database

This repository contains a **Question-and-Answer (QnA) chatbot** built with **Generative AI (GenAI)** to handle job-related queries. The chatbot is designed with cutting-edge technologies like **LangChain** and **LangSmith** for robust AI workflows, **Streamlit** for its interactive interface, and **AstraDB** for efficient vectorized data management.

## Key Features

- **Generative AI with Llama3**: Provides accurate, context-aware responses to user queries.
- **Fast Inference with ChatGroq**: Optimized for low-latency interactions.
- **LangChain Integration**: Ensures seamless orchestration of AI components for complex workflows.
- **LangSmith for Monitoring and Debugging**: Offers tools for performance tracking and debugging.
- **GoogleGenAIEmbedding for Semantic Understanding**: Semantic embeddings power intelligent query matching.
- **AstraDB as a Vector Database**: Manages and retrieves vectorized data efficiently.
- **Streamlit Frontend**: A user-friendly, web-based interface for interaction.

## Technologies Used

| Component              | Technology/Library         | Description                                           |
|------------------------|----------------------------|-----------------------------------------------------|
| **Frontend**           | Streamlit                 | Web-based interface for user interaction.           |
| **Language Model**     | Llama3                    | Generates natural language responses.               |
| **Inference Engine**   | ChatGroq                  | Enables fast and efficient inference.               |
| **Workflow Orchestration** | LangChain              | Manages complex AI workflows.                      |
| **Monitoring**         | LangSmith                 | Tracks and debugs AI performance.                   |
| **Embedding**          | GoogleGenAIEmbedding      | Creates semantic embeddings for query understanding.|
| **Database**           | AstraDB                  | Vector database for scalable data retrieval.        |

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kunal356/job-QnA-chatbot-with-db.git
cd job-QnA-chatbot-with-db
```

### 2. Install Dependencies
Make sure Python is installed, then install the required packages:
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
ASTRA_DB_APPLICATION_TOKEN = <YOUR_ASTRA_DB_TOKEN>
ASTRA_DB_ID = <YOUR_ASTRA_DB_ID>
ASTRA_DB_NAMESPACE= <YOUR_ASTRA_DB_NAMESPACE>
ASTRA_DB_API_ENDPOINT = <YOUR_ASTRA_DB_ENDPOINT>

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

## How It Works

1. **Input via Streamlit**: Users enter job-related queries through the Streamlit interface.
2. **Embedding Generation**: GoogleGenAIEmbedding converts the query into semantic embeddings.
3. **Data Retrieval**: The embeddings are compared with stored vectors in AstraDB to find relevant information.
4. **Workflow Orchestration**: LangChain orchestrates the AI workflow, including context preparation and model response generation.
5. **Monitoring**: LangSmith tracks performance and identifies potential bottlenecks or errors.
6. **Response Generation**: Llama3 generates a natural language response.
7. **Output**: The chatbot displays the response on the Streamlit interface.

## Project Structure

```
job-QnA-chatbot-with-db/
│
├── app.py                   # Main entry point (Streamlit app)
├── requirements.txt         # Python dependencies
├── .env                     # Example environment variables setup
└── README.md                # Project documentation
```

