from fastapi import FastAPI

# 变量名必须是小写的 app，因为你的运行命令里写的是 :app
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}
