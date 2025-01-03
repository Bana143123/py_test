import pytest
from calculator import add

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_sample(sample_data):
    assert sample_data["key"] == "value"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),     
        (0, 0, 0),       
        (-1, -1, -2),    
        (100, 200, 300), 
        (3.5, 2.5, 6.0)  
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected

