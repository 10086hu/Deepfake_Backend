from app.init import create_app
from flask_cors import CORS  # 导入 CORS

app = create_app()

# 在 Flask 应用中启用 CORS
CORS(app, origins=["http://localhost:5173"])  # 配置允许访问的前端地址

if __name__ == '__main__':
    # 启动 Flask 应用
    app.run(debug=True, use_reloader=False)
