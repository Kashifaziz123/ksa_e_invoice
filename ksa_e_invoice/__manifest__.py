{
    "name": "KSA E-invoice",
    "version": "15.0.0.0.0",
    "category": "",
    'summary': "KSA E-invoicing for point of sale and invoicing for b2c and b2b",
    'description': "KSA E-invoicing for point of sale and invoicing for b2c and b2b",
    "author": "Alhaditech",
    "website": "",
    'license': '',
    'price': 30, 'currency': 'USD',
    'images': ['static/description/background.jpeg'],
    "depends": [
        'base', 'point_of_sale',
    ],
    "data": [
        'views/assets.xml',
        ],
    'qweb': ['static/src/xml/pos.xml'],
    "installable": True,
}
