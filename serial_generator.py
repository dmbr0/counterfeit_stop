#!/usr/bin/env python
import strgen 
batch_num = input("Please enter a batch ID:")
serialqty = input("How many serial numbers would you like to create?:")
print("Batch:", batch_num)
print(strgen.StringGenerator("[\d\w]{7}").render_list(serialqty,unique=True))
