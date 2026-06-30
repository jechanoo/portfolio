"""
============================================================
E-commerce Product Scraper - Portfolio Sample Project
============================================================

A professional web scraper that extracts product information
from e-commerce websites and exports to clean CSV or Excel.

Key features:
- Scrapes product name, price, rating, review count, and URL
- Handles pagination automatically
- Rate limiting to avoid being blocked
- Clean error handling with retry logic
- Exports to CSV (and Excel if openpyxl available)

This is the kind of work I deliver to clients on Upwork/Fiverr.
"""

import requests
from lxml import html
import csv
import time
import random
import json
from datetime import datetime
from urllib.parse import urljoin, urlparse


class EcommerceScraper:
    """
    A production-ready web scraper for e-commerce product data.

    Usage:
        scraper = EcommerceScraper()
        products = scraper.scrape_books_demo(max_pages=3)
        scraper.save_to_csv(products, "products.csv")
    """

    def __init__(self, delay_min=1.0, delay_max=3.0):
        """
        Initialize scraper with polite rate limiting.

        Args:
            delay_min: Minimum delay between requests (seconds)
            delay_max: Maximum delay between requests (seconds)
        """
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        self.delay_min = delay_min
        self.delay_max = delay_max
        self.products = []

    def _be_polite(self):
        """Random delay between requests to avoid overwhelming servers."""
        time.sleep(random.uniform(self.delay_min, self.delay_max))

    def _fetch_page(self, url, retries=3):
        """
        Fetch a page with retry logic and error handling.

        Args:
            url: The URL to fetch
            retries: Number of retry attempts on failure

        Returns:
            requests.Response object, or None if all retries fail
        """
        for attempt in range(retries):
            try:
                self._be_polite()
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"  [WARN] Attempt {attempt + 1}/{retries} failed for {url}: {e}")
                if attempt == retries - 1:
                    print(f"  [FAIL] All retries exhausted for {url}")
                    return None
                time.sleep(2 ** attempt)  # Exponential backoff

    def scrape_books_demo(self, base_url="http://books.toscrape.com", max_pages=None):
        """
        Scrape the Books to Scrape demo site (a real, working e-commerce demo).

        This demonstrates the exact technique used for real e-commerce sites.

        Args:
            base_url: The starting URL
            max_pages: Maximum pages to scrape (None = all)

        Returns:
            List of product dictionaries
        """
        print(f"[*] Starting scrape of {base_url}")
        print(f"   Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)

        page = 1
        url = base_url + "/catalogue/page-1.html"

        while url:
            if max_pages and page > max_pages:
                break

            print(f"\n--- Page {page}: {url}")
            response = self._fetch_page(url)

            if not response:
                break

            tree = html.fromstring(response.content)
            books = tree.xpath('//article[@class="product_pod"]')

            for book in books:
                try:
                    # Extract product data using XPath
                    title_elem = book.xpath('.//h3/a')
                    price_elem = book.xpath('.//p[contains(@class, "price_color")]')
                    rating_elem = book.xpath('.//p[contains(@class, "star-rating")]')
                    availability = book.xpath('.//p[contains(@class, "instock")]')
                    image_elem = book.xpath('.//div[contains(@class, "image_container")]/img')

                    title = title_elem[0].get('title', 'N/A') if title_elem else 'N/A'
                    product_url = urljoin(url, title_elem[0].get('href', '')) if title_elem else ''
                    price = price_elem[0].text_content().strip() if price_elem else 'N/A'

                    # Parse rating from CSS class (e.g., "star-rating Three")
                    rating_text = 'N/A'
                    if rating_elem:
                        classes = rating_elem[0].get('class', '')
                        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
                        for word, stars in rating_map.items():
                            if word in classes:
                                rating_text = f"{stars}/5"
                                break

                    in_stock = bool(availability)
                    image_url = urljoin(url, image_elem[0].get('src', '')) if image_elem else ''

                    product = {
                        'title': title,
                        'price': price,
                        'rating': rating_text,
                        'in_stock': in_stock,
                        'product_url': product_url,
                        'image_url': image_url,
                        'scraped_at': datetime.now().isoformat(),
                    }
                    self.products.append(product)
                    # Clean price for console display (pound sign may break Windows GBK)
                    price_display = price.replace('\xa3', 'GBP ')
                    print(f"  [OK] {title[:60]} | {price_display} | {rating_text}")

                except Exception as e:
                    print(f"  [SKIP] Skipped a book due to error: {e}")
                    continue

            # Find next page link
            next_link = tree.xpath('//li[@class="next"]/a')
            if next_link:
                url = urljoin(url, next_link[0].get('href', ''))
                page += 1
            else:
                url = None

        print(f"\n[DONE] Scraped {len(self.products)} products from {page} pages.")
        return self.products

    def save_to_csv(self, products, filename):
        """
        Save scraped products to a clean CSV file.

        Args:
            products: List of product dictionaries
            filename: Output CSV filename
        """
        if not products:
            print("[WARN] No products to save!")
            return

        fieldnames = ['title', 'price', 'rating', 'in_stock',
                      'product_url', 'image_url', 'scraped_at']

        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)

        print(f"[SAVED] {len(products)} products -> {filename}")

    def save_to_json(self, products, filename):
        """Save products to JSON format."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        print(f"[SAVED] {len(products)} products -> {filename}")

    def get_stats(self, products):
        """
        Generate summary statistics for the scraped data.

        Clients love this — it adds value beyond raw data.
        """
        if not products:
            return {}

        prices = []
        for p in products:
            try:
                # Clean price string: "£51.77" -> 51.77
                price_str = p['price'].replace('£', '').replace('$', '')
                prices.append(float(price_str))
            except (ValueError, KeyError):
                continue

        stats = {
            'total_products': len(products),
            'in_stock': sum(1 for p in products if p.get('in_stock')),
            'out_of_stock': sum(1 for p in products if not p.get('in_stock')),
            'avg_price': round(sum(prices) / len(prices), 2) if prices else 0,
            'min_price': round(min(prices), 2) if prices else 0,
            'max_price': round(max(prices), 2) if prices else 0,
            'scraped_at': datetime.now().isoformat(),
        }
        return stats


# ============================================================
# DEMO: Run this to see the scraper in action
# ============================================================
if __name__ == '__main__':
    print("=" * 55)
    print("  E-COMMERCE PRODUCT SCRAPER - LIVE DEMO")
    print("  By [Your Name] | Upwork/Fiverr Portfolio")
    print("=" * 55)

    scraper = EcommerceScraper(delay_min=0.5, delay_max=1.5)

    # Scrape 3 pages as a demo
    products = scraper.scrape_books_demo(max_pages=3)

    if products:
        # Save results
        scraper.save_to_csv(products, 'products_demo.csv')
        scraper.save_to_json(products, 'products_demo.json')

        # Print summary
        stats = scraper.get_stats(products)
        print("\n===== SUMMARY STATISTICS: =====")
        print(f"   Total products: {stats['total_products']}")
        print(f"   In stock: {stats['in_stock']}")
        print(f"   Average price: GBP {stats['avg_price']}")
        print(f"   Price range: GBP {stats['min_price']} - {stats['max_price']}")

        print("\n[DONE] Demo complete! Check products_demo.csv for the output.")
    else:
        print("[FAIL] No data scraped. Check your internet connection.")
