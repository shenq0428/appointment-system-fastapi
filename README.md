### 🛠 技术栈
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)

### 📂 目录结构颜色定义
- ![app/api](https://img.shields.io/badge/api-接口逻辑-green) : 处理所有路由请求
- ![app/models](https://img.shields.io/badge/models-数据模型-orange) : 数据库表定义
- ![app/schemas](https://img.shields.io/badge/schemas-Pydantic验证-blue) : 输入输出校验
  
# appointment-system-fastapi
28/1/2026 A backend appointment management system built with FastAPI, SQLite/PostgreSQL, and Docker for learning system design.

## 功能

- 健康检查 API (/health)
- 用户预约管理
- 数据库存储 (SQLite/PostgreSQL)

## 安装步骤

1. 安装依赖: `pip install -r requirements.txt`
2. 运行服务: `uvicorn main:app --reload`
3. 访问健康检查: `http://127.0.0.1:8000/health`
