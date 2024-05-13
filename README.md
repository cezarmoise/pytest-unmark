Implementation of negative markers to allow excluding markers from tests that their class has set

Only work for positive selections of markers, e.g. `-m marker` but not `-m "not marker"`


List of tests
- `test_class.py::TestClass_1` marked with `some_mark`
   - `test_class.py::TestClass_1::test_1_2`
   - `test_class.py::TestClass_1::test_1_2`
   - `test_class.py::TestClass_1::test_1_3` marked with `not_some_mark`
- `test_class.py::TestClass_2` marked with `some_mark2`
   - `test_class.py::TestClass_2::test_2_1`
   - `test_class.py::TestClass_2::test_2_2` marked with `not_some_mark2`
   - `test_class.py::TestClass_2::test_2_3` marked with `not_some_mark2`


Select all the tests
```
$ python -m pytest -q --collect-only              
test_class.py::TestClass_1::test_1_1
test_class.py::TestClass_1::test_1_2
test_class.py::TestClass_1::test_1_3
test_class.py::TestClass_2::test_2_1
test_class.py::TestClass_2::test_2_2
test_class.py::TestClass_2::test_2_3
```

Select only tests with `some_mark`
```
$ python -m pytest -q --collect-only -m some_mark 
test_class.py::TestClass_1::test_1_1
test_class.py::TestClass_1::test_1_2
```

Select only tests with `some_mark2`
```
$ python -m pytest -q --collect-only -m some_mark2
test_class.py::TestClass_2::test_2_1
```

Select tests with either `some_mark` or `some_mark2`
```
$ python -m pytest -q --collect-only -m "some_mark or some_mark2"
test_class.py::TestClass_1::test_1_1
test_class.py::TestClass_1::test_1_2
test_class.py::TestClass_2::test_2_1
```

Select all tests that don't have `some_mark`
```
$ python -m pytest -q --collect-only -m "not some_mark"
test_class.py::TestClass_2::test_2_1
test_class.py::TestClass_2::test_2_2
test_class.py::TestClass_2::test_2_3
```

Notice that `test_class.py::TestClass_1::test_1_3` is not selected. This is becase our `pytest_collection_modifyitems` hook does not replace the original hook, it only runs before it. Our hook adds that test to the items list, but becase the parent `TestClass_1` has that marker, when the original hook runs, it will deselect it. The `item.iter_markers()` function return not just the current item's markers, but also those of the parent. A complete implementation would need to rewrite all the markers so that the markers of the parents are moved to the items themselves.