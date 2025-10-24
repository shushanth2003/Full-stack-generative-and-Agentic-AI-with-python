menu=[
    "chicken puff",
    "chicken masala",
    "chicken puff",
    "chicken masala"
];
remove_duplicate_menu={menu_card for menu_card in menu};
print(f"Removed Duplicate Elements : {remove_duplicate_menu}");

menus={
    "tea":["sugar","milk","water"],
    "milkshake":["sugar","milk","ice","favour"]
}
unique_menu={spices for integredients in menus.values() for spices in integredients};
print(f"Unique set menu fits and fields {unique_menu}");