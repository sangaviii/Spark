{
    'name': "spark_bikers",
    'author': "sangavikumar",
    'version': '0.1',
    'depends': ['base','purchase', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/bike_views.xml',
        'views/customer_views.xml',
        'views/employer_views.xml' ,
        'views/purchase_views.xml',
        'views/manager_views.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}