HOST = 'https://exist.ua/api/v1/catalogue/get-necessary/?selected_car=false'

internal_api_methods = {
    """
        name:(method, param, status_code)
    """
    'create': ('POST', '', '204'),
    'bulk_create': ('POST', 'bulk-create/', '204'),
    'delete': ('DELETE', 'id', '200'),
    'bulk_destroy': ('POST', 'bulk-destroy/', '200'),
    'update': ('PUT', 'id/', '201'),
    'bulk_update': ('PUT', 'bulk-update/', '201'),
    'get': ('GET', '', '200')
}
