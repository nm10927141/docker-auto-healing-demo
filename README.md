# Docker Auto-Healing System (Demo)

這是一個自動化運維系統的實作 Demo，包含自動部署腳本與具備自癒能力的監控程式。

## 功能特色 (Features)
1. **自動部署 (Deployment)**: 使用 Bash Script (`manage_docker.sh`) 快速管理容器生命週期。
2. **自癒監控 (Self-Healing)**: 使用 Python (`monitor.py`) 進行服務健康檢查，偵測到 Timeout 或 Connection Refused 時自動重啟 Docker 容器。
3. **日誌追蹤 (Logging)**: 完整記錄故障發生時間與修復結果。
4. **CI Pipeline**: 整合 GitHub Actions 進行自動化程式碼品質檢查。 // 目前還在學習

## 使用方式 (Usage)

### 1. 啟動服務
`bash`
`./manage_docker.sh start`
### 2.啟動監控
`python monitor.py`


Language: Python 3.9, Bash Shell
Infrastructure: Docker
CI/CD: GitHub Actions
