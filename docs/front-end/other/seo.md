# SEO (Search Engine Optimization) Interview Questions and Answers

_Last updated: October 28, 2026_

90 SEO interview questions with answers, split into three levels: 30 easy, 30 moderate and 30 advanced.

The answers follow how Google Search works today: mobile-first indexing, Core Web Vitals with INP, JavaScript rendering, structured data in JSON-LD, Google's current spam policies and AI features like AI Overviews. Most questions are written from a web developer's point of view, so the focus is on technical SEO and on-page work rather than marketing.

## Table of Contents

- [Easy Questions (1-30)](#easy-questions-1-30)
- [Moderate Questions (31-60)](#moderate-questions-31-60)
- [Advanced Questions (61-90)](#advanced-questions-61-90)

### Easy Questions (1-30)

- [1: What is SEO?](#1-what-is-seo)
- [2: How does a search engine work at a high level?](#2-how-does-a-search-engine-work-at-a-high-level)
- [3: What is crawling?](#3-what-is-crawling)
- [4: What is indexing?](#4-what-is-indexing)
- [5: What is the difference between organic and paid results?](#5-what-is-the-difference-between-organic-and-paid-results)
- [6: What is a SERP?](#6-what-is-a-serp)
- [7: What is a title tag and why does it matter?](#7-what-is-a-title-tag-and-why-does-it-matter)
- [8: What is a meta description? Does it affect rankings?](#8-what-is-a-meta-description-does-it-affect-rankings)
- [9: Does Google still use the meta keywords tag?](#9-does-google-still-use-the-meta-keywords-tag)
- [10: What is robots.txt?](#10-what-is-robotstxt)
- [11: What is an XML sitemap?](#11-what-is-an-xml-sitemap)
- [12: What is the robots meta tag?](#12-what-is-the-robots-meta-tag)
- [13: What is a canonical URL?](#13-what-is-a-canonical-url)
- [14: What is alt text and why does it matter for SEO?](#14-what-is-alt-text-and-why-does-it-matter-for-seo)
- [15: How should you use heading tags (h1-h6)?](#15-how-should-you-use-heading-tags-h1-h6)
- [16: What are backlinks?](#16-what-are-backlinks)
- [17: What is the difference between internal and external links?](#17-what-is-the-difference-between-internal-and-external-links)
- [18: What is anchor text?](#18-what-is-anchor-text)
- [19: What is a 301 redirect and when do you use it instead of a 302?](#19-what-is-a-301-redirect-and-when-do-you-use-it-instead-of-a-302)
- [20: What is a 404 page, and does it hurt SEO?](#20-what-is-a-404-page-and-does-it-hurt-seo)
- [21: What is Google Search Console?](#21-what-is-google-search-console)
- [22: What makes a URL SEO friendly?](#22-what-makes-a-url-seo-friendly)
- [23: What is mobile-first indexing?](#23-what-is-mobile-first-indexing)
- [24: Does HTTPS affect rankings?](#24-does-https-affect-rankings)
- [25: What are Core Web Vitals?](#25-what-are-core-web-vitals)
- [26: What is structured data?](#26-what-is-structured-data)
- [27: What are rich results?](#27-what-are-rich-results)
- [28: What is keyword research?](#28-what-is-keyword-research)
- [29: What is duplicate content? Is there a penalty for it?](#29-what-is-duplicate-content-is-there-a-penalty-for-it)
- [30: What are Open Graph tags and do they help SEO?](#30-what-are-open-graph-tags-and-do-they-help-seo)

### Moderate Questions (31-60)

- [31: What is the difference between on-page, off-page and technical SEO?](#31-what-is-the-difference-between-on-page-off-page-and-technical-seo)
- [32: How do you write a good title tag, and why does Google sometimes change it?](#32-how-do-you-write-a-good-title-tag-and-why-does-google-sometimes-change-it)
- [33: What happens if a page is blocked in robots.txt and also has a noindex tag?](#33-what-happens-if-a-page-is-blocked-in-robotstxt-and-also-has-a-noindex-tag)
- [34: What is the X-Robots-Tag header and when do you use it?](#34-what-is-the-x-robots-tag-header-and-when-do-you-use-it)
- [35: Is the canonical tag a rule or a hint? How does Google pick the canonical?](#35-is-the-canonical-tag-a-rule-or-a-hint-how-does-google-pick-the-canonical)
- [36: What do rel="nofollow", rel="sponsored" and rel="ugc" mean?](#36-what-do-relnofollow-relsponsored-and-relugc-mean)
- [37: How do you add structured data with JSON-LD?](#37-how-do-you-add-structured-data-with-json-ld)
- [38: How do you test and monitor structured data?](#38-how-do-you-test-and-monitor-structured-data)
- [39: How do you make a single-page application crawlable?](#39-how-do-you-make-a-single-page-application-crawlable)
- [40: Does Google run JavaScript? How does it index JS-heavy pages?](#40-does-google-run-javascript-how-does-it-index-js-heavy-pages)
- [41: What is the difference between CSR, SSR and SSG for SEO?](#41-what-is-the-difference-between-csr-ssr-and-ssg-for-seo)
- [42: How do you set page metadata in the Next.js App Router?](#42-how-do-you-set-page-metadata-in-the-nextjs-app-router)
- [43: How do you generate a sitemap and robots.txt in Next.js?](#43-how-do-you-generate-a-sitemap-and-robotstxt-in-nextjs)
- [44: What is a soft 404 and how do you avoid it in an SPA?](#44-what-is-a-soft-404-and-how-do-you-avoid-it-in-an-spa)
- [45: How should you handle pagination for SEO?](#45-how-should-you-handle-pagination-for-seo)
- [46: What is hreflang and how do you use it?](#46-what-is-hreflang-and-how-do-you-use-it)
- [47: How do you lazy load images without hurting SEO?](#47-how-do-you-lazy-load-images-without-hurting-seo)
- [48: What is LCP and how do you improve it?](#48-what-is-lcp-and-how-do-you-improve-it)
- [49: What is INP and how is it different from FID?](#49-what-is-inp-and-how-is-it-different-from-fid)
- [50: What is CLS and how do you fix it?](#50-what-is-cls-and-how-do-you-fix-it)
- [51: What is the difference between field data and lab data?](#51-what-is-the-difference-between-field-data-and-lab-data)
- [52: What does the URL Inspection tool in Search Console show you?](#52-what-does-the-url-inspection-tool-in-search-console-show-you)
- [53: What is keyword cannibalization?](#53-what-is-keyword-cannibalization)
- [54: What is E-E-A-T?](#54-what-is-e-e-a-t)
- [55: What are orphan pages and how do you find them?](#55-what-are-orphan-pages-and-how-do-you-find-them)
- [56: How do you handle URL parameters like sorting, filters and tracking codes?](#56-how-do-you-handle-url-parameters-like-sorting-filters-and-tracking-codes)
- [57: How do you avoid duplicates from www, trailing slashes and HTTP vs HTTPS?](#57-how-do-you-avoid-duplicates-from-www-trailing-slashes-and-http-vs-https)
- [58: How do you control what Google shows in the snippet?](#58-how-do-you-control-what-google-shows-in-the-snippet)
- [59: What is breadcrumb structured data and why use it?](#59-what-is-breadcrumb-structured-data-and-why-use-it)
- [60: What is the difference between 404, 410 and 503 for SEO?](#60-what-is-the-difference-between-404-410-and-503-for-seo)

### Advanced Questions (61-90)

- [61: What is crawl budget and when should you care about it?](#61-what-is-crawl-budget-and-when-should-you-care-about-it)
- [62: How do server errors and slow responses affect crawling?](#62-how-do-server-errors-and-slow-responses-affect-crawling)
- [63: What happens when robots.txt returns an error?](#63-what-happens-when-robotstxt-returns-an-error)
- [64: How do you migrate a site to a new domain without losing traffic?](#64-how-do-you-migrate-a-site-to-a-new-domain-without-losing-traffic)
- [65: How do you handle faceted navigation on a large e-commerce site?](#65-how-do-you-handle-faceted-navigation-on-a-large-e-commerce-site)
- [66: How do you make infinite scroll SEO friendly?](#66-how-do-you-make-infinite-scroll-seo-friendly)
- [67: What is dynamic rendering and should you still use it?](#67-what-is-dynamic-rendering-and-should-you-still-use-it)
- [68: What are common JavaScript SEO problems?](#68-what-are-common-javascript-seo-problems)
- [69: What are the limitations of Googlebot's renderer?](#69-what-are-the-limitations-of-googlebots-renderer)
- [70: How do you debug pages stuck in "Discovered - currently not indexed" or "Crawled - currently not indexed"?](#70-how-do-you-debug-pages-stuck-in-discovered---currently-not-indexed-or-crawled---currently-not-indexed)
- [71: How do you use server log analysis for SEO?](#71-how-do-you-use-server-log-analysis-for-seo)
- [72: How do you verify that a request really comes from Googlebot?](#72-how-do-you-verify-that-a-request-really-comes-from-googlebot)
- [73: How should you structure an international site, and why are IP-based redirects risky?](#73-how-should-you-structure-an-international-site-and-why-are-ip-based-redirects-risky)
- [74: How do you manage hreflang for a large site?](#74-how-do-you-manage-hreflang-for-a-large-site)
- [75: Does streaming SSR or hydration affect SEO?](#75-does-streaming-ssr-or-hydration-affect-seo)
- [76: How do you handle SEO for paywalled or login-only content?](#76-how-do-you-handle-seo-for-paywalled-or-login-only-content)
- [77: What is cloaking and how can a developer cause it by accident?](#77-what-is-cloaking-and-how-can-a-developer-cause-it-by-accident)
- [78: How do you investigate a sudden drop in organic traffic?](#78-how-do-you-investigate-a-sudden-drop-in-organic-traffic)
- [79: Which Google spam policies should developers know about?](#79-which-google-spam-policies-should-developers-know-about)
- [80: Is AI-generated content bad for SEO?](#80-is-ai-generated-content-bad-for-seo)
- [81: How do AI Overviews and AI crawlers affect SEO, and how can you control them?](#81-how-do-ai-overviews-and-ai-crawlers-affect-seo-and-how-can-you-control-them)
- [82: What is llms.txt and does it help SEO?](#82-what-is-llmstxt-and-does-it-help-seo)
- [83: What is IndexNow?](#83-what-is-indexnow)
- [84: How do you keep staging and preview environments out of search results?](#84-how-do-you-keep-staging-and-preview-environments-out-of-search-results)
- [85: What should you know about image SEO beyond alt text?](#85-what-should-you-know-about-image-seo-beyond-alt-text)
- [86: How do you catch SEO regressions automatically in CI?](#86-how-do-you-catch-seo-regressions-automatically-in-ci)
- [87: How do you handle many similar pages, like location pages or product variants?](#87-how-do-you-handle-many-similar-pages-like-location-pages-or-product-variants)
- [88: How do you improve INP on a heavy React page?](#88-how-do-you-improve-inp-on-a-heavy-react-page)
- [89: How do you handle out-of-stock and discontinued products?](#89-how-do-you-handle-out-of-stock-and-discontinued-products)
- [90: How do you plan internal linking for a large site?](#90-how-do-you-plan-internal-linking-for-a-large-site)

---

# Easy Questions (1-30)

## 1: What is SEO?

SEO (Search Engine Optimization) is the work you do so that your pages show up in search results for the queries people actually type, and so that people click on them. It covers three things: making sure search engines can find and read your pages, making the content useful and relevant, and getting other sites to trust and link to you.

For a developer, most of the job is the technical side: clean HTML, correct status codes, fast pages, crawlable links, good metadata and no blockers like broken robots.txt rules.

## 2: How does a search engine work at a high level?

There are three main steps:

1. **Crawling**: bots (like Googlebot) follow links and sitemaps to find URLs and download them.
2. **Indexing**: the search engine processes the page (and often renders its JavaScript), figures out what it is about, picks a canonical version and stores it in its index.
3. **Ranking/serving**: when someone searches, the engine picks the most relevant pages from the index and orders them using many signals (relevance, quality, links, page experience, location, language and so on).

A page can fail at any of these steps. If it is not crawled, it can't be indexed. If it is not indexed, it can't rank.

## 3: What is crawling?

Crawling is the process where a bot downloads pages from the web. Googlebot starts from URLs it already knows, follows the links on those pages and reads sitemaps to discover new URLs.

Things that help crawling:

- Real `<a href="...">` links between pages
- An XML sitemap
- Fast server responses and few errors
- No accidental `Disallow` rules in robots.txt

## 4: What is indexing?

Indexing is when the search engine analyzes a crawled page and stores it so it can be shown in results. During indexing Google reads the text, titles, headings, images, structured data and links, renders JavaScript if needed, and decides which URL is the canonical one among duplicates.

Not every crawled page gets indexed. Google may skip pages that are low quality, duplicates, or marked with `noindex`. You can check the status of a page in Google Search Console with the URL Inspection tool.

## 5: What is the difference between organic and paid results?

Organic results are the normal search results. You don't pay for them; you get them through SEO. Paid results are ads (Google Ads) that appear at the top or bottom of the page and are marked as "Sponsored". You pay per click.

SEO only affects organic results. Running ads does not improve your organic rankings.

## 6: What is a SERP?

SERP stands for Search Engine Results Page, the page you see after you search. Today it is more than ten blue links. It can include ads, AI Overviews, featured snippets, "People also ask" boxes, image and video results, local map results, shopping results and more.

These features matter because they take space and clicks. Ranking first doesn't always mean you are at the top of the screen.

## 7: What is a title tag and why does it matter?

The title tag is the `<title>` element in the `<head>`. Google uses it as the main source for the clickable headline in search results (Google calls it the "title link"), and it is also shown in the browser tab.

```html
<head>
  <title>Running Shoes for Flat Feet - Buying Guide | ShoeShop</title>
</head>
```

A good title is unique per page, describes the page clearly, puts the main topic near the start and is not stuffed with keywords. It is one of the stronger on-page signals and has a big effect on click-through rate.

## 8: What is a meta description? Does it affect rankings?

The meta description is a short summary of the page in the `<head>`:

```html
<meta
  name="description"
  content="Compare 12 running shoes for flat feet, with prices, support levels and real test results."
/>
```

Google does not use it as a ranking signal. It can be shown as the snippet under the title in results, so a good one can improve click-through rate. Google often writes its own snippet from the page text if it thinks that matches the query better. Make it unique per page and describe what the user will get.

## 9: Does Google still use the meta keywords tag?

No. Google has ignored `<meta name="keywords">` for ranking since around 2009, because people abused it. It does no harm to have it, but it does nothing for Google. The only thing it can do is show your competitors which keywords you target.

## 10: What is robots.txt?

`robots.txt` is a plain text file at the root of a host (for example `https://example.com/robots.txt`) that tells crawlers which paths they may or may not crawl.

```txt
User-agent: *
Disallow: /admin/
Disallow: /cart/

Sitemap: https://example.com/sitemap.xml
```

Important points:

- It controls **crawling**, not indexing. A blocked URL can still appear in results (without a description) if other sites link to it.
- It is public, so don't use it to hide secret paths.
- Each subdomain and protocol needs its own file.
- Well-behaved bots follow it. Bad bots ignore it.

## 11: What is an XML sitemap?

An XML sitemap is a file that lists the URLs you want search engines to know about. It helps with discovery, especially for new sites, big sites, or pages with few internal links.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/blog/seo-basics</loc>
    <lastmod>2026-09-14</lastmod>
  </url>
</urlset>
```

One sitemap can have up to 50,000 URLs or 50 MB (uncompressed). For more, use a sitemap index file. Only include canonical, indexable URLs that return 200. Google ignores `<changefreq>` and `<priority>`, but uses `<lastmod>` if it is accurate. Submit it in Search Console and reference it in robots.txt.

## 12: What is the robots meta tag?

It is a tag in the `<head>` that tells search engines how to treat a specific page:

```html
<!-- Don't show this page in search results -->
<meta name="robots" content="noindex" />

<!-- Don't index and don't follow links on this page -->
<meta name="robots" content="noindex, nofollow" />

<!-- Only for Google -->
<meta name="googlebot" content="noindex" />
```

The default is `index, follow`, so you don't need to add that. The most common use is `noindex` on pages like internal search results, thank-you pages, or login pages. The crawler must be able to fetch the page to see the tag.

## 13: What is a canonical URL?

When the same or very similar content is available on several URLs, the canonical URL is the one you want search engines to treat as the main version. You declare it with a link tag:

```html
<link rel="canonical" href="https://example.com/shoes/running" />
```

For example, `/shoes/running?sort=price` and `/shoes/running?utm_source=newsletter` should both point to `/shoes/running`. This groups the signals (like links) on one URL and tells Google which one to show. Use absolute URLs, and it is fine (and common) for a page to have a canonical pointing to itself.

## 14: What is alt text and why does it matter for SEO?

Alt text is the `alt` attribute of an image. It describes the image for screen reader users and for search engines, which use it to understand the image and the page.

```html
<img
  src="/img/red-trail-shoe.jpg"
  alt="Red trail running shoe with a thick rubber sole"
/>
```

Good alt text helps the image show up in Google Images and improves accessibility. Describe what is in the image in plain words. Don't stuff keywords. Decorative images should have an empty `alt=""` so screen readers skip them.

## 15: How should you use heading tags (h1-h6)?

Headings show the structure of the page. Use them in a logical order, like a table of contents:

```html
<h1>How to Choose Running Shoes</h1>
<h2>Know Your Foot Type</h2>
<h3>Flat Feet</h3>
<h3>High Arches</h3>
<h2>Pick the Right Cushioning</h2>
```

Usually you have one `<h1>` that describes the main topic. Don't pick heading tags for their font size; use CSS for styling. Headings help search engines and screen reader users understand what each section is about. Having more than one `h1` is not a penalty, but one clear main heading is easier to understand.

## 16: What are backlinks?

Backlinks are links from other websites to your site. Search engines treat them as a kind of vote: if many trusted and relevant sites link to a page, it is probably useful. Google's original PageRank algorithm was built on this idea and links are still an important signal.

Quality matters much more than quantity. One link from a respected site in your field is worth more than hundreds of links from spammy directories. Buying links or doing link schemes breaks Google's spam policies and can get your site demoted.

## 17: What is the difference between internal and external links?

- **Internal links** point to other pages on the same site, like your menu, breadcrumbs or "related articles". They help users and bots find pages and show which pages are important.
- **External links** point to other sites. Links from your site to others are outbound links; links from other sites to yours are backlinks.

Internal linking is fully under your control, which makes it one of the easiest SEO improvements a developer can make.

## 18: What is anchor text?

Anchor text is the clickable text of a link:

```html
<a href="/guides/trail-running">trail running guide</a>
```

Search engines use it to understand what the target page is about. "Trail running guide" says much more than "click here" or "read more". Keep it descriptive and natural. Exact-match keyword anchor text repeated everywhere, especially in backlinks, can look spammy.

## 19: What is a 301 redirect and when do you use it instead of a 302?

- **301 (Moved Permanently)** and **308**: the page moved for good. Search engines move the signals to the new URL and show the new URL in results.
- **302 (Found)** and **307**: the move is temporary. Search engines usually keep the old URL indexed.

Use 301/308 when you change URLs, merge pages, move to HTTPS or change domain. Use 302/307 for short-term cases like a temporary promotion page or A/B tests. Do redirects on the server, not with JavaScript or meta refresh, when you can.

```nginx
location = /old-page {
  return 301 /new-page;
}
```

## 20: What is a 404 page, and does it hurt SEO?

A 404 means "Not Found". It is normal for removed pages to return 404, and having 404s does not hurt your site's rankings overall. Google simply drops those URLs from the index after a while.

What you should avoid:

- Internal links pointing to 404 pages (bad for users and crawling)
- Deleting pages that had good backlinks without redirecting them to a relevant replacement
- Returning 200 for a "not found" page (a soft 404)

A good 404 page returns the real 404 status code and helps the user with search or links to main sections.

## 21: What is Google Search Console?

Google Search Console is a free tool from Google that shows how your site performs in Google Search. You verify ownership of the site (with a DNS record, HTML file, meta tag and so on) and then you can:

- See clicks, impressions, CTR and average position per query and page
- Check which pages are indexed and why others are not
- Inspect a single URL and request indexing
- Submit sitemaps
- See Core Web Vitals, HTTPS and rich result reports
- Get alerts about manual actions and security issues

Bing has a similar tool called Bing Webmaster Tools.

## 22: What makes a URL SEO friendly?

An SEO friendly URL is short, readable and describes the page:

```txt
Good: https://example.com/blog/how-to-choose-running-shoes
Bad:  https://example.com/index.php?id=4821&cat=7&ref=abc
```

Tips:

- Use lowercase words separated by hyphens (not underscores).
- Keep it stable. Changing URLs means you need redirects.
- Avoid session IDs and unneeded parameters.
- Use a logical folder structure if it helps (`/blog/...`, `/products/...`).

URL keywords are a very small ranking factor. The bigger benefit is that clear URLs are easier to share and get more clicks.

## 23: What is mobile-first indexing?

Mobile-first indexing means Google mainly uses the mobile version of your page for crawling, indexing and ranking. Googlebot crawls as a smartphone for almost all sites now.

So if your mobile version hides content, drops structured data, has different titles or is missing images compared to desktop, Google will only see the mobile version. The easiest way to be safe is a responsive design where the same HTML is served to all devices.

## 24: Does HTTPS affect rankings?

Yes, but only a little. Google confirmed HTTPS as a lightweight ranking signal in 2014. More important, browsers mark HTTP pages as "Not secure", which hurts trust and clicks, and many modern browser features only work on HTTPS.

When moving to HTTPS, redirect every HTTP URL to its HTTPS version with a 301, update canonicals, internal links and sitemaps, and avoid mixed content.

## 25: What are Core Web Vitals?

Core Web Vitals are three metrics Google uses to measure real user experience on a page:

| Metric                              | What it measures                                                         | Good           |
| ----------------------------------- | ------------------------------------------------------------------------ | -------------- |
| **LCP** (Largest Contentful Paint)  | Loading: when the main content shows up                                  | 2.5 s or less  |
| **INP** (Interaction to Next Paint) | Responsiveness: how fast the page reacts to clicks, taps and key presses | 200 ms or less |
| **CLS** (Cumulative Layout Shift)   | Visual stability: how much things jump around                            | 0.1 or less    |

They are measured at the 75th percentile of real visits. INP replaced FID in March 2024. They are part of Google's page experience signals. They help, but relevant content still matters much more.

## 26: What is structured data?

Structured data is extra code that describes the content of a page in a standard format, so search engines understand it without guessing. Most sites use the schema.org vocabulary in JSON-LD format:

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "Trail Runner 3",
    "image": "https://example.com/img/trail-runner-3.jpg",
    "offers": {
      "@type": "Offer",
      "price": "119.99",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock"
    }
  }
</script>
```

Structured data is not a direct ranking factor, but it can make the page eligible for rich results.

## 27: What are rich results?

Rich results are search results with extra visual information beyond the title, URL and snippet, such as review stars, prices, product availability, recipe images and cooking time, event dates, breadcrumbs or video thumbnails.

They usually come from structured data. Adding the markup makes a page eligible, but Google decides whether to show the rich result. Some types have been reduced over time (for example, FAQ rich results are now mostly limited to government and health sites, and HowTo rich results were removed), so check Google's current documentation before investing in a type.

## 28: What is keyword research?

Keyword research is finding out what words and questions people use when they search for things related to your site, and how often. It tells you what pages to create and what words to use in them.

Things you look at:

- **Search volume**: how many people search for it
- **Difficulty**: how strong the pages that already rank are
- **Intent**: what the person wants (learn something, find a specific site, compare, buy)

Common tools are Google Keyword Planner, Search Console (queries you already get impressions for), Ahrefs, Semrush and Google's autocomplete and "People also ask".

## 29: What is duplicate content? Is there a penalty for it?

Duplicate content is the same or very similar content on more than one URL, for example the same product page reachable through several category paths, or with and without tracking parameters.

There is no penalty for normal duplicate content. Google picks one version to show and filters out the rest. The problem is that Google might pick a URL you don't want, and that signals like links get split. Fix it with canonical tags, redirects, consistent internal links and by not creating needless URL variations. Copying content from other sites on purpose to manipulate rankings is a different thing and can be treated as spam.

## 30: What are Open Graph tags and do they help SEO?

Open Graph tags control how a link looks when it is shared on social networks and messaging apps (title, description, image):

```html
<meta property="og:title" content="How to Choose Running Shoes" />
<meta
  property="og:description"
  content="A simple guide to picking shoes for your foot type."
/>
<meta
  property="og:image"
  content="https://example.com/img/og/running-shoes.jpg"
/>
<meta
  property="og:url"
  content="https://example.com/blog/how-to-choose-running-shoes"
/>
<meta name="twitter:card" content="summary_large_image" />
```

They are not a Google ranking factor. They still matter because a good preview gets more clicks and shares, which brings traffic and can lead to links.

# Moderate Questions (31-60)

## 31: What is the difference between on-page, off-page and technical SEO?

- **On-page SEO**: what is on the page itself. Content, titles, headings, internal links, images, structured data.
- **Off-page SEO**: signals from outside your site. Mostly backlinks, but also brand mentions and reviews.
- **Technical SEO**: making sure search engines can crawl, render and index the site. Status codes, redirects, robots.txt, sitemaps, canonicals, JavaScript rendering, site speed, mobile support, hreflang.

Developers mostly own technical SEO and a good part of on-page SEO (templates, metadata, markup).

## 32: How do you write a good title tag, and why does Google sometimes change it?

A good title:

- Is unique for every page
- Says what the page is about in plain words, with the main topic near the start
- Is short enough not to get cut off (roughly 50-60 characters; the real limit is pixel width)
- Optionally ends with the brand name

```html
<title>Trail Running Shoes for Women | ShoeShop</title>
```

Google can show a different title link if your title is missing, too long, stuffed with keywords, the same on many pages or doesn't match the content. In that case it takes text from the `<h1>`, other headings, anchor text or the page. The fix is usually to make the title more accurate and to keep it close to the main heading.

## 33: What happens if a page is blocked in robots.txt and also has a noindex tag?

The `noindex` will not work. Because the page is blocked from crawling, Google never downloads it, so it never sees the `noindex` tag. If other pages link to that URL, Google can still index it, showing it with no description.

If you want a page removed from search results:

1. Allow crawling in robots.txt.
2. Add `noindex` (meta tag or `X-Robots-Tag` header).
3. Wait until Google recrawls it and drops it. You can use the Removals tool in Search Console to hide it faster for a while.

Only block it in robots.txt after it has dropped out, if you need to.

## 34: What is the X-Robots-Tag header and when do you use it?

`X-Robots-Tag` is an HTTP response header that does the same job as the robots meta tag. You need it for files that are not HTML, like PDFs, images or JSON, because they have no `<head>`.

```http
HTTP/1.1 200 OK
Content-Type: application/pdf
X-Robots-Tag: noindex
```

Example in Nginx for all PDFs:

```nginx
location ~* \.pdf$ {
  add_header X-Robots-Tag "noindex, nofollow";
}
```

It is also handy when you want to set rules for a whole section at the server level without touching templates.

## 35: Is the canonical tag a rule or a hint? How does Google pick the canonical?

It is a strong hint, not a rule. Google looks at several signals to pick the canonical URL of a duplicate group:

- `rel="canonical"` tags
- Redirects
- Which URL is in the sitemap
- Which URL internal links point to
- HTTPS over HTTP
- Hreflang clusters
- Which URL looks cleaner

If these signals disagree (for example canonical points to A, but the sitemap and all internal links use B), Google may ignore your canonical. You can see the "Google-selected canonical" in the URL Inspection tool. Keep all signals consistent, and don't point a canonical to a page that redirects, returns 404 or has `noindex`.

## 36: What do rel="nofollow", rel="sponsored" and rel="ugc" mean?

They are link attributes that describe your relationship with the linked page:

```html
<a href="https://partner.com" rel="sponsored">Our partner</a>
<a href="https://user-site.com" rel="ugc">User's site</a>
<a href="https://unknown.com" rel="nofollow">Some link</a>
```

- `sponsored`: paid links, ads, affiliate links
- `ugc`: user generated content, like comments and forum posts
- `nofollow`: you don't want to vouch for the link, and none of the above fits

Since 2019-2020 Google treats all three as hints, not strict rules. Paid links must be marked with `sponsored` or `nofollow`, otherwise they break Google's link spam policies. Don't put `nofollow` on your own internal links to "save PageRank"; it doesn't work that way.

## 37: How do you add structured data with JSON-LD?

Put a `<script type="application/ld+json">` block anywhere in the HTML (usually the `<head>`). It doesn't need to be tied to the visible markup, which makes it easy to generate from your data.

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "How to Choose Running Shoes",
    "image": ["https://example.com/img/running-shoes-1x1.jpg"],
    "datePublished": "2026-08-10T08:00:00+00:00",
    "dateModified": "2026-09-02T10:30:00+00:00",
    "author": [
      {
        "@type": "Person",
        "name": "Jane Smith",
        "url": "https://example.com/authors/jane-smith"
      }
    ]
  }
</script>
```

Google recommends JSON-LD over Microdata and RDFa. The data must match what users see on the page. Marking up content that is not visible, or fake reviews, can lead to a manual action.

If you build the JSON with a template, escape it correctly. Inserting user text directly into the script tag can break the JSON or allow XSS if it contains `</script>`.

## 38: How do you test and monitor structured data?

- **Rich Results Test** (search.google.com/test/rich-results): checks if a page or code snippet is eligible for Google rich results and shows errors and warnings.
- **Schema Markup Validator** (validator.schema.org): checks general schema.org validity, not just what Google supports.
- **Search Console enhancement reports**: show errors across the whole site for each rich result type Google detected, and let you validate fixes.
- **URL Inspection tool**: shows the structured data Google found on the rendered page.

Test the rendered page, not only the source, especially if the JSON-LD is added by JavaScript.

## 39: How do you make a single-page application crawlable?

- Use real links with `href` for navigation. Google follows `<a href="/products/1">`, not `<div onclick="go(1)">` or `<a>` without `href`.
- Use the History API (`pushState`) with clean paths, not hash URLs like `/#/products/1`. Google ignores the part after `#`.
- Give every view its own URL that returns the full content when loaded directly.
- Update `<title>`, meta description and canonical for each route.
- Return correct status codes, or at least handle "not found" pages properly (see soft 404).
- Prefer server-side rendering or static generation for important pages so the content is in the initial HTML.

```html
<!-- Crawlable -->
<a href="/products/42">Trail Runner 3</a>

<!-- Not crawlable -->
<span onclick="router.navigate('/products/42')">Trail Runner 3</span>
```

## 40: Does Google run JavaScript? How does it index JS-heavy pages?

Yes. Googlebot uses an up-to-date (evergreen) version of Chromium to render pages. The process is:

1. **Crawl**: fetch the HTML.
2. **Render**: the page goes into a render queue. Later, Chromium runs the JavaScript and builds the final DOM.
3. **Index**: Google indexes the rendered HTML.

Rendering is usually fast now, but it can still be delayed, and it can fail if scripts error out, time out, or need resources blocked by robots.txt. Other search engines and many AI crawlers render JavaScript less well, or not at all. That is why important content and links should be in the server HTML when possible.

## 41: What is the difference between CSR, SSR and SSG for SEO?

- **CSR (client-side rendering)**: the server sends a nearly empty HTML shell and JavaScript builds the page in the browser. Google can index it after rendering, but it is slower to show content, more fragile, and other bots may see nothing.
- **SSR (server-side rendering)**: the server builds the full HTML for each request. Bots get the content right away. Good for pages that change often or depend on the request.
- **SSG (static site generation)**: pages are built to HTML at build time and served from a CDN. Fastest and very crawlable. Good for content that doesn't change often. ISR (incremental static regeneration) refreshes static pages after some time.

For SEO, SSR and SSG are the safest choices for public pages. CSR is fine for pages behind login that don't need to rank.

## 42: How do you set page metadata in the Next.js App Router?

Export a `metadata` object for static values, or a `generateMetadata` function for dynamic values, from a `layout.tsx` or `page.tsx`:

```tsx
// app/products/[slug]/page.tsx
import type { Metadata } from "next";

type Props = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const product = await getProduct(slug);

  return {
    title: `${product.name} | ShoeShop`,
    description: product.shortDescription,
    alternates: { canonical: `/products/${slug}` },
    openGraph: {
      title: product.name,
      images: [product.imageUrl],
    },
  };
}

export default async function ProductPage({ params }: Props) {
  const { slug } = await params;
  const product = await getProduct(slug);
  return <h1>{product.name}</h1>;
}
```

Set `metadataBase` in the root layout so relative URLs (like the canonical above) become absolute. Next.js renders these tags on the server, so bots see them in the HTML.

## 43: How do you generate a sitemap and robots.txt in Next.js?

Next.js supports special files in the `app` folder:

```ts
// app/sitemap.ts
import type { MetadataRoute } from "next";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getPosts();

  return [
    { url: "https://example.com", lastModified: new Date() },
    ...posts.map((post) => ({
      url: `https://example.com/blog/${post.slug}`,
      lastModified: post.updatedAt,
    })),
  ];
}
```

```ts
// app/robots.ts
import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/", disallow: "/admin/" },
    sitemap: "https://example.com/sitemap.xml",
  };
}
```

They are served at `/sitemap.xml` and `/robots.txt`. For very large sites you can use `generateSitemaps` to split the sitemap into several files.

## 44: What is a soft 404 and how do you avoid it in an SPA?

A soft 404 is a page that tells users "not found" (or is basically empty) but returns status `200`. Google detects many of these and reports them in Search Console as "Soft 404". They waste crawl budget and can get indexed as junk.

In a server-rendered app, return a real `404` status. In a client-side SPA, where the server always returns 200 for the shell, you have two common options:

```js
// Option 1: send the user to a URL that the server answers with 404
window.location.href = "/not-found";

// Option 2: add noindex to the page when the item doesn't exist
const meta = document.createElement("meta");
meta.name = "robots";
meta.content = "noindex";
document.head.appendChild(meta);
```

The better long-term fix is to render the route on the server so it can send the right status code.

## 45: How should you handle pagination for SEO?

- Give each page its own URL, like `/blog?page=2` or `/blog/page/2`.
- Link the pages with normal `<a href>` links (next, previous, page numbers) so Google can crawl through them.
- Let each page have a self-referencing canonical. Don't canonical page 2, 3, 4 to page 1, because then Google may not index the items that only appear on later pages.
- Don't `noindex` paginated pages if they are the only path to the items on them.
- Avoid putting the same intro text on every page.

Google stopped using `rel="next"` and `rel="prev"` as an indexing signal in 2019. They are harmless and other search engines may still use them, but you can't rely on them.

## 46: What is hreflang and how do you use it?

`hreflang` tells search engines which language and region versions of a page exist, so they show the right one to each user.

```html
<link rel="alternate" hreflang="en-us" href="https://example.com/en-us/shoes" />
<link rel="alternate" hreflang="en-gb" href="https://example.com/en-gb/shoes" />
<link rel="alternate" hreflang="de" href="https://example.com/de/schuhe" />
<link rel="alternate" hreflang="x-default" href="https://example.com/shoes" />
```

Rules:

- Every version must list all versions, including itself.
- Links must be reciprocal. If A points to B, B must point back to A, or Google may ignore it.
- Use ISO 639-1 language codes, optionally with an ISO 3166-1 region code (`en-gb`, not `en-uk`).
- `x-default` is the fallback for users who don't match any listed version.
- Point to canonical, indexable URLs.

Hreflang doesn't fix translation quality and doesn't make a page rank. It only helps swap in the right version.

## 47: How do you lazy load images without hurting SEO?

Use native lazy loading for images below the fold:

```html
<img
  src="/img/shoe-2.jpg"
  alt="Blue road running shoe"
  width="800"
  height="600"
  loading="lazy"
/>
```

Googlebot supports this, and the image stays in the HTML with a real `src`. Things to avoid:

- Lazy loading the LCP image (the hero image at the top). It delays LCP. Load it normally and you can add `fetchpriority="high"`.
- Custom lazy loaders that only put the real URL in `data-src` and swap it on scroll. Googlebot doesn't scroll, so it may never see the image.
- Leaving out `width` and `height`, which causes layout shifts.

## 48: What is LCP and how do you improve it?

LCP (Largest Contentful Paint) is the time until the largest image or text block in the viewport is rendered. Good is 2.5 seconds or less.

LCP time can be split into four parts, and you fix whichever is biggest:

1. **Time to First Byte**: slow server, no caching, no CDN, redirects.
2. **Resource load delay**: the browser finds the LCP image late (for example it is a CSS background or added by JavaScript).
3. **Resource load time**: the image is too big or not compressed.
4. **Render delay**: render-blocking CSS/JS, or the element is rendered by client-side JS.

Common fixes:

```html
<link rel="preload" as="image" href="/img/hero.avif" fetchpriority="high" />
<img
  src="/img/hero.avif"
  alt="Runner on a mountain trail"
  width="1200"
  height="600"
  fetchpriority="high"
/>
```

Plus: use a CDN, cache HTML, serve modern formats (AVIF/WebP) with responsive sizes, render content on the server, and remove or defer render-blocking scripts.

## 49: What is INP and how is it different from FID?

INP (Interaction to Next Paint) measures how long it takes from a user interaction (click, tap, key press) until the browser paints the next frame. It looks at all interactions during the visit and reports roughly the worst one. Good is 200 ms or less.

FID (First Input Delay) only measured the delay before the **first** interaction started being handled. It ignored the processing time and everything that happened later, so most sites passed it easily. INP replaced FID as a Core Web Vital in March 2024.

INP is made of three parts: input delay (main thread busy), processing time (your event handlers) and presentation delay (rendering the update). Long JavaScript tasks are the usual cause of bad INP.

## 50: What is CLS and how do you fix it?

CLS (Cumulative Layout Shift) measures how much visible content moves around unexpectedly while the page is open. Good is 0.1 or less.

Common causes and fixes:

- **Images and videos without size**: always set `width` and `height` or CSS `aspect-ratio`.
- **Ads, embeds and banners injected late**: reserve space for them with a fixed `min-height`.
- **Web fonts swapping**: use `font-display: optional` or adjust the fallback font with `size-adjust` so the text doesn't reflow much.
- **Content inserted above existing content**: like a cookie bar or "new posts" bar pushing the page down. Use overlays or insert below.
- **Animating layout properties**: animate `transform` and `opacity` instead of `top`, `height` and so on.

Shifts that happen within 500 ms after a user interaction don't count, because the user expects them.

## 51: What is the difference between field data and lab data?

- **Field data** (real user monitoring, RUM) comes from real visitors. Google's source is the Chrome UX Report (CrUX), which collects data from opted-in Chrome users over a 28-day window. This is what Google uses for the Core Web Vitals assessment.
- **Lab data** comes from a test in a controlled setup, like Lighthouse in Chrome DevTools. It is good for debugging, but it uses one device and one network profile and can't measure real interactions well (INP needs real users; in the lab you use Total Blocking Time as a proxy).

PageSpeed Insights shows both: CrUX field data at the top (if the page has enough traffic) and a Lighthouse lab run below. You can also collect your own field data with the `web-vitals` JavaScript library:

```js
import { onLCP, onINP, onCLS } from "web-vitals";

onLCP(sendToAnalytics);
onINP(sendToAnalytics);
onCLS(sendToAnalytics);
```

## 52: What does the URL Inspection tool in Search Console show you?

For one URL it shows:

- Whether it is indexed, and if not, why
- How Google discovered it (sitemaps, referring pages)
- Last crawl date and the user agent used
- Whether crawling and indexing are allowed
- The user-declared canonical and the Google-selected canonical
- Detected structured data and other enhancements

With "Test live URL" you can see the rendered HTML, a screenshot, the page resources that failed to load and JavaScript console messages. This is the best way to check what Googlebot actually sees on a JavaScript page. You can also click "Request indexing" after you fix or publish a page.

## 53: What is keyword cannibalization?

It happens when several pages on your site target the same search intent, so they compete with each other. Google keeps switching which one ranks, or none of them ranks well.

You can spot it in Search Console by filtering by a query and looking at which pages get impressions for it. Fixes:

- Merge the pages into one stronger page and 301 redirect the others
- Make each page clearly target a different intent
- Adjust internal links and anchor text so it is clear which page is the main one

Having several pages rank for similar terms is not always a problem. It is only cannibalization when they hurt each other.

## 54: What is E-E-A-T?

E-E-A-T stands for Experience, Expertise, Authoritativeness and Trustworthiness. It comes from Google's Search Quality Rater Guidelines, which human raters use to evaluate search results. It is not a single ranking signal or score, but Google's systems try to reward content that shows these qualities.

In practice:

- Show who wrote the content and why they know the topic (author pages, bios)
- Show first-hand experience (real photos, real testing)
- Be clear about who runs the site, with contact info and policies
- Cite sources and keep content accurate and updated

Trust is the most important part, especially for "Your Money or Your Life" topics like health, finance and safety.

## 55: What are orphan pages and how do you find them?

Orphan pages are pages that no other page on the site links to. Search engines may only find them through the sitemap or external links, and they usually get little crawling and weak rankings.

To find them, compare two lists:

1. All URLs you expect to exist (from your database, CMS, sitemap or analytics)
2. All URLs a crawler (Screaming Frog, Sitebulb, and so on) finds by following links from the homepage

URLs in list 1 but not in list 2 are orphans. Then link to them from relevant pages, or remove or redirect them if they are not needed.

## 56: How do you handle URL parameters like sorting, filters and tracking codes?

Parameters can create thousands of URLs with the same or similar content. Ways to handle them:

- **Tracking parameters** (`utm_source`, `gclid`): canonical to the clean URL and don't use them in internal links.
- **Sorting and view options** (`?sort=price`, `?view=grid`): canonical to the main URL.
- **Filters that create useful pages** (like `/shoes?color=red` if people search "red shoes"): consider giving them a clean, indexable URL with a self canonical and real content.
- **Useless combinations**: avoid linking to them, or block their crawling in robots.txt if they eat a lot of crawl budget.

Keep parameters in a consistent order so `?a=1&b=2` and `?b=2&a=1` don't become two URLs. Google retired the URL Parameters tool in Search Console in 2022, so you have to handle this on your side.

## 57: How do you avoid duplicates from www, trailing slashes and HTTP vs HTTPS?

These all can create separate URLs for the same page:

```txt
http://example.com/shoes
https://example.com/shoes
https://www.example.com/shoes
https://www.example.com/shoes/
https://www.example.com/Shoes
```

Pick one version and enforce it:

- 301 redirect every other variant to the chosen one (one hop, not a chain)
- Use the chosen form in canonicals, internal links and sitemaps
- Add HSTS once HTTPS is stable

URL paths are case sensitive for Google, so `/Shoes` and `/shoes` are different URLs. Lowercase everything and redirect uppercase variants.

## 58: How do you control what Google shows in the snippet?

With robots directives and an HTML attribute:

```html
<!-- No text snippet or video preview at all -->
<meta name="robots" content="nosnippet" />

<!-- Snippet max 120 characters, large image previews allowed -->
<meta name="robots" content="max-snippet:120, max-image-preview:large" />

<!-- Exclude part of the page from snippets -->
<p data-nosnippet>Internal pricing note that shouldn't appear in search.</p>
```

Other options are `max-video-preview:<seconds>` and `noimageindex`. Google also says that `nosnippet` and `data-nosnippet` keep content from being used as direct input for AI Overviews and AI Mode. Be careful: `nosnippet` can lower clicks, because your result looks empty. `max-image-preview:large` is recommended if you want big images in Discover.

## 59: What is breadcrumb structured data and why use it?

Breadcrumbs show where a page sits in the site hierarchy. Visible breadcrumbs help users and create internal links up the hierarchy. With `BreadcrumbList` markup, search engines understand that hierarchy:

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Shoes",
        "item": "https://example.com/shoes"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Running",
        "item": "https://example.com/shoes/running"
      },
      { "@type": "ListItem", "position": 3, "name": "Trail Runner 3" }
    ]
  }
</script>
```

The last item can leave out `item` because it is the current page. Google may use this to show the page's position in the site. Note that on mobile, Google shows just the domain in the URL line, so the visible effect is mostly on desktop.

## 60: What is the difference between 404, 410 and 503 for SEO?

- **404 Not Found**: the page doesn't exist. Google drops it from the index after some recrawls.
- **410 Gone**: the page was removed on purpose and won't come back. Google treats it almost the same as 404; it may drop the URL a little faster. Use it when you are sure.
- **503 Service Unavailable**: a temporary problem, like maintenance. Google keeps the page in the index and tries again later. Add a `Retry-After` header.

```http
HTTP/1.1 503 Service Unavailable
Retry-After: 3600
```

Don't keep a site on 503 for many days. If it lasts too long, Google starts treating the URLs as gone. And never show a maintenance page with a 200 status, or Google may index the maintenance message.

# Advanced Questions (61-90)

## 61: What is crawl budget and when should you care about it?

Crawl budget is how many URLs Googlebot can and wants to crawl on your site in a given time. It depends on two things:

- **Crawl capacity limit**: how much Google can crawl without overloading your server. Fast, error-free responses raise it. Slow responses and server errors lower it.
- **Crawl demand**: how much Google wants to crawl, based on how popular and how often updated your URLs are.

Most sites don't need to worry about it. Google says it matters mainly for very large sites (around a million or more pages that change weekly) or medium sites (10,000+ pages) whose content changes daily, and for sites with lots of URLs stuck as "Discovered - currently not indexed".

To use it better: remove or block infinite URL spaces (filters, calendars, session IDs), fix redirect chains, return real 404s instead of soft 404s, keep sitemaps clean and make the server fast. Remember that every resource Googlebot fetches for rendering (JS, CSS, API calls) also uses crawl budget.

## 62: How do server errors and slow responses affect crawling?

Googlebot adjusts its crawl rate based on how your server responds:

- If the server responds fast, Google may crawl more.
- If responses get slow, or you return many `500`, `503` or `429` responses, Google slows down crawling.
- If errors continue for a long time, already indexed URLs can be dropped.

This is why a slow backend or an aggressive rate limiter can hurt SEO even if users don't notice much. Check the Crawl Stats report in Search Console for response time, response codes and host availability. If you need Google to crawl less for a short time (for example during an incident), returning `503` or `429` is the right tool. Don't block Googlebot with `403` or `404`, because those mean something else.

## 63: What happens when robots.txt returns an error?

Google treats it differently depending on the status code:

- **200**: rules are read normally. Google caches the file for up to about 24 hours.
- **3xx**: Google follows up to five redirects. After that it treats it like a 404.
- **4xx (except 429)**: Google assumes there is no robots.txt and crawls everything.
- **5xx or 429**: Google assumes the whole site is disallowed and stops crawling for now. If the file stays unreachable for more than 30 days, it uses the last cached copy, or assumes no restrictions if it has none.

So a robots.txt endpoint that returns 500 because of a bug can stop Google from crawling your entire site. Monitor it like any other critical endpoint. Also note that Google reads only the first 500 KiB of the file.

## 64: How do you migrate a site to a new domain without losing traffic?

1. **Prepare a URL map**: list every old URL (from crawls, sitemaps, analytics, Search Console and backlink tools) and its new URL. Map pages one to one to the closest equivalent, not everything to the homepage.
2. **Set up the new site**: same content, correct canonicals pointing to the new domain, updated internal links, new sitemaps, structured data and hreflang.
3. **Redirect**: 301 every old URL to its new URL in one hop, at the server level.
4. **Tell Google**: verify both domains in Search Console and use the Change of Address tool. Submit the new sitemaps. Keeping an old sitemap with the old URLs for a while can help Google find the redirects faster.
5. **Monitor**: watch 404s, crawl errors, index coverage and traffic for both domains. Fix broken redirects quickly.
6. **Keep the redirects** for at least a year, ideally forever, and keep the old domain registered.

Expect some ranking fluctuation for a few weeks. Avoid combining a migration with a redesign, content changes and a URL structure change all at once, because if traffic drops you won't know why.

## 65: How do you handle faceted navigation on a large e-commerce site?

Facets (color, size, brand, price, sort) can combine into millions of URLs. Most of them are near duplicates, and crawling them wastes budget. A typical approach:

- **Decide which facet pages deserve to rank**, based on search demand (for example "women's trail running shoes" or "nike running shoes"). Give them clean, static URLs, unique titles, headings and some unique text, and link to them.
- **For the rest**, don't let them become crawlable URLs:
  - Apply filters without changing to a new crawlable link (for example a form or a button that updates the list), or
  - Block the parameter patterns in robots.txt, or
  - Use canonical tags to the main category (weaker, because Google still has to crawl them).
- **Return 404** for impossible or empty combinations instead of a 200 "no products" page.
- Keep parameter order consistent and avoid putting filter state in URLs that get linked internally by default.

Google's own advice is: if you don't need facet URLs indexed, block their crawling with robots.txt or use URL fragments for filter state; if you do, use a consistent format and return 404 for empty results.

## 66: How do you make infinite scroll SEO friendly?

Googlebot doesn't scroll like a user, so content that loads only on scroll may never be seen. The usual fix is to back infinite scroll with paginated URLs:

- Split the content into pages with their own URLs (`/blog?page=2`).
- Each page can be loaded directly and shows its own items.
- Add normal pagination links (`<a href="/blog?page=2">`) so crawlers can reach every page. They can be visible links at the bottom, or a "Load more" link that JavaScript enhances.
- As the user scrolls, update the URL with `history.pushState` or `replaceState` to the page they are on.

```js
const observer = new IntersectionObserver(async ([entry]) => {
  if (!entry.isIntersecting) return;
  nextPage++;
  await appendItems(nextPage);
  history.replaceState(null, "", `/blog?page=${nextPage}`);
});

observer.observe(document.querySelector("#load-more"));
```

## 67: What is dynamic rendering and should you still use it?

Dynamic rendering means detecting bots by user agent and serving them a pre-rendered HTML version (made with a tool like a headless browser), while users get the normal client-side app.

Google now calls it a workaround and does not recommend it. It adds complexity, the bot version can get out of sync with the real one, and it can look like cloaking if the content differs. Use server-side rendering, static generation or hydration instead. You may still meet it in older projects that use services like Prerender.io. If you keep it, make sure the content served to bots is the same as what users see.

## 68: What are common JavaScript SEO problems?

- **Content that only appears after interaction** (clicking a tab, "show more" that fetches data, scroll). Googlebot doesn't click or scroll.
- **Links without `href`**, so Google can't discover pages.
- **Blocked resources**: JS, CSS or API URLs disallowed in robots.txt, so rendering fails.
- **JavaScript errors** or using APIs the renderer doesn't support, so the page renders empty.
- **Metadata set too late or wrong**: canonical, robots or title tags that differ between the server HTML and the rendered HTML. For example, the server HTML has `noindex` and JS removes it. Google may never render the page, because it sees `noindex` first.
- **Hash routing** (`/#/page`).
- **Slow API calls** during render, so the content isn't there when the snapshot is taken.
- **Soft 404s** from routes that show "not found" with a 200.

Test with the URL Inspection tool (rendered HTML and screenshot) and compare the rendered HTML with the raw HTML.

## 69: What are the limitations of Googlebot's renderer?

- It doesn't keep state between page loads: cookies, `localStorage` and `sessionStorage` are cleared, so each URL must work as a fresh visit.
- It declines permission prompts (camera, location, notifications).
- It doesn't click, type or scroll. It uses a tall viewport instead of scrolling, so `IntersectionObserver` based lazy loading usually works, but scroll event based loading may not.
- It only processes the first 15 MB of each HTML file or resource it fetches.
- It may not wait forever for slow requests or timers.
- It respects robots.txt for every resource, including API endpoints.
- It caches resources aggressively and may ignore cache headers, so use content hashes in file names (`app.3f9a2c.js`) to avoid it using an old JS file with new HTML.

Also, `content-visibility`, service workers and some browser features behave differently or are not used. Design pages so the important content and links exist without user interaction.

## 70: How do you debug pages stuck in "Discovered - currently not indexed" or "Crawled - currently not indexed"?

These are two different problems:

- **Discovered - currently not indexed**: Google knows the URL but hasn't crawled it yet. Usually a crawl budget or server capacity issue, or Google doesn't think the URL is important enough. Check: server response times, too many low-value URLs (facets, parameters), weak internal linking to these pages, and the Crawl Stats report.
- **Crawled - currently not indexed**: Google crawled it and decided not to index it, at least for now. Usually a quality or duplication issue. Check: is the content thin or very similar to other pages? Does it render properly? Does it add anything compared to what is already indexed?

Fixes include improving or merging thin pages, linking to important pages from strong pages, removing junk URLs so Google focuses on the good ones, and making the server faster. "Request indexing" can help for a few URLs but doesn't fix the root cause.

## 71: How do you use server log analysis for SEO?

Server logs show every request Googlebot (and other bots) actually made, which tools like Search Console only show partly. From logs you can find:

- Which sections Google crawls most and which it ignores
- Crawl budget wasted on parameters, redirects, 404s or old URLs
- Status codes and response times bots get
- How quickly new or updated pages get crawled
- Orphan URLs that bots still hit
- Whether AI crawlers or fake "Googlebots" are hitting your site

You typically export access logs (from Nginx, a CDN or a load balancer), filter by verified bot requests and group by URL pattern, status code and date. Tools like Screaming Frog Log File Analyser help, or you can use BigQuery or a simple script.

## 72: How do you verify that a request really comes from Googlebot?

The user agent can be faked by anyone, so don't trust it alone. Google's recommended method:

1. Do a reverse DNS lookup on the IP. The hostname must end with `googlebot.com`, `google.com` or `googleusercontent.com`.
2. Do a forward DNS lookup on that hostname and check it resolves back to the same IP.

```bash
$ host 66.249.66.1
1.66.249.66.in-addr.arpa domain name pointer crawl-66-249-66-1.googlebot.com.

$ host crawl-66-249-66-1.googlebot.com
crawl-66-249-66-1.googlebot.com has address 66.249.66.1
```

For automated checks at scale, Google publishes its crawler IP ranges as JSON files (for example `googlebot.json`), which you can download and match against. Bing and most large AI crawlers offer similar verification methods.

## 73: How should you structure an international site, and why are IP-based redirects risky?

Common structures:

| Structure     | Example               | Notes                                                                                       |
| ------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| ccTLD         | `example.de`          | Strongest country signal, but each domain builds authority separately and costs more to run |
| Subdirectory  | `example.com/de/`     | Easiest to manage, shares domain authority. Most common choice                              |
| Subdomain     | `de.example.com`      | Possible, often used when the sites are run on different setups                             |
| URL parameter | `example.com?lang=de` | Not recommended                                                                             |

Use hreflang between versions in all cases.

Automatically redirecting users by IP or `Accept-Language` is risky because Googlebot mostly crawls from US IP addresses and usually doesn't send `Accept-Language`. If you redirect everyone in the US to `/en-us/`, Google may never see your other versions. Better: let every version be accessible directly, and show a banner like "Looks like you're in Germany, go to the German site?" instead of forcing a redirect.

## 74: How do you manage hreflang for a large site?

There are three ways to declare hreflang, and you should pick one:

- **HTML `<link>` tags** in the `<head>`: simple, but on a page with 30 language versions it adds a lot of tags to every page.
- **HTTP headers**: useful for non-HTML files like PDFs.
- **XML sitemaps**: each `<url>` lists all alternates with `xhtml:link`. Keeps HTML light and is easier to generate from one source.

```xml
<url>
  <loc>https://example.com/en-us/shoes</loc>
  <xhtml:link rel="alternate" hreflang="en-us" href="https://example.com/en-us/shoes"/>
  <xhtml:link rel="alternate" hreflang="de" href="https://example.com/de/schuhe"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/shoes"/>
</url>
```

(The `urlset` element needs `xmlns:xhtml="http://www.w3.org/1999/xhtml"`.)

At scale, the usual problems are missing return links, pointing to redirected or `noindex` URLs, wrong codes, and pages that exist in one language but not another. Generate hreflang from a single mapping table in your database instead of per template, and audit it with a crawler regularly.

## 75: Does streaming SSR or hydration affect SEO?

Usually not, if done right. Googlebot waits for the full HTML response, so streamed HTML (for example React Suspense boundaries that stream content later in the same response) ends up in the HTML it processes.

Things to watch:

- **Metadata placement**: some frameworks stream metadata after the initial `<head>`. Next.js handles this by detecting bots with limited JS support and blocking on metadata for them, but you should check the raw HTML your bots receive.
- **Content fetched only on the client** after hydration (for example inside `useEffect`) is not in the server HTML. Google can render it, but it is slower and less reliable, and other crawlers may miss it.
- **Hydration errors** that make the client re-render or blank the page can break what the renderer sees.
- **Status codes**: once streaming starts, the status code is already sent (usually `200`). A "not found" detected later in the stream can't change it, so frameworks fall back to things like a `noindex` meta tag. Do lookups that decide 404 or redirect before streaming starts when possible.

## 76: How do you handle SEO for paywalled or login-only content?

If Google sees full content but users see a paywall, that can look like cloaking. Google allows it if you mark the paywalled part with structured data:

```html
<article>
  <p>Free intro text...</p>
  <div class="paywall">Full article for subscribers...</div>
</article>

<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "Inside the Shoe Industry",
    "isAccessibleForFree": false,
    "hasPart": {
      "@type": "WebPageElement",
      "isAccessibleForFree": false,
      "cssSelector": ".paywall"
    }
  }
</script>
```

Serve the full content to verified Googlebot only if you use this markup. Content fully behind a login (dashboards, account pages) can't and shouldn't be indexed; keep it out of sitemaps and make the public pages around it strong instead. Also make sure your paywall check doesn't depend on cookies Googlebot won't have.

## 77: What is cloaking and how can a developer cause it by accident?

Cloaking is showing different content to search engines than to users, to manipulate rankings. It breaks Google's spam policies and can lead to a manual action.

Developers can cause it by accident:

- User agent checks that serve bots a "lite" page with different text or links
- A/B tests that always show bots one variant with very different content (light A/B tests are fine; don't single out Googlebot)
- Geo or language redirects that send bots somewhere else
- A hacked site that shows spam only to Googlebot (a common hack pattern)
- Prerendering that is out of date compared to the live app

Small differences, like a smaller layout or no personalized content for bots, are fine. The main content and intent must be the same.

## 78: How do you investigate a sudden drop in organic traffic?

Work from the most likely technical causes to the less obvious ones:

1. **Check the data is real**: did analytics tracking break? Compare analytics with Search Console clicks.
2. **Find the scope**: which pages, sections, countries, devices and queries dropped? A drop in one template usually means a technical bug.
3. **Check recent deploys**: new `noindex`, changed canonicals, robots.txt changes, broken redirects, rendering errors, removed internal links, status code changes.
4. **Check Search Console**: Page indexing report, Crawl Stats, manual actions, security issues.
5. **Check Google updates**: did a core or spam update roll out on those dates? Google lists them on the Search Status Dashboard.
6. **Check the SERP itself**: maybe rankings are the same, but AI Overviews or new SERP features take the clicks. Compare impressions and position, not only clicks.
7. **Check competitors and seasonality**: maybe demand dropped (Google Trends) or someone else improved.

Write down what you find with dates, because SEO causes are often confused when several things change at once.

## 79: Which Google spam policies should developers know about?

Besides old ones like cloaking, hidden text, keyword stuffing, doorway pages, sneaky redirects and link schemes, Google added and clarified a few in 2024:

- **Scaled content abuse**: producing lots of pages mainly to manipulate rankings, with little value for users, whether made by AI, by people or by a mix.
- **Site reputation abuse**: a site hosting third-party pages (for example coupon or casino content) to use the host's ranking signals.
- **Expired domain abuse**: buying an expired domain and putting low-value content on it to use its old reputation.

Developers should also watch for things like hacked content, auto-generated pages from templates with no real data (for example "Plumber in [City]" pages that are all the same), and user-generated spam in comments or profiles. Violations can be handled by algorithms or by a manual action shown in Search Console.

## 80: Is AI-generated content bad for SEO?

Google doesn't penalize content just because AI helped make it. Its position is that it rewards helpful, original, reliable content, however it is produced.

What gets sites in trouble is using AI (or anything else) to mass-produce pages with no real value, which falls under scaled content abuse. Practical guidance:

- Use AI as a helper, but have people check facts and add real experience, data or opinions.
- Don't publish thousands of near-identical pages just to match keyword variations.
- Make sure each page answers the query better than what already exists.
- Be careful with structured data and metadata generated automatically; it must match the visible content.

## 81: How do AI Overviews and AI crawlers affect SEO, and how can you control them?

AI Overviews and AI Mode in Google, and AI search tools like ChatGPT search or Perplexity, answer questions directly and show a few cited sources. This can lower clicks for informational queries, while pages that get cited can still get traffic. The same basics apply: be crawlable and indexed, have clear and well-structured content, and be a trusted source.

Controls:

- **Google AI Overviews / AI Mode** use the normal Google Search index. You control them like snippets: `nosnippet`, `data-nosnippet` or `max-snippet`. Blocking them fully means blocking from Search.
- **Google-Extended** (a robots.txt token) controls whether your content is used to train and ground Gemini models. It does not affect Search ranking or AI Overviews.
- **Other AI crawlers** have their own user agents, often split by purpose, for example OpenAI's `GPTBot` (training) and `OAI-SearchBot` (search), or Anthropic's `ClaudeBot`.

```txt
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: OAI-SearchBot
Allow: /
```

Many AI crawlers don't run JavaScript, which is another reason to render content on the server.

## 82: What is llms.txt and does it help SEO?

`llms.txt` is a proposed standard (from 2024) for a Markdown file at `/llms.txt` that gives language models a short summary of a site and links to its most useful content, often in plain Markdown versions.

It is not a ranking factor. Google has said it doesn't use it for Search, and there is little evidence that major AI assistants rely on it. It can be useful for developer documentation sites, where tools and coding assistants may fetch it directly. Treat it as optional and cheap to add, not as an SEO strategy.

## 83: What is IndexNow?

IndexNow is a protocol that lets you notify search engines right away when a URL is added, updated or deleted, instead of waiting for them to crawl. It is supported by Bing, Yandex, Naver, Seznam and others. Google does not use it.

You host a key file on your site and send a request with the changed URLs:

```bash
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "host": "example.com",
    "key": "a1b2c3d4e5f6",
    "keyLocation": "https://example.com/a1b2c3d4e5f6.txt",
    "urlList": ["https://example.com/products/42"]
  }'
```

Participating engines share submissions with each other. For Google, keep sitemaps with accurate `lastmod` and good internal linking. Google's Indexing API is officially only for job posting and livestream pages.

## 84: How do you keep staging and preview environments out of search results?

The safest option is to put them behind authentication (HTTP basic auth, VPN or an IP allowlist). Bots can't index what they can't access.

If that's not possible:

- Send `X-Robots-Tag: noindex` on every response from that environment.
- Don't rely on robots.txt `Disallow` only. Blocked URLs can still get indexed if someone links to them.

The common mistake is the reverse: copying the staging config to production and launching with `noindex` or `Disallow: /`. Make these settings depend on the environment and add a check in your deploy pipeline:

```bash
# fail the production deploy if the homepage has noindex
if curl -s https://example.com | grep -qi 'name="robots" content="[^"]*noindex'; then
  echo "noindex found on production"; exit 1
fi
if curl -sI https://example.com | grep -qi 'x-robots-tag:.*noindex'; then
  echo "noindex header found on production"; exit 1
fi
```

If a staging site already got indexed, add authentication or `noindex`, then use the Removals tool in Search Console.

## 85: What should you know about image SEO beyond alt text?

- **Use real `<img>` elements** for content images. Google doesn't index CSS background images as images.
- **Responsive images** with `srcset`/`sizes` or `<picture>` are supported. Make sure the `src` fallback is a valid URL.
- **Modern formats** (AVIF, WebP) reduce size and help LCP. Google Images supports them.
- **Descriptive file names** (`red-trail-shoe.jpg` instead of `IMG_4821.jpg`) and good surrounding text help Google understand the image.
- **Image sitemaps** help Google discover images, for example ones loaded by JavaScript.
- **Images on a CDN on another domain** are fine, but that host must allow Googlebot to crawl them in its robots.txt.
- **Stable image URLs**: changing image URLs on every deploy makes Google re-discover them and can drop them from Google Images for a while.
- **`max-image-preview:large`** lets Google show big previews, which matters for Discover.

```html
<picture>
  <source
    type="image/avif"
    srcset="/img/shoe-800.avif 800w, /img/shoe-1600.avif 1600w"
    sizes="(max-width: 800px) 100vw, 800px"
  />
  <img
    src="/img/shoe-800.jpg"
    alt="Red trail running shoe, side view"
    width="800"
    height="600"
  />
</picture>
```

## 86: How do you catch SEO regressions automatically in CI?

SEO often breaks silently on deploy. Some checks you can automate:

- **Lighthouse CI** with budgets for performance and the SEO category.
- **Template tests** that render key page types and check title, meta description, canonical, robots tags, `h1`, hreflang and JSON-LD.
- **A crawl of the preview environment** (Screaming Frog CLI, a custom crawler) to find new 404s, redirect chains and missing tags.
- **robots.txt and sitemap tests**: the production robots.txt doesn't block important paths, and sitemap URLs return 200.
- **Real user monitoring** of Core Web Vitals with alerts after releases.

Example with Playwright:

```ts
import { test, expect } from "@playwright/test";

test("product page has correct SEO tags", async ({ page }) => {
  const response = await page.goto("/products/trail-runner-3");
  expect(response?.status()).toBe(200);

  await expect(page).toHaveTitle(/Trail Runner 3/);
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute(
    "href",
    "https://example.com/products/trail-runner-3",
  );
  await expect(
    page.locator('meta[name="robots"][content*="noindex"]'),
  ).toHaveCount(0);
  await expect(page.locator("h1")).toHaveCount(1);

  const jsonLd = await page
    .locator('script[type="application/ld+json"]')
    .first()
    .textContent();
  expect(JSON.parse(jsonLd ?? "{}")["@type"]).toBe("Product");
});
```

Note that this checks the rendered DOM. To be sure the tags are in the server HTML, also check the raw response body.

## 87: How do you handle many similar pages, like location pages or product variants?

These pages can easily look like doorway pages or duplicates.

**Location pages** ("Plumber in Austin", "Plumber in Dallas"): only create them if you really serve that place, and give each one real local information: address, opening hours, staff, reviews, local photos, service areas. If the only thing that changes is the city name, merge them into fewer pages.

**Product variants** (sizes, colors): usually one page for the product with variant selection, and one canonical URL. If a variant has its own search demand (like a specific color) you can give it its own URL with a self canonical and different content (images, title, availability). Google supports `ProductGroup` structured data with `hasVariant` and `variesBy` to describe variant groups.

The general rule: every indexable URL should have a clear reason to exist that users would agree with.

## 88: How do you improve INP on a heavy React page?

First, find the slow interactions with field data (the `web-vitals` library with attribution, or a RUM tool) and the Performance panel in DevTools. Then:

- **Break up long tasks** in event handlers, and give the browser a chance to paint between steps:

```js
async function handleFilterClick(filter) {
  setActiveFilter(filter); // quick visual feedback

  // let the browser paint before the heavy work
  if ("scheduler" in window && "yield" in scheduler) {
    await scheduler.yield();
  } else {
    await new Promise((resolve) => setTimeout(resolve, 0));
  }

  runExpensiveFiltering(filter);
}
```

- **Use `useTransition` or `useDeferredValue`** in React so heavy updates don't block urgent ones like typing.
- **Render less**: virtualize long lists, memoize expensive components, avoid state changes that re-render the whole tree.
- **Reduce third-party scripts** (tag managers, chat widgets) that keep the main thread busy.
- **Make DOM updates smaller** and avoid layout thrashing (reading and writing layout in a loop).
- **Hydrate less JavaScript**: React Server Components or partial hydration reduce the work done on the client.

## 89: How do you handle out-of-stock and discontinued products?

It depends on whether the product is coming back:

- **Temporarily out of stock**: keep the page live with a 200, show it clearly as out of stock, update `availability` in structured data to `https://schema.org/OutOfStock`, and offer alternatives or a "notify me" option. Don't `noindex` it; it keeps its rankings for when it returns.
- **Discontinued with a clear replacement**: 301 redirect to the new model or the closest product.
- **Discontinued with no replacement but still useful** (people search for it, it has backlinks): keep the page with information and links to similar products.
- **Discontinued and not useful**: return 404 or 410. Don't redirect everything to the homepage; Google often treats that as a soft 404 anyway.

On large stores, the bigger issue is usually thousands of empty category or filter pages that show "No products found" with a 200. Return 404 or `noindex` for those.

## 90: How do you plan internal linking for a large site?

Internal links decide how easily bots find pages and how link value spreads. For a large site:

- **Keep crawl depth low**: important pages should be reachable within a few clicks from the homepage.
- **Use a clear hierarchy**: homepage, then categories (hubs), then subcategories, then detail pages, with breadcrumbs linking back up.
- **Link sideways with purpose**: "related products", "related articles" or "other models from this brand" based on real relevance, not random.
- **Use descriptive anchor text** that matches the target page.
- **Don't hide navigation** in JavaScript that needs a click to load. Mega menus and footer links should be real `<a href>` links in the HTML.
- **Link from strong pages** (ones with many backlinks or traffic) to pages you want to push.
- **Avoid linking to junk URLs** (filtered combinations, tracking parameters, redirected URLs) in navigation.

Audit with a crawler: look at crawl depth, number of internal links per page (inlinks), and orphan pages. Search Console's Links report shows your most linked pages, which should match your most important ones.
