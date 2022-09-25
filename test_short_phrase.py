class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase (shorter than 15 characters):")
        assert len(phrase) < 15
