from fastapi import FastAPI

print("hello AWS world!")
app = FastAPI()

@app.get("/health")
def health():
    return "hello google"
