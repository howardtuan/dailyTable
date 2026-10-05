# 搜尋優化與驗證記錄

查核日期：2026-10-05（Asia/Taipei）。正式網域：<https://mydailytable.com/>。

## 修改前的公開搜尋觀察

- 一般「無糖可可粉」首批結果以其他品牌及購物平台為主，本次未看到新版官網。
- 「無糖可可粉」限制 `mydailytable.com` 網域，可查到首頁，但搜尋資料仍標示約 3.3 年前擷取、含舊版電話及文案。這證明存在舊首頁搜尋資料，不代表新版內容已更新索引。
- 新的產品、日常及通路網址未出現在本次 `site:` 查詢結果。`site:` 不是完整索引清單，不能以無結果判定未索引。
- 查詢工具的返回順序不代表特定地區 Google、Bing 或 AI 平台的精確排名。

## 本次實作

- 首頁與產品頁自然呈現「無糖可可粉」；產品標題說明 250g 與 100% 純可可，保留正式品名與規格。
- 新增可可指南入口，以及選購、沖泡兩篇具有不同用途的文章。內容包括成分比較、包裝標示、三步沖泡、牛奶／豆漿／咖啡／冰飲、結塊／沉澱／保存。
- 八個頁面提供真實內部連結及獨立標題、描述與 canonical。Article、FAQ、麵包屑資料對應可見內容，原始來源在文章中可讀。
- Sitemap 與補充 AI 摘要加入新文章，保留正常爬蟲存取。
- 新增 IndexNow 驗證檔與部署後提交通知腳本，避免用已停用的 sitemap ping 或不適用商品站的 Google Indexing API。

## 驗證標準

1. 本機與正式站的頁面可讀、圖片及連結正常，手機可閱讀且無水平溢出。
2. 八個 canonical 網址都在 sitemap，FAQ 結構化文字與正文一致，重要資訊無 JavaScript 也能讀取。
3. IndexNow 回覆獨立記錄；200 是收到，202 是等待驗證。收到通知不等於索引成功。
4. Google Search Console 要以網站擁有者或完整使用者權限驗證索引及申請重新擷取；沒有該權限不得宣稱已提交。
5. 「無糖可可粉」不限制網域、不加入品牌字時，實際返回新版官網，才能記為泛詞搜尋曝光證據。技術測試、網域限定結果、AI 工具讀取成功不能代替這項結果。

## 發布與提交結果

待部署後填入實際檢查及回覆；尚不宣稱泛詞排名或 AI 引用已成功。

## 官方依據

- [Google SEO 入門](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)：自然內容、清楚的標題與描述、可追蹤內部連結；不採關鍵字堆疊。
- [Google 重新擷取](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)：可能需數天到數週，申請並不保證收錄，重複申請不會加速。
- [Google site: 查詢限制](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)：查詢結果不保證完整。
- [IndexNow 文件](https://www.indexnow.org/documentation)：網站驗證檔、網址通知與 HTTP 回覆的含義。
- [Bing AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)：清楚結構、可靠來源、一致及更新的內容與 IndexNow。
