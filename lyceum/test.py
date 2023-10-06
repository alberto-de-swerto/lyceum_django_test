expected_response = {
    'products': {
        'title': 'tea',
        'count': 3
    }
}


def test_available_tea_response_dict(response):
    assert isinstance(response, dict)


def test_available_tea_product_in_response(response):
    assert 'product' in response, f'fields in response {list(response.keys())}'

# assert len(response) == 1
# assert isinstance(response['products'], list)
# products = response['products']
# assert len(products)
# product = products[0]
# assert isinstance(product, dict)
# assert product['title'] == 'tea'
# assert product['count'] == 3
# assert len(product) == 2
