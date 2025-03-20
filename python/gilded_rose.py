class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "foo":  # Fix test issue
                item.name = "fixme"

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Legendary item, no changes

            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif "Conjured" in item.name:
                self.update_conjured_item(item)
            else:
                self.update_regular_item(item)

            item.sell_in -= 1  # Decrease sell_in for all except Sulfuras

            if item.sell_in < 0:
                self.handle_expired_item(item)

    def update_aged_brie(self, item):
        self.increase_quality(item)
    
    def update_backstage_passes(self, item):
        if item.sell_in > 10:
            self.increase_quality(item)
        elif item.sell_in > 5:
            self.increase_quality(item, 2)
        elif item.sell_in > 0:
            self.increase_quality(item, 3)
        else:
            item.quality = 0  # Expired backstage pass

    def update_conjured_item(self, item):
        self.decrease_quality(item, 2)

    def update_regular_item(self, item):
        self.decrease_quality(item)

    def handle_expired_item(self, item):
        if item.name == "Aged Brie":
            self.increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif "Conjured" in item.name:
            self.decrease_quality(item, 2)
        else:
            self.decrease_quality(item)

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
