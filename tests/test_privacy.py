from src.privacy import is_private_path, redact


def test_redacts_api_key():
    value = redact('api_key=super-secret-value')
    assert 'super-secret-value' not in value
    assert '[REDACTED]' in value


def test_redacts_bearer_token():
    value = redact('Authorization: Bearer abc.def.ghi')
    assert 'abc.def.ghi' not in value


def test_private_paths():
    assert is_private_path('.env')
    assert is_private_path('/home/user/.ssh/config')
    assert is_private_path('/repo/.aws/credentials')
