def get_login_mac_mik(ip, user, paswrd, port):
    log_mac_olt = np.array([['', '', '']])
    connection = routeros_api.RouterOsApiPool(ip, username=user, password=paswrd, port=port,
                                              plaintext_login=True)
    api = connection.get_api()
    tt = api.get_resource('/ppp/active')
    r = tt.get()
    return r