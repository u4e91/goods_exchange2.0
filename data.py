import os
import json

# 全局变量
_items = {} # 保存物品库存的字典
_users = {} # 保存用户信息的字典
_registers = {} # 保存正在注册的用户的字典
_types = {} # 保存物品类型的字典

def init():
    """从磁盘JSON格式文件中读取数据"""
    global _items, _users, _registers, _types
    if os.path.exists("items.json"):
        f = open("items.json", "r", encoding='utf-8')
        _items = json.loads(f.read())
        f.close()
    if os.path.exists("users.json"):
        f = open("users.json", "r", encoding='utf-8')
        _users = json.loads(f.read())
        f.close()
    if os.path.exists("registers.json"):
        f = open("registers.json", "r", encoding='utf-8')
        _registers = json.loads(f.read())
        f.close()
    if os.path.exists("types.json"):
        f = open("types.json", "r", encoding='utf-8')
        _types = json.loads(f.read())
        f.close()

def _save_items():
    """把物品信息数据_items以JSON格式保存到磁盘"""
    global _items
    f = open("items.json", "w", encoding='utf-8')
    f.write(json.dumps(_items, ensure_ascii=False))
    f.close()


def _save_users():
    """把用户信息数据_users以JSON格式保存到磁盘"""
    global _users
    f = open("users.json", "w", encoding='utf-8')
    f.write(json.dumps(_users, ensure_ascii=False))
    f.close()


def _save_registers():
    """把注册用户信息数据_registers以JSON格式保存到磁盘"""
    global _registers
    f = open("registers.json", "w", encoding='utf-8')
    f.write(json.dumps(_registers, ensure_ascii=False))
    f.close()

def _save_types():
    """把类别信息数据_types以JSON格式保存到磁盘"""
    global _types
    f = open("types.json", "w", encoding='utf-8')
    f.write(json.dumps(_types, ensure_ascii=False))
    f.close()


def get_items():
    """返回物品信息"""
    global _items
    return _items

def get_users():
    """返回用户信息"""
    global _users
    return _users

def get_registers():
    """返回注册用户信息"""
    global _registers
    return _registers

def get_types():
    """返回类别信息"""
    global _types
    return _types
    
def add_items(id, name, type, instru, place, tel, email, other, uaname):
    """增加一个物品"""
    global _items
    uinfo = [name, type, instru, place, tel, email, other, uaname]
    _items[id] = uinfo
    _save_items()


def add_users(name, password, place, tel):
    """增加一个用户"""
    global _users
    uinfo = [password, place, tel]
    _users[name] = uinfo
    _save_users()

def add_registers(name, password, place, tel):
    """增加一个注册用户"""
    global _registers
    uinfo = [password, place, tel]
    _registers[name] = uinfo
    _save_registers()

def change_types(name, cla):
    """修改物品类别"""
    global _types
    uinfo = [cla]
    _types[name] = uinfo
    _save_types()

def remove_item(id):
    """出库一个物品"""
    global _items
    del _items[id]
    _save_items()

def remove_registers(name):
    """删除一个注册用户"""
    global _registers
    del _registers[name]
    _save_registers()