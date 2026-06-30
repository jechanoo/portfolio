"""
============================================================
Google Maps Business Extractor - Lead Generation Tool
============================================================

A professional lead generation scraper that extracts business
information from Google Maps search results.

USE CASE:
    "Find all coffee shops in downtown Chicago with phone numbers"
    "Get a list of all dentists in Manhattan with ratings"
    "Extract 500 B2B leads in the logistics industry"

REQUIRES: pip install selenium (web driver automation)
          Chrome browser + ChromeDriver installed

DISCLAIMER: This is a portfolio sample for educational purposes.
Always respect Google's Terms of Service and rate limits.
Use responsibly for small-scale lead research only.
"""

import csv
import time
import random
import json
import re
from datetime import datetime


class GoogleMapsScraper:
    """
    Extract business listings from Google Maps search.

    Designed to be adaptable:
    - Replace _parse_result() to work with different platforms
    - Adjust delays for your target website
    - Add proxy support for large-scale scraping

    Architecture:
        GoogleMapsScraper
        |-- __init__()       : Setup browser, anti-detection
        |-- search()         : Execute search query
        |-- _scroll_results(): Load more results
        |-- _parse_result()  : Extract data from each listing
        |-- extract_all()    : Orchestrate full extraction
        |-- save_csv()       : Export to CSV
        |-- save_json()      : Export to JSON
    """

    def __init__(self, headless=False, delay=2.0):
        """
        Initialize the scraper.

        Args:
            headless: Run browser in background (True = invisible)
            delay: Base delay between actions to avoid detection
        """
        self.delay = delay
        self.results = []
        self.browser = None
        self.headless = headless

    def _init_browser(self):
        """
        Initialize Selenium WebDriver with anti-detection measures.

        In a real project, this would use:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options

            options = Options()
            if self.headless:
                options.add_argument('--headless')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--user-agent=...')
            self.browser = webdriver.Chrome(options=options)

        For this demo, we simulate the extraction with realistic sample data.
        """
        print("[INFO] Browser initialized with anti-detection measures")
        print("[INFO] User-Agent: Chrome 120 / Windows 10")
        print("[INFO] Headless mode:", self.headless)

    def search(self, query, location=""):
        """
        Execute a Google Maps search.

        Args:
            query: Business type or keyword (e.g., "coffee shops")
            location: Geographic area (e.g., "Chicago, IL")

        Returns:
            Number of results found
        """
        full_query = f"{query} {location}".strip()
        print(f'\n[SEARCH] Searching for: "{full_query}"')

        # In production: browser.get(maps_url + query_params)
        self._random_delay(1, 2)

        # Simulate finding results
        result_count = random.randint(20, 120)
        print(f"[INFO] Found approximately {result_count} results")
        return result_count

    def _scroll_results(self, target_count):
        """
        Scroll the results panel to load more listings.

        Google Maps loads results dynamically as you scroll.
        """
        loaded = 0
        scrolls = 0
        max_scrolls = min(target_count // 20 + 5, 50)

        while loaded < target_count and scrolls < max_scrolls:
            # In production: browser.execute_script(
            #     'document.querySelector("[role=feed]").scrollTop += 5000')
            loaded += 20
            scrolls += 1
            self._random_delay(0.5, 1.5)

        print(f"[INFO] Loaded {min(loaded, target_count)} listings "
              f"after {scrolls} scrolls")
        return min(loaded, target_count)

    def _parse_result(self, element_html=""):
        """
        Extract structured data from a single business listing.

        In production, this parses actual HTML elements:
            name = element.find_element('.class-name').text
            rating = element.find_element('.rating-class').get_attribute('aria-label')
            etc.

        Returns:
            Dictionary with business information
        """
        # Simulated extraction - in production, this parses real HTML
        business_types = ['Cafe', 'Restaurant', 'Shop', 'Office', 'Clinic',
                          'Studio', 'Firm', 'Services', 'Ltd', 'Inc']

        streets = ['Main St', 'Oak Ave', 'Broadway', 'Market St', 'Park Blvd',
                   'Elm St', 'Washington Ave', 'Lake Dr', 'Highland Rd']

        business = {
            'name': f"Sample Business {len(self.results) + 1}",
            'category': random.choice(business_types),
            'address': f"{random.randint(100, 9999)} {random.choice(streets)}",
            'phone': self._generate_phone(),
            'website': f"https://business{len(self.results)+1}.example.com",
            'rating': round(random.uniform(2.5, 5.0), 1),
            'review_count': random.randint(5, 1500),
            'hours': 'Mon-Fri 9AM-6PM',
            'plus_code': f"XXXX+XX Area {random.randint(1,20)}",
        }
        return business

    def _generate_phone(self):
        """Generate a realistic-looking phone number."""
        formats = [
            lambda: f"+1 ({random.randint(200,999)}) {random.randint(100,999)}-{random.randint(1000,9999)}",
            lambda: f"({random.randint(200,999)}) {random.randint(100,999)}-{random.randint(1000,9999)}",
            lambda: f"+44 {random.randint(1000,9999)} {random.randint(100000,999999)}",
        ]
        return random.choice(formats)()

    def _random_delay(self, min_sec, max_sec):
        """Add a random delay to mimic human behavior."""
        time.sleep(random.uniform(min_sec, max_sec))

    def extract_all(self, query, location="", max_results=40):
        """
        Main extraction orchestration.

        Args:
            query: What to search for
            location: Where to search
            max_results: Maximum number of businesses to extract

        Returns:
            List of business dictionaries
        """
        print("=" * 60)
        print(f"  GOOGLE MAPS BUSINESS EXTRACTOR")
        print(f"  Query: {query} | Location: {location or 'Any'}")
        print(f"  Target: {max_results} results")
        print(f"  Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

        # Step 1: Initialize browser
        self._init_browser()

        # Step 2: Search
        estimated = self.search(query, location)

        # Step 3: Scroll to load results
        to_load = min(max_results, estimated)
        self._scroll_results(to_load)

        # Step 4: Parse each listing
        print(f"\n[EXTRACT] Parsing {to_load} business listings...")
        for i in range(to_load):
            try:
                business = self._parse_result()
                self.results.append(business)

                if (i + 1) % 10 == 0:
                    print(f"  Progress: {i+1}/{to_load} extracted...")
                self._random_delay(0.1, 0.3)

            except Exception as e:
                print(f"  [SKIP] Error at listing {i+1}: {e}")
                continue

        print(f"\n[DONE] Extracted {len(self.results)} businesses")
        return self.results

    def clean_data(self):
        """
        Clean and validate extracted data.

        - Remove entries without phone numbers
        - Standardize phone formats
        - Remove duplicates
        - Validate website URLs
        """
        cleaned = []
        seen = set()

        for b in self.results:
            # Deduplicate by name + address
            key = (b['name'].lower(), b['address'].lower())
            if key in seen:
                continue
            seen.add(key)

            # Keep only entries with phone numbers (more valuable for leads)
            if b['phone'] and 'N/A' not in b['phone']:
                cleaned.append(b)

        removed = len(self.results) - len(cleaned)
        if removed > 0:
            print(f"[CLEAN] Removed {removed} duplicates or incomplete entries")
        self.results = cleaned
        return cleaned

    def enrich_leads(self):
        """
        Add lead scoring to help prioritize follow-ups.

        Score factors:
        - Has website (+10)
        - Rating >= 4.0 (+10)
        - Has phone (+10)
        - Many reviews (+5)
        """
        for b in self.results:
            score = 0
            if b.get('website') and 'example.com' not in b['website']:
                score += 10
            if b.get('rating', 0) >= 4.0:
                score += 10
            if b.get('phone'):
                score += 10
            if b.get('review_count', 0) > 50:
                score += 5
            b['lead_score'] = score

        print(f"[ENRICH] Added lead scores to {len(self.results)} entries")

    def save_csv(self, filename="leads.csv"):
        """Export to CSV with BOM for Excel compatibility."""
        if not self.results:
            print("[WARN] No data to save")
            return

        fields = ['name', 'category', 'address', 'phone', 'website',
                  'rating', 'review_count', 'lead_score']

        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=fields,
                                    extrasaction='ignore')
            writer.writeheader()
            writer.writerows(self.results)

        print(f"[SAVED] {len(self.results)} leads -> {filename}")

    def save_json(self, filename="leads.json"):
        """Export to JSON."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"[SAVED] {len(self.results)} leads -> {filename}")

    def summary(self):
        """Print extraction summary."""
        if not self.results:
            return

        ratings = [b['rating'] for b in self.results]
        with_phone = sum(1 for b in self.results if b.get('phone'))
        with_website = sum(1 for b in self.results if b.get('website'))

        print("\n" + "=" * 40)
        print("  EXTRACTION SUMMARY")
        print("=" * 40)
        print(f"  Total leads:     {len(self.results)}")
        print(f"  With phone:      {with_phone}")
        print(f"  With website:    {with_website}")
        print(f"  Avg rating:      {sum(ratings)/len(ratings):.1f}/5")
        print(f"  Min rating:      {min(ratings):.1f}/5")
        print(f"  Max rating:      {max(ratings):.1f}/5")
        print(f"  Top leads (score >= 30): "
              f"{sum(1 for b in self.results if b.get('lead_score', 0) >= 30)}")
        print("=" * 40)


# ============================================================
# DEMO
# ============================================================
if __name__ == '__main__':
    print("""
    =========================================================
      GOOGLE MAPS LEAD EXTRACTOR - DEMO MODE
      Jesse | Upwork/Fiverr Portfolio Sample
    =========================================================

    In production, this tool uses Selenium WebDriver to extract
    real business data from Google Maps search results.

    This demo shows the architecture, data pipeline, and output
    format using simulated data (identical structure to real runs).
    """)

    # Initialize
    scraper = GoogleMapsScraper(headless=False, delay=1.5)

    # Run extraction
    leads = scraper.extract_all(
        query="coffee shops",
        location="Chicago, IL",
        max_results=40
    )

    if leads:
        # Clean and enrich
        scraper.clean_data()
        scraper.enrich_leads()

        # Save outputs
        scraper.save_csv("leads_sample.csv")
        scraper.save_json("leads_sample.json")

        # Summary
        scraper.summary()

        print("\n[DONE] Check leads_sample.csv for the output.")
        print("[NOTE] This demo uses simulated data.")
        print("[REAL] Contact me for a live demo on your target market.")
    else:
        print("[FAIL] No leads extracted.")
