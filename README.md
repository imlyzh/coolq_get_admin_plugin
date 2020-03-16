# coolq_get_admin_plugin
一个酷Q插件，提供了加群后需要管理员权限的功能。需配合aiocqhttp插件使用

加群后需要在指定时间内给予管理员，否则退群。
需配置config文件

提供了Pyinstaller打包的方法（pkg.cmd）

## 使用方法:
1. 将`扣扣号.json`文件复制到`\data\app\io.github.richardchien.coolqhttpapi\config`目录中并改名为机器人的QQ号
2. 启动CQHTTP插件
3. 将`bot.exe`和`cgap.config.json`放在一个文件夹中，并配置`cgap.config.json`文件
    - "super_user": 你的QQ号,
    - "wait_minute": 等待后退群时间
    - 其它如果你不明白是什么，不要动
4. 启动`bot.exe`

## Append:

鉴于现在的网络环境，为防各种坑爹情况发生。我决定在包体积较小时直接在源码中提供打包好的应用（win32-only）