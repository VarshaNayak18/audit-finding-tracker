import chromadb

class ChromaClient:

    def __init__(self):

        self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(
            name="audit_knowledge",
            embedding_function=None
        )

    def add_documents(self, docs):

        ids = [str(i) for i in range(len(docs))]

        embeddings = [
            [0.0] * 5 for _ in docs
        ]

        self.collection.add(
            documents=docs,
            ids=ids,
            embeddings=embeddings
        )

    def query(self, text, n_results=2):

        query_embedding = [0.0] * 5

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results