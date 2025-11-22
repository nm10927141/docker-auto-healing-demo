#!/usr/bin/env bash

# 1. 防呆：檢查有沒有輸入參數
if [[ -z "$1" ]]; then
    echo "錯誤：請輸入指令 (start 或 stop)"
    echo "用法：$0 {start|stop}"
    exit 1
fi

# 2. 處理輸入：轉成全小寫，方便比對
action=$(echo "$1" | tr 'A-Z' 'a-z')

# 3. 核心邏輯
case $action in
    "start")
        echo "正在啟動 Nginx 網頁伺服器... "
        
        # --- Docker 關鍵指令解析 ---
        # run   : 啟動一個 Container
        # -d    : Detach (在背景執行，不要卡住我的終端機)
        # --name: 給它一個好記的名字 "my-web"，不然 Docker 會亂取名
        # -p    : Port Mapping (把電腦的 8080 孔 接通到 Container 裡的 80 孔)
        # nginx : 這是 Image 的名字 (Docker 會自動去網路下載)
        docker run -d --name my-web -p 8080:80 nginx
        
        echo " 啟動成功！請打開瀏覽器輸入: http://localhost:8080 "
        ;;

    "stop")
        echo " 正在關閉並刪除伺服器..."
        
        # 先停止執行中的 Container
        docker stop my-web
        # 再把屍體 (Container 實體) 刪掉，保持環境乾淨
        docker rm my-web
        
        echo " 已清理完畢。 "
        ;;

    *)
        echo "無效的指令: $1"
        echo "請使用 start 或 stop"
        exit 1
        ;;
esac
