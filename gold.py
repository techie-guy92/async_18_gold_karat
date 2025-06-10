import requests
import requests_cache
from bs4 import BeautifulSoup
import aiohttp
import asyncio


# ============================================ Func 1 =====================================================

# Enable caching to avoid redundant requests (cached for 5 minutes)
requests_cache.install_cache("tgju_cache", expire_after=300)  

def calculate_18k_gold_price_toman_1():
    tgju = requests.get("https://www.tgju.org/")
    assert tgju.status_code == 200, "Failed to fetch data. Check the website or your connection."
    soup = BeautifulSoup(tgju.content, "html.parser")
    ounce = soup.select_one("#l-ons .info-price")  
    dollar = soup.select_one("#l-price_dollar_rl .info-price")
    
    if not ounce or not dollar:
        raise ValueError("Failed to fetch required data from tgju.org.")

    ounce_price = ounce.text.strip().replace(",", "")
    dollar_rate = dollar.text.strip().replace(",", "")

    if ounce_price.replace(".", "").isdigit() and dollar_rate.replace(".", "").isdigit():
        ounce_price = float(ounce_price)
        dollar_rate = float(dollar_rate)
    else:
        raise ValueError("Invalid data format. Ensure that the extracted prices are numerical.")
    
    karat_24_price_per_gram = ounce_price / 31.1
    karat_18_price_per_gram = karat_24_price_per_gram * (18 / 24)
    karat_18_gold_toman_price = karat_18_price_per_gram * dollar_rate
    price = f"{karat_18_gold_toman_price:,.0f}"
    
    return f"Price of 18 karat gold is: IRT {price}"

func_1 = calculate_18k_gold_price_toman_1()


# ============================================ Func 2 =====================================================

async def calculate_18k_gold_price_toman_2():
    async with aiohttp.ClientSession() as session:
        async def get_price(url):
            async with session.get(url) as response:
                return await response.text()
        
        tgju_content = await get_price("https://www.tgju.org/")
        soup = BeautifulSoup(tgju_content, "html.parser")
        ounce = soup.select_one("#l-ons .info-price")
        dollar = soup.select_one("#l-price_dollar_rl .info-price")
        
        if not ounce or not dollar:
            raise ValueError("Failed to fetch required data from tgju.")
        
        ounce_price = ounce.text.strip().replace(",", "")
        dollar_rate = dollar.text.strip().replace(",", "")
        
        if ounce_price.replace(".", "").isdigit() and dollar_rate.replace(".", "").isdigit():
            ounce_price = float(ounce_price)
            dollar_rate = float(dollar_rate)
        else:
            raise ValueError("Invalid data format, the extracted prices are not numerical.")
        
        karat_24_price_per_gram = ounce_price / 31.1
        karat_18_price_per_gram = karat_24_price_per_gram * (18 / 24)
        karat_18_gold_toman_price = karat_18_price_per_gram * dollar_rate
        price = f"{karat_18_gold_toman_price:,.0f}"
        
        return f"Price of 18 karat gold is: IRT {price}"

async def main():
    func_2 = await calculate_18k_gold_price_toman_2()
    print(func_2)


# ============================================ Executor ===================================================

# print(func_1)
asyncio.run(main())


# =========================================================================================================
