# Packet Aquarium

**Packet Aquarium** は、ローカルネットワーク内のパケットをキャプチャして、まるで水槽の中に泳ぐ魚のように可視化するプロジェクトです。安全なローカル環境内でネットワークの生態系を観察できるツールとして設計されています。

---

## Features

- リアルタイムでパケットキャプチャ
- 簡単なWeb UIでの可視化
- Dockerベースの再現性の高い環境
- `NET_RAW` & `NET_ADMIN` 権限を使用（要注意）
- 開発者がローカル環境でネットワーク観察を学ぶためのサンドボックス

---

## Requirements

- Docker
- Docker Compose
- Unix系OS推奨（Windows WSL2 環境でも動作確認済み）

---

## インストール & 起動方法

1. リポジトリをクローン

```bash
git clone git@github.com:t-bfny/packet_aquarium.git
cd packet_aquarium
```

2. Docker イメージをビルド＆起動

```bash
docker compose up --build
```
※ docker-compose.yml に privileged, NET_RAW, NET_ADMIN, network_mode: host などの設定が含まれているため、権限に注意してください。

3. ブラウザでアクセス

```bash
http://localhost:5000
```

