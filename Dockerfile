FROM python:3.12-slim

# 作業ディレクトリを作成・移動（コンテナ内の作業場所）
WORKDIR /app

# パッケージインストール用に requirements.txt をコピー
COPY requirements.txt .

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# Flaskアプリ（templates, static, server.py含む）をコピー
COPY app/ .

# ポート5000を開放（Flaskのデフォルト）
EXPOSE 5000

# アプリ起動
CMD ["python", "server.py"]
