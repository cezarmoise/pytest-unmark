import pytest

@pytest.mark.some_mark
class TestClass_1:
    def test_1_1(self):
        pass

    def test_1_2(self):
        pass

    @pytest.mark.not_some_mark
    def test_1_3(self):
        pass

@pytest.mark.some_mark2
class TestClass_2:
    def test_2_1(self):
        pass

    @pytest.mark.not_some_mark2
    def test_2_2(self):
        pass

    @pytest.mark.not_some_mark2
    def test_2_3(self):
        pass
