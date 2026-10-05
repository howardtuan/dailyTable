# 搜尋可見性：官方依據與維護原則

查核日期：2026-10-05。適用網站：<https://mydailytable.com/>，GitHub Pages 純靜態品牌網站。

SEO 與 GEO 的目標是讓搜尋引擎與 AI 搜尋可以存取、辨識並正確引用品牌與產品資訊。完成網站設定不代表搜尋平台已收錄，也不保證排名或 AI 引用。

## 內容與結構

- [Google：生成式 AI 搜尋最佳實務](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)：持續採用基礎 SEO，提供有用、可靠的內容。Google Search 不使用 `llms.txt`，也不要求特製的 AI 結構化資料。
- [Google：AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)：AI 搜尋的支援連結需可被索引、且能在搜尋結果顯示摘要。產品名稱、成分、規格、用途、購買方式與問答應以可見文字提供；JSON-LD 必須符合頁面內容。
- [Google：Organization](https://developers.google.com/search/docs/appearance/structured-data/organization)：首頁可提供實際品牌名稱、官網與 Logo，協助辨識品牌。沒有確認的公司地址、電話、統編或社群帳號，不應自行補入。
- [Google：網站名稱](https://developers.google.com/search/docs/appearance/site-names)：首頁使用單一 `WebSite` 節點，提供 `name`、官網 `url`，必要時提供 `alternateName`。本站沒有站內搜尋功能，不應加入不存在的 `SearchAction`。
- [Google：Product snippet](https://developers.google.com/search/docs/appearance/structured-data/product-snippet)：商品複合式搜尋結果要求真實的 `review`、`aggregateRating` 或 `offers` 等資料。本站沒有站內結帳，也沒有持續維護的售價與評論來源，因此基本 `Product` 描述用於產品語意；不捏造價格、評分、庫存或運送承諾。
- [Google：文件更新紀錄](https://developers.google.com/search/updates)：2026-05-08 公告 FAQ 複合式搜尋結果自 2026-05-07 停止顯示，2026-06-15 移除對應文件。可見 FAQ 仍有閱讀價值；`FAQPage` 如使用，僅提供一致的問答語意，不承諾 Google FAQ 複合式搜尋結果。

## 爬蟲存取

`robots.txt` 是存取政策，不是收錄申請。搜尋用途與模型訓練用途應分別判斷；不需要為搜尋可見性另行開啟訓練爬蟲。

- [OpenAI Docs：爬蟲](https://developers.openai.com/api/docs/bots)：`OAI-SearchBot` 用於 ChatGPT 搜尋；`GPTBot` 用於模型訓練，兩者獨立。`ChatGPT-User` 是使用者觸發的網頁存取，不是自動搜尋索引爬蟲。若未來新增防火牆或 CDN，依官方公布的 IP 清單查核合法搜尋流量。
- [Anthropic：爬蟲](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)：`Claude-SearchBot` 用於搜尋品質與索引，`Claude-User` 用於使用者查詢，`ClaudeBot` 為訓練用途。這些爬蟲遵守官方列出的 `robots.txt` 控制方式。
- [Perplexity：爬蟲](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)：`PerplexityBot` 用於搜尋結果與連結，不用於基礎模型訓練。`Perplexity-User` 是使用者要求的擷取，通常不遵守 `robots.txt`；若有防火牆，使用官方最新 IP 清單搭配 User-Agent 驗證。

## Sitemap 與選用的 AI 導覽

- [Google：建立與提交 sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)：列出希望索引的 canonical 頁面網址；單頁網站的 `#product` 等錨點不是另一個獨立頁面。`lastmod` 只在主要內容、結構化資料或連結有實質更新時修改。Google 忽略 `priority` 與 `changefreq`。
- [llms.txt 原始提案](https://llmstxt.org/)：截至查核日仍為社群提案。可作簡潔的品牌／產品文字與導覽入口；維護時保持與可見 HTML 一致，只指向存在的公開資源。它不取代 `robots.txt`、sitemap 或主要 HTML，也不能證明 ChatGPT、Claude、Perplexity 已收錄本站。

## 發布後的人工追蹤

1. 用網站擁有者帳號在 [Google Search Console](https://search.google.com/search-console) 驗證 `mydailytable.com`，提交 `https://mydailytable.com/sitemap.xml`。
2. 用 URL Inspection 檢查首頁與實際 Google 擷取結果，必要時申請重新索引。[Google 官方重新擷取說明](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)指出需要 Search Console 擁有者或完整使用者權限；提出申請仍不保證立即收錄。
   同時依 Google 的生成式 AI 搜尋指南，確認 Search Console 的生成式 AI 搜尋顯示設定未排除本站；這是帳戶端設定，不能由 HTML 或 robots.txt 代為啟用。
3. 查看查詢字詞、點閱與索引狀態，使用自然的產品資訊補足使用者問題。不要為了關鍵字堆疊內容或隱藏文字。
4. 更新通路時，同步調整可見購買卡片、FAQ、JSON-LD、AI 導覽文字與 [通路查核記錄](retailers.md)。售價、優惠、效期與供貨以各通路頁面為準。
5. 調整正式網域或新增頁面時，同步檢查 canonical、分享圖絕對網址、sitemap 與 `robots.txt`；實際發布後確認這些檔案回應成功，且不是 404 頁面。
