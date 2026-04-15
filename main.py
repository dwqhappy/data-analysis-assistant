from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import sessions, messages, query

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(sessions.router, prefix="/api/sessions", tags=["sessions"])
app.include_router(messages.router, prefix="/api/sessions", tags=["messages"])
app.include_router(query.router, prefix="/api", tags=["query"])

@app.get("/")
def read_root():
    return {"message": "智能数据分析系统 API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}