from app.features import hash_feature
from app.model import predict


def test_hash_feature_within_bucket_range():
    result = hash_feature("test", num_buckets=10)
    assert 0 <= result < 10


def test_hash_feature_deterministic():
    value = "consistent_test"
    assert hash_feature(value) == hash_feature(value)


def test_hash_feature_custom_buckets():
    assert 0 <= hash_feature("test", num_buckets=5) < 5
    assert 0 <= hash_feature("test", num_buckets=1000) < 1000


def test_predict_calculation():
    assert predict(50) == 5.0


def test_predict_with_positive_values():
    assert predict(1) == 0.1
    assert predict(10) == 1.0
    assert predict(100) == 10.0
