import pytest
import datetime
from datetime import date
from typing import Generator
from unittest.mock import MagicMock, patch


from app.main import outdated_products


@pytest.fixture
def mock_date_today() -> Generator[MagicMock, None, None]:
    with patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date(2022, 2, 2)
        yield mock_date


def test_groceries_with_date(mock_date_today: MagicMock) -> None:
    mock_date_today.return_value = date(2022, 2, 2)
    result = outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ])
    assert result == ["duck"]
