from flask_script import Manager
from App import __int__

app  = __int__.init_app()

#全局的对象

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()

'''
static 放置静态文件
T 前端模板
M 控制数据库
V 试图关联前端，放路由
'''
