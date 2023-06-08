import pytest


def test_noun_chunks_is_parsed_bal(bal_tokenizer):
    """Test that noun_chunks raises Value Error for 'bal' language if Doc is not parsed."""

    doc = bal_tokenizer("این یک جمله نمونه می باشد.")
    with pytest.raises(ValueError):
        list(doc.noun_chunks)
