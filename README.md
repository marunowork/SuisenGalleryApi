# SuisenGalleryAPI
水仙郷画像をギャラリー表示させるためのRESTful API



## 概要

水仙郷画像をギャラリー表示させるためのRESTful API



## インストール

1. Dockerが動作する環境を用意してください

2. githubからリポジトリを取得して、Dockerイメージを作成します。

   ```
   $ git clone https://github.com/marunowork/SuisenGalleryApi.git
   $ cd SuisenGalleryApi
   $ docker build -t suisengalleryapi .
   
   ```



## 起動

1. コンテナを起動します。

   ```
   $ docker run --rm -p 8000:8000 -v 保存場所のフルパス:/opt/data-volume -w /opt/data-volume SuisenGalleryAPI
   ```

   

2. URLを入力します。

   http://localhost:8000/api

