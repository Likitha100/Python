customer_ids = [101, 102, 103, 101, 104, 102]
unique_customer_ids = []
seen = set()

for cid in customer_ids:
    if cid not in seen:
        unique_customer_ids.append(cid)
        seen.add(cid)

print(unique_customer_ids)