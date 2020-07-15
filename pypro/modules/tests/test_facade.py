from pypro.modules import facade


def test_modules_sorted_by_order(modules):
    assert list(sorted(modules, key=lambda module: module.order)) == facade.modules_sorted_by_order()
