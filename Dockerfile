FROM python:3.11

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . /app

# 安装依赖，如果有 requirements.txt 文件
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# 运行 Python 脚本
#CMD ["python", "server.py"]    