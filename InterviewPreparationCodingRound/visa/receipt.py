def recipt(items):
    width=30
    print('-'*width)
    print("Receipt".center(width))
    print('-' * width)
    for item in items:
        description,price=item
        print(f"{description.ljust(width)}" (str(price)))
    print('-'*width)

items=[["apple","$50"],["banana","$20"]]
recipt(items)
