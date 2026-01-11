from app.features import hash_feature

def test_hash_feature_consistency():
    value = "mlops"
    bucket1 = hash_feature(value, 10)
    bucket2 = hash_feature(value, 10)
    assert bucket1 == bucket2
