# gilded_rose.py

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class DefaultUpdater:
    def update(self, item):
        item.sell_in -= 1
        degradation = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - degradation)


class AgedBrieUpdater:
    def update(self, item):
        item.sell_in -= 1
        increase = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + increase)


class SulfurasUpdater:
    def update(self, item):
        pass  # legendary — never changes


class BackstagePassUpdater:
    def _increase_for(self, sell_in):
        if sell_in < 0:
            return None
        if sell_in < 5:
            return 3
        if sell_in < 10:
            return 2
        return 1

    def update(self, item):
        item.sell_in -= 1
        inc = self._increase_for(item.sell_in)
        if inc is None:
            item.quality = 0
        else:
            item.quality = min(50, item.quality + inc)


class ConjuredUpdater:
    def update(self, item):
        item.sell_in -= 1
        degradation = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degradation)


UPDATER_REGISTRY = {
    "Aged Brie": AgedBrieUpdater(),
    "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
    "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater(),
    "Conjured Mana Cake": ConjuredUpdater(),
}


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = UPDATER_REGISTRY.get(item.name, DefaultUpdater())
            updater.update(item)
