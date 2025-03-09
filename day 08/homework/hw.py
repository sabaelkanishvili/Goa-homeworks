
# თავდაპირველი ფასები წიგნებისთვის 

book1_original_price = 55.0
book2_original_price = 25.0
book3_original_price = 85.0
book4_original_price = 90.0
book5_original_price = 40.0

# ფასდაკლების ოდენობა (30%) 

discount_percentage = 30.0

# ფასდაკლების თანხა 

discount_amount = discount_percentage / 100.0

# ახალი ფასები წიგნებისთვის
book1_new_price = book1_original_price = (book1_original_price * discount_amount)
book2_new_price = book2_original_price = (book2_original_price * discount_amount)
book3_new_price = book3_original_price = (book3_original_price * discount_amount)
book4_new_price = book4_original_price = (book4_original_price * discount_amount)
book5_new_price = book5_original_price = (book5_original_price * discount_amount)

# ახალი ფასების დაბეჭდვა
print("წიგნი 1-ის ახალი ფასი:", book1_new_price)
print("წიგნი 2-ის ახალი ფასი:", book2_new_price)
print("წიგნი 3-ის ახალი ფასი:", book3_new_price)
print("წიგნი 4-ის ახალი ფასი:", book4_new_price)
print("წიგნი 5-ის ახალი ფასი:", book5_new_price) 