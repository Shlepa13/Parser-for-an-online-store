# online store - https://www.everbrightinc.com/

for category in ['67_68','67_74','67_73','67_72','67_70','67_69','67_71', # - WOMEN
                 '75_79','75_77','75_78','75_76',                         # - MEN
                 '84_85','84_86',                                         # - GIRL
                 '80_81','80_83','80_82',                                 # - BOY
                 '91_92',                                                 # - BABY not available
                 '93',                                                    # - SALES
                 '95',                                                    # - HOLIDAYS
                 '103']:                                                  # - NEW
    for page in range(1, 8):
        url = f'https://www.everbrightinc.com/index.php?route=product/category&path={category}&page={page}'