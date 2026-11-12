import os
import sys
from collections import Counter
from itertools import chain, combinations

import requests

FILE_NAME = "orders.txt"
DOCUMENT_URL = "https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF"
MIN_SUPPORT = 15
MIN_CONFIDENCE = 45


def download_document(file_name, document_url):
    if os.path.exists(file_name):
        return
    response = requests.get(document_url, timeout=60)
    if response.status_code != 200:
        sys.exit(f"Failed to download the document. Status code: {response.status_code}")
    if response.content.lstrip().lower().startswith(b"<!doctype html"):
        sys.exit(f"Google Drive повернув HTML замість файлу. Збережіть файл вручну як '{file_name}'.")
    with open(file_name, "wb") as f:
        f.write(response.content)


def parse_orders(text):
    orders = []
    for block in text.split("\n\n"):
        block = block.strip()
        if block:
            orders.append([p.strip() for p in block.split("@@@")])
    return orders


def read_orders(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return parse_orders(f.read())


def count_products(orders):
    return Counter(chain.from_iterable(set(order) for order in orders))


def count_product_pairs(orders):
    pair_count = Counter()
    for order in orders:
        pair_count.update(combinations(sorted(set(order)), 2))
    return pair_count


def find_association_rules(products, product_pairs, min_confidence, min_support):
    printed = 0
    for (x, y), support in sorted(product_pairs.items()):
        if support < min_support:
            continue
        conf_x_to_y = support / products[x] * 100
        conf_y_to_x = support / products[y] * 100
        if conf_x_to_y >= min_confidence:
            print(f"p1 {x} => {y} ({conf_x_to_y:.2f}% confidence), {support} support")
            printed += 1
        if conf_y_to_x >= min_confidence:
            print(f"p2 {y} => {x} ({conf_y_to_x:.2f}% confidence), {support} support")
            printed += 1
    return printed


def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else FILE_NAME
    min_support = int(sys.argv[2]) if len(sys.argv) > 2 else MIN_SUPPORT
    min_confidence = float(sys.argv[3]) if len(sys.argv) > 3 else MIN_CONFIDENCE

    if file_name == FILE_NAME:
        download_document(FILE_NAME, DOCUMENT_URL)

    orders = read_orders(file_name)
    print(f"Довжина списку = {len(orders)}")

    products = count_products(orders)
    print(f"Кількість унікальних товарів = {len(products)}")

    product_pairs = count_product_pairs(orders)
    print(f"Знайдено {len(product_pairs)} пар товарів із {len(orders)} замовлень")

    total = find_association_rules(products, product_pairs, min_confidence, min_support)
    print(f"\nУсього правил: {total}")


if __name__ == "__main__":
    main()