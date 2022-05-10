class DefaultConfig(object):
    """
    配置
    """
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/sale?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'd890fbe7e26c4c3eb557b6009e3f4d3d'

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''