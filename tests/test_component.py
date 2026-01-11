from app.features import hash_feature
from app.model import predict

def test_feature_to_model_flow():
    feature = hash_feature("test")
    result = predict(feature)
    assert result >= 0
