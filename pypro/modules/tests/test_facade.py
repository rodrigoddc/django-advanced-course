from pypro.modules.facades import facade_module


def test_modules_sorted_by_order(modules):
    assert list(sorted(modules, key=lambda module: module.order)) == facade_module.modules_sorted_by_order()
