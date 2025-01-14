from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Buka TikTok
driver.get("https://www.tiktok.com")

# Tunggu beberapa saat agar halaman selesai dimuat
driver.implicitly_wait(10)

# Ambil semua cookies
cookies = driver.get_cookies()

# Temukan cookie yang spesifik, misalnya tt_chain_token
for cookie in cookies:
    if cookie['name'] == 'tt_chain_token':
        print(f"tt_chain_token: {cookie['value']}")

# Tutup WebDriver
driver.quit()
