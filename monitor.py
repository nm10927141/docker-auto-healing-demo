import requests
import time
import subprocess  # 用來執行 Shell command
import logging     # 寫 Log 
from datetime import datetime

# --- 設定日誌 (Log) ---
# 這會把發生的事情寫入 'system_monitor.log' 檔案中
logging.basicConfig(
    filename='system_monitor.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

URL = "http://localhost:8080"
CONTAINER_NAME = "my-web"

def restart_container():
    """
    當服務掛掉時，執行這個函式來重啟 Docker 容器
    """
    print("嘗試自動修復中 (Restarting Container)...")
    logging.warning(f"偵測到服務異常，開始執行自動修復：重啟 {CONTAINER_NAME}")
    
    try:
        # subprocess.run 是 Python 執行 Linux 指令的標準方式
        # 等同於在終端機打： docker restart my-web
        result = subprocess.run(
            ["docker", "restart", CONTAINER_NAME], 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        print("修復指令已發送")
        logging.info("自動修復成功：容器已重啟")
        
    except subprocess.CalledProcessError as e:
        print(f" 修復失敗: {e}")
        logging.error(f"自動修復失敗，請人工介入！錯誤訊息: {e}")

print(f"程式啟動，監控目標：{URL}")

# ... 上面的程式碼不用變 ...

try:
    while True:
        try:
            response = requests.get(URL, timeout=2)
            
            if response.status_code == 200:
                print(".", end="", flush=True)
            else:
                print(f"\n 狀態碼異常: {response.status_code}")
                restart_container()
        
        # RequestException，不管它是斷線、Timeout 還是 DNS 錯誤，都抓
        except requests.exceptions.RequestException as e:
            print(f"\n 偵測到網路異常 (錯誤類型: {type(e).__name__})")
            print(f"詳細原因: {e}")
            restart_container() # 
            
            print("等待 5 秒讓服務啟動...")
            time.sleep(5)
        # ----------------

        time.sleep(2)

except KeyboardInterrupt:
    print("\n 監控結束")