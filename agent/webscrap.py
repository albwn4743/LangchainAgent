from playwright.async_api import async_playwright
import asyncio

async def search_and_scrape(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=r"C:\Users\albin.joy\AppData\Local\Google\Chrome\User Data\playwright",
            channel="chrome",
            headless=False
        )
        page = await browser.new_page()
        print("Opening Google...")
        await page.goto(
            "https://www.google.com",
            wait_until="domcontentloaded"
        )
        await page.fill(
            'textarea[name="q"]',
            query
        )

        await page.keyboard.press("Enter")
        await page.wait_for_url("**/search?*")

        await page.locator("h3").first.wait_for(timeout=15000)

        print("\nSearch Page:")
        print(await page.title())
        print(page.url)

        results = page.locator("h3")
        count = await results.count()
        print(f"\nFound {count} results\n")
        result_urls = []
        for i in range(min(count, 5)):
            try:
                # title = await results.nth(i).inner_text()
                anchor = results.nth(i).locator(
                    "xpath=ancestor::a[1]"
                )
                url = await anchor.get_attribute("href")
                # print(f"{i+1}. {title}")
                # print(url)
                # print("-" * 60)

                if url and url.startswith("http"):
                    result_urls.append(url)

            except Exception as e:
                print("Error:", e)

        if not result_urls:
            print("No search result URLs found")
            return

        target_url = result_urls[0]

        print("\nOpening:")
        print(target_url)

        await page.goto(
            target_url,
            wait_until="domcontentloaded"
        )

        await page.wait_for_timeout(3000)
        text = await page.locator(
            "body"
        ).inner_text()

        print("\nExtracted Content:\n")

        print(text[:3000])

        await browser.close()


q=input("Enter the question:")
asyncio.run(
    search_and_scrape(q)
)