marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
# Return True if two sets have a null intersection.
print(marcas_tv.isdisjoint(marcas_smartphones))