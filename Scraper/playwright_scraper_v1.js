const { chromium } = require('playwright');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;


(async() => {
    const browser = await chromium.launch({ headless: false }); // Set headless to false for a visible browser window
    const page = await browser.newPage();

    const mobileEmulation = {
        deviceMetrics: { width: 428, height: 926, pixelRatio: 3.0 },
        userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1',
    };

    await page.setViewportSize({ width: 428, height: 926 }); // Set the viewport size

    // Navigate to the URL
    const url = 'https://www.daraz.com.np/products/mamaearth-ubtan-face-wash-100-ml-i100764018-s1021228047.html?spm=a2a0e.searchlist.list.7.30f064c6atZEG1&search=1';
    await page.goto(url);

    // Scroll down gradually
    for (let i = 0; i < 20; i++) {
        console.log('Scrolling...');
        await page.evaluate(() => {
            window.scrollBy(0, 100);
        });
        await page.waitForTimeout(100);
    }

    // Product Info
    const productTitle = await page.textContent('.pdp-mod-product-title');
    const productPrice = await page.textContent('.pdp-price');
    const originalPrice = await page.textContent('.price-discount');
    const discountPercent = await page.textContent('.price-decrease');
    const totalSales = await page.textContent('.product-info-sold');
    const cartAdded = await page.textContent('#fomo-banner > div > div > div > div > div:nth-child(3) > div > span.normal-text');
    const wishlistAdded = await page.textContent('.pdp-mod-wishlist');

    // Create a CSV writer
    const csvWriter = createCsvWriter({
        path: 'productdetails.csv',
        header: [
            { id: 'Product Name', title: 'Product Name' },
            { id: 'Product Price', title: 'Product Price' },
            { id: 'Original Price', title: 'Original Price' },
            { id: 'Discount %', title: 'Discount %' },
            { id: 'Total Sales', title: 'Total Sales' },
            { id: 'Cart Added', title: 'Cart Added' },
            { id: 'Wishlist Added', title: 'Wishlist Added' },
        ],
    });

    const records = [{
        'Product Name': productTitle,
        'Product Price': productPrice,
        'Original Price': originalPrice,
        'Discount %': discountPercent,
        'Total Sales': totalSales,
        'Cart Added': cartAdded,
        'Wishlist Added': wishlistAdded,
    }, ];

    // Write the data to the CSV file
    await csvWriter.writeRecords(records);

    // Close the browser
    await browser.close();
})();