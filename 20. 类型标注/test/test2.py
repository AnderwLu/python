from typing import TypedDict, Optional


class DatabaseConfig(TypedDict):
    """数据库配置"""
    # 你的代码：包含 host(str), port(int), username(str), password(str), database(str)
    host:str
    port:int
    username:str
    password:str
    database:str


class AppConfig(TypedDict):
    """应用配置"""
    # 你的代码：包含 app_name(str), debug(bool), db(DatabaseConfig)
    app_name:str
    debug:bool
    db:DatabaseConfig

def load_config() -> AppConfig:
    """加载默认配置"""
    return {
        "app_name": "MyApp",
        "debug": False,
        "db": {
            "host": "localhost",
            "port": 5432,
            "username": "admin",
            "password": "secret",
            "database": "mydb",
        }
    }
