# -----------------------------------------------------------------------
# Description: This file contains the tests for the REST API
# -----------------------------------------------------------------------

import pytest
import requests

# -----------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------

# @pytest.mark.duckduckgo
# @pytest.mark.rest_api
def test_duckdcukgo_isntant_answer_api():
    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'
    
    # Act
    response = requests.get(url)
    body = response.json()
    
    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']
