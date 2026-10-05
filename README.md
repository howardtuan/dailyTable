# 每日餐桌 daily TABLE

簡約的單頁品牌形象網站，介紹頂級沖泡純可可粉、日常搭配與購買通路。

- 正式網站：[mydailytable.com](https://mydailytable.com/)
- 純 HTML / CSS / JavaScript，無建置流程或套件依賴。
- GitHub Pages 從 `main` 分支的根目錄部署；自訂網域設定保留於 `CNAME`。

## 本機預覽

在專案根目錄執行：

```sh
python3 -m http.server 4173
```

開啟 `http://localhost:4173`。更新 `main` 並 push 後，由既有 GitHub Pages 流程部署。

## 內容維護

- `index.html`：繁體中文內容、產品資訊、通路卡片、聯絡表單連結與搜尋分享資訊。
- `assets/css/styles.css`：響應式版面、鍵盤焦點與減少動態效果設定。
- `assets/js/scripts.js`：手機導覽選單及頁尾年份；主要內容、FAQ 與購物連結無 JavaScript 仍可使用。
- `assets/img/web/`：從原始品牌照片產生的網頁尺寸版本。原始照片保留於 `assets/img/`。
- `assets/logos/`：各通路的本地 Logo；[來源記錄](assets/logos/README.md)。
- [通路查核記錄](docs/retailers.md)：商品／查詢網址、供貨狀態與查核依據。

購買卡片應使用核實過的商品直連；下架通路提供商品資訊或站內搜尋，並清楚標示狀態。更新通路時，同步修改頁面查核日期與查核記錄。商品價格、庫存及效期以通路頁面為準，不在品牌網站固定承諾。

## 驗證

已檢查桌機（1440px）、平板（768px）、手機（390px）與小螢幕（320px）的排版、圖片、錨點、手機選單及 FAQ；頁面使用相對資源路徑，支援 GitHub Pages。
