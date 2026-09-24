import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_swap_by_newest():
    item_a = Clothing(condition=2.0, age=5)
    item_b = Decor(condition=2.0, age=3)
    item_c = Clothing(condition=4.0, age=1)
    item_d = Decor(condition=5.0, age=2)
    item_e = Clothing(condition=3.0, age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    item_f = Clothing(condition=2.0, age=6)
    item_g = Decor(condition=2.0, age=7)
    item_h = Clothing(condition=4.0, age=8)
    item_i = Decor(condition=5.0, age=9)
    item_j = Clothing(condition=3.0, age=10)
    jesse = Vendor(
        inventory=[item_f, item_g, item_h, item_i, item_j]
    )

    result = tai.swap_by_newest(jesse)

    assert result is True
    assert len(tai.inventory) == 5
    assert len(jesse.inventory) == 5
    assert item_c in jesse.inventory
    assert item_f in tai.inventory
    