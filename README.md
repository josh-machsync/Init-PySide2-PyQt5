# Init-PyQt5
pyqt5 一個初始化範例

- python 3.8.10
- pQqt5
- [Qt Designer](https://build-system.fman.io/qt-designer-download)

### 檔案架構

``` bash
project_root/
├── main.py                 # 主程式入口，啟動應用程式
├── .env                    # 配置檔案，用於存放設定參數
├── requirements.txt        # 依賴需求清單
├── README.md               # 專案說明文件
├── resources/              # 靜態資源文件夾（圖片、字型、樣式表等）
│   ├── images/
│   ├── fonts/
├── ui/                     # 存放 UI 文件
│   ├── main_window.ui      # 使用 Qt Designer 設計的 UI 文件
├── app/                    # 主應用程式模組
│   ├── __init__.py
│   ├── main_window.py      # 主視窗的邏輯 Qt Designer UI To Python
│   ├── controller.py        # 控制器，用於處理業務邏輯
│   ├── model.py             # 資料模型，儲存應用的數據結構和處理
│   └── view.py             # 視圖模組，專注於 UI 與模型的互動
└── utils/                  # 實用工具函式
    ├── __init__.py
    ├── helpers.py          # 常用函式
    └── database.py         # 資料庫連線與操作
```

## QT UI To Python
``` bash
pyuic5 -x qt_designer.ui -o qt_designer.py

```





# 其他



### 進階檔案架構

``` bash
project_root/
├── main.py                 # 主程式入口，啟動應用程式
├── config.py               # 配置檔案，用於存放設定參數
├── requirements.txt        # 依賴需求清單
├── README.md               # 專案說明文件
├── resources/              # 靜態資源文件夾（圖片、字型、樣式表等）
│   ├── images/
│   ├── fonts/
│   └── styles.qss          # QSS樣式表
├── ui/                     # 存放 UI 文件
│   ├── main_window.ui      # 使用 Qt Designer 設計的 UI 文件
│   └── dialogs/            # 存放各種對話框的 UI 文件
├── app/                    # 主應用程式模組
│   ├── __init__.py
│   ├── main_window.py      # 主視窗的邏輯
│   ├── dialogs/            # 各種對話框的邏輯
│   │   └── custom_dialog.py
│   ├── controllers/        # 控制器，用於處理業務邏輯
│   ├── models/             # 資料模型，儲存應用的數據結構和處理
│   └── views/              # 視圖模組，專注於 UI 與模型的互動
└── utils/                  # 實用工具函式
    ├── __init__.py
    ├── helpers.py          # 常用函式
    └── database.py         # 資料庫連線與操作
```
