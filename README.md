Implementation of negative markers to allow excluding markers from tests that their class has set

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
test_class.py::TestClass_1::test_1_3
test_class.py::TestClass_2::test_2_1
test_class.py::TestClass_2::test_2_2
test_class.py::TestClass_2::test_2_3
```

Select all tests that don't have neither `some_mark` nor `some_mark2`
```
$ python -m pytest -q --collect-only -m "not some_mark and not some_mark2"
test_class.py::TestClass_1::test_1_3
test_class.py::TestClass_2::test_2_2
test_class.py::TestClass_2::test_2_3
```
