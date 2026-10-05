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
- `robots.txt` / `sitemap.xml`：公開網頁與搜尋爬蟲設定，網站地圖包含正式首頁及產品圖片。
- `llms.txt`：品牌與產品的補充資訊摘要，供支援此格式的工具使用。
- `.nojekyll`：直接發布靜態檔案，保留 `robots.txt`、XML 與文字摘要的原始格式。

購買卡片應使用核實過的商品直連；下架通路提供商品資訊或站內搜尋，並清楚標示狀態。更新通路時，同步修改頁面查核日期與查核記錄。商品價格、庫存及效期以通路頁面為準，不在品牌網站固定承諾。

## SEO 與 AI 搜尋

首頁提供產品名稱與規格的標題／摘要、HTTPS canonical、Open Graph／社群分享資訊，以及 Organization、Brand、WebSite、WebPage、Product、FAQPage 與購買通路 ItemList 的 JSON-LD。產品資訊與問答皆直接出現在靜態 HTML，不依賴 JavaScript 載入。

`robots.txt` 開放一般搜尋與 OAI-SearchBot、Claude-SearchBot、PerplexityBot，排除儲存庫維護文件；這不代表平台一定會收錄。`llms.txt` 為補充格式，Google Search 不使用它作排名或 AI 搜尋訊號。FAQ 與基本 Product 標記協助表達內容，不宣稱取得 Google FAQ／商品複合式搜尋結果；本站沒有固定售價或評分資料。

更新公開內容時，同步維護以下資料：

1. `index.html` 的可見產品資訊、FAQ 與 JSON-LD，確保內容一致。
2. `sitemap.xml` 的 `lastmod`、WebPage 的 `dateModified`，填入實際內容更新日。
3. `llms.txt` 的摘要、通路狀態與查核日期；庫存查核日期與頁面更新日應分開維護。

發布後，由網域擁有者在 Google Search Console／Bing Webmaster Tools 驗證網站並提交 `https://mydailytable.com/sitemap.xml`，使用 URL 檢查確認索引狀態。帳戶驗證、收錄與排名由平台處理，本次未代為提交或虛構驗證標籤。若要統一 HTTP 至 HTTPS，應在既有 Cloudflare 設定中確認 SSL 模式與重新導向規則，避免與 GitHub Pages 產生循環重新導向。

[官方文件與設計依據](docs/search-sources.md)

## 驗證

已檢查桌機（1440px）、平板（768px）、手機（390px）與小螢幕（320px）的排版、圖片、錨點、手機選單及 FAQ；頁面使用相對資源路徑，支援 GitHub Pages。
