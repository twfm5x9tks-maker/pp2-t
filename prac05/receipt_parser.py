import re
import json

with open(r"C:\Users\serik\pp2-t\prac05\raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

date_time_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}", text)
date_time = date_time_match.group() if date_time_match else None

payment_match = re.search(r"Банковская карта|Наличные|Kaspi|CARD|CASH", text, re.IGNORECASE)
payment_method = payment_match.group() if payment_match else None

total_match = re.search(r"ИТОГО:\s*\n?([\d\s]+,\d{2})", text)
total_amount = None
if total_match:
    total_amount = total_match.group(1).replace(" ", "")
    total_amount = float(total_amount.replace(",", "."))

product_pattern = r"\d+\.\s*\n(.+?)\n\d+,\d{3}\s*x\s*[\d\s]+,\d{2}"
products = re.findall(product_pattern, text, re.MULTILINE)

price_pattern = r"\n([\d\s]+,\d{2})\nСтоимость"
prices_raw = re.findall(price_pattern, text)

prices = []
for p in prices_raw:
    clean = p.replace(" ", "").replace(",", ".")
    prices.append(float(clean))

items = []

for i in range(min(len(products), len(prices))):
    items.append({
        "product": products[i].strip(),
        "price": prices[i]
    })

data = {
    "company": "EUROPHARMA",
    "city": "Нур-Султан",
    "date_time": date_time,
    "payment_method": payment_method,
    "total_amount": total_amount,
    "items": items
}

print(json.dumps(data, indent=4, ensure_ascii=False))