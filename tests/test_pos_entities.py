import malaya

def test_pos_entities_char():
    available_models = malaya.get_available_pos_entities_models()
    string = 'KUALA LUMPUR: Sempena sambutan Aidilfitri minggu depan'
    assert len(malaya.deep_pos_entities('char').predict(string)) > 0

def test_pos_entities_concat():
    available_models = malaya.get_available_pos_entities_models()
    string = 'KUALA LUMPUR: Sempena sambutan Aidilfitri minggu depan'
    assert len(malaya.deep_pos_entities('concat').predict(string)) > 0

def test_pos_entities_attention():
    available_models = malaya.get_available_pos_entities_models()
    string = 'KUALA LUMPUR: Sempena sambutan Aidilfitri minggu depan'
    assert len(malaya.deep_pos_entities('attention').predict(string)) > 0
