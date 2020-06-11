class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_quality_backstage_pass(item)
            elif item.name == "Aged Brie":
                self.update_quality_aged_brie(item)
            else:
                self.update_quality_standard_item(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                self.decrease_selling_date(item)

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def update_quality_standard_item(self, standard_item):
        if standard_item.quality > 0:
            if standard_item.name != "Sulfuras, Hand of Ragnaros":
                standard_item.quality = standard_item.quality - 1

    def update_quality_backstage_pass(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def update_quality_aged_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrease_selling_date(self, item):
        item.sell_in = item.sell_in - 1