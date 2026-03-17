import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_degrades_quality(self):
        items = [Item("foo", sell_in=10, quality=20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("foo", sell_in=0, quality=0)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", sell_in=5, quality=10)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(11, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_backstage_pass_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", sell_in=5, quality=10)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual(8, items[0].quality)

if __name__ == '__main__':
    unittest.main()
