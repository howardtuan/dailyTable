# 每日餐桌 daily TABLE

簡約的品牌形象官網，以五個獨立頁面介紹純可可粉、品牌理念、日常搭配與購買通路。

- 正式網站：[mydailytable.com](https://mydailytable.com/)
- 純 HTML / CSS / JavaScript，無套件依賴、後端或建置流程。
- GitHub Pages 從 `main` 分支根目錄部署，自訂網域設定保留於 `CNAME`。
- `.nojekyll` 直接發布靜態檔案，保留 robots、XML 與文字摘要的原始格式。

## 網站頁面

| 網址 | 原始檔案 | 內容 |
| --- | --- | --- |
| `/` | `index.html` | 首頁與品牌／產品／日常提案導覽 |
| `/products/cocoa/` | `products/cocoa/index.html` | 成分、規格、產品特色及常見問題 |
| `/about/` | `about/index.html` | 品牌理念與餐桌故事 |
| `/rituals/` | `rituals/index.html` | 晨間、午後與週末的可可搭配 |
| `/shop/` | `shop/index.html` | 六個購買／查詢通路、Logo 與供貨資訊 |

主選單直接開啟各頁網址，首頁舊版的產品、品牌、日常、通路與 FAQ 錨點由 JavaScript 轉向相應新頁面。電話及聯絡表單已從公開網頁、結構化資料與資訊摘要移除。

## 本機預覽

在專案根目錄執行：

```sh
python3 -m http.server 4173
```

開啟 `http://localhost:4173`。直接 push 至 `main` 後，由既有 GitHub Pages 流程部署。資源及內部連結使用根目錄路徑，對應正式自訂網域。

## 內容維護

- 各頁 HTML：可見內容、共用導覽／頁尾、每頁 SEO 與 JSON-LD。導覽或頁尾更新時同步維護五個頁面。
- `assets/css/styles.css`：共用響應式版型、鍵盤焦點與減少動態效果設定。
- `assets/js/scripts.js`：手機選單、頁尾年份與舊網址相容。主要內容、購物連結與 FAQ 不依賴 JavaScript。
- `assets/img/web/`：原有品牌攝影的網頁尺寸版本，原始照片保留於 `assets/img/`。
- `assets/logos/`：[通路 Logo 來源記錄](assets/logos/README.md)。
- [通路查核記錄](docs/retailers.md)：商品／查詢網址、供貨狀態與依據。

購買卡片使用核實過的商品直連；下架通路提供商品資訊或站內搜尋並標示狀態。商品價格、庫存與效期以通路頁面為準，不在官網固定承諾。

## SEO 與 AI 搜尋

每頁都有獨立的標題、摘要、HTTPS canonical、Open Graph／分享資訊及適合該頁的 JSON-LD。全站提供 Organization、Brand 與 WebSite；產品頁另有 Product／FAQPage，通路及日常頁提供 ItemList，內頁提供 BreadcrumbList。所有重要文字皆直接存在靜態 HTML。

`robots.txt` 開放一般搜尋與 OAI-SearchBot、Claude-SearchBot、PerplexityBot，排除儲存庫維護文件。`sitemap.xml` 列出五個 canonical 網址及產品圖片。`llms.txt` 為品牌／產品的補充導覽；Google Search 不使用它作排名或 AI 搜尋訊號，也不代表任何平台已收錄。

更新內容時，同步維護：

1. 可見資訊及相應頁面的 JSON-LD，產品 FAQ 文字應完全一致。
2. `sitemap.xml` 的 `lastmod` 與每頁 `dateModified`，填入實際內容更新日。
3. `llms.txt`、通路卡片及查核記錄；供貨查核日期與頁面更新日分別維護。
4. 內部導覽、canonical、麵包屑與分享圖片網址。

網站擁有者可在 Google Search Console／Bing Webmaster Tools 驗證網域並提交 `https://mydailytable.com/sitemap.xml`，檢查首頁與產品頁索引及生成式 AI 搜尋顯示設定。本次未代為進行帳戶驗證或提交；實際收錄、排名與 AI 引用由平台決定。本站無固定價格／評分資料，不宣稱取得 Google FAQ／商品複合式搜尋結果。

[官方文件與設計依據](docs/search-sources.md)

## 驗證

檢查五頁在桌機、平板、手機及 320px 小螢幕的版面、圖片、內部連結、選單、FAQ、舊網址相容與無 JavaScript 使用；另檢查 sitemap、爬蟲規則、結構化資料與可見內容一致性。
