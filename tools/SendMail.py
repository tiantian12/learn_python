#encoding:utf-8
#导包
import zmail

#邮件消息体
mail_content={
    "SUBJECT":"邮件主题123",
    "Content_html":"邮件内容1"
}

#进行邮箱验证创建连接
server=zmail.server("I_love_you_tian@163.com","ForTest123456")

#发送邮件
server.send_mail("clareliu@futunn.com",mail_content)





#收邮件demo
#server=zmail.server("2601504660@qq.com","iflcppcfpijmeaid")

#获取最新邮件
mail=server.get_latest()

#依据id获取邮件
#mail=server.get_mail(6)

#根据条件获取邮件列表
#mail=server.get_mails(subject="芭依珊",start_time="2019-1-19")

#获取所有邮件头信息
#mail_info=server.get_headers()

#获取收件箱信息
#mailbox_info=server.stat()

#获取邮件的主题
#subject=mail['subject']

#展示邮件的信息
zmail.show(mail)
