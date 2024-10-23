from hexlet_pytest.example import reverse


def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_with_fixtures():
    origin_text_path = 'tests/fixtures/origin.txt'
    reversed_text_path = 'tests/fixtures/reversed.txt'

    with open(origin_text_path, encoding='utf8') as f_o,  \
         open(reversed_text_path, encoding='utf8') as f_r:

        origin_text = f_o.read()
        fixture_text = f_r.read()
        reversed_text = reverse(origin_text)
        assert reversed_text == fixture_text
