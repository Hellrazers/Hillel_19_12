label_in_recomend_view_under_image = r"""//*[text() = 'Рекомендації на основі ваших переглядів']/parent::div/following-sibling::rz-scroller//rz-product-tile/child::*/a[@class="black-green-link text-base"]"""
# info XPATH
label_in_recomend_view_under_image_with_free_delivery = r'''//*[text() = 'Рекомендації на основі ваших переглядів']/parent::div/following-sibling::rz-scroller//rz-tile-premium/parent::*/a[@class="black-green-link text-base"]'''
fix_xpath = r'''//div/following-sibling::rz-scroller//rz-tile-premium/parent::*/a[@class="black-green-link text-base"]'''