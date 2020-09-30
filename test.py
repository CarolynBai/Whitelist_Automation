# -*-coding:utf8 -*-
# Bai Yuning created
# Feel free to contact me if there's a problem, Tel：18001161013; Wechat num: 357909318
from selenium import webdriver
import time
import csv
import tkinter
import tkinter.messagebox #弹窗库

driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  # chromedriver的文件位置

browser = webdriver.Chrome(executable_path=driver)


def main():
    # 在当前浏览器中访问list
    browser.get(
        'https://issues.amazon.com/issues/search?q=status%3A(Open)+containingFolder%3A(7afcfcfd-4b2e-4aad-b95e-de19706ddda4)&sort=createDate+desc&selectedDocument=353d70dc-e4ab-444b-a4ff-3c33b51000e7')
    time.sleep(30)
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("https://aws-id-whitelisting.amazon.com/external_registion");'
    browser.execute_script(js)
    time.sleep(8)


def whitelist():
    # 输出当前窗口句柄（list）
    list_handle = browser.current_window_handle

    # 获取当前窗口句柄集合（列表类型）
    handles = browser.window_handles
    # print(handles)  # 输出句柄集合
    # ['CDwindow-E9B85270B51D42AF7369D81B9AA70FFE',
    # 'CDwindow-90004FD79A0F59EE057846B34D0E7327']

    # 获取录入窗口
    input_handle = None
    for handle in handles:
        if handle != list_handle:
            input_handle = handle
    i = 0
    n = 0

    browser.switch_to.window(list_handle)

    with open('record.csv', 'a+', encoding='utf-8') as f:  # 打开文件

        f_csv = csv.writer(f)

        while n == 0:

            #while browser.find_element_by_class_name('queue-item-contents') == True:

                # id = i + 1
                # i = id
            try:
                browser.find_element_by_class_name('queue-item-contents').click()
                time.sleep(10)
                type = browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/header/div[5]/div/div/div[2]/form/fieldset/div[1]/h2/span[2]')
                if type.text == 'Whitelist Request From BD':
                    getURL = browser.current_url
                    getOwner = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/strong')
                    getEmail = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[1]/p/a')
                    getCompany = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[2]/p')
                    getRemarks = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[3]/p')
                    getSource = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[4]/p')
                    Email = getEmail.text
                    Company = getCompany.text
                    Remarks = getRemarks.text
                    Source = getSource.text
                    Owner = getOwner.text
                    Link = getURL

                    f_csv.writerow(('BD', Owner, Email, Company, Remarks, Source, Link)) #BD团队提交的sim的格式
                    Info = ('\nRegistration Email Address'
                            + '\n' + Email
                            + '\n'
                            + '\nCompany Name'
                            + '\n' + Company
                            + '\n'
                            + '\nRemarks'
                            + '\n' + Remarks
                            + '\n'
                            + '\nWhether the customer filled Contact US Form from website'
                            + '\n' + Source)
                    print(Info)

                if type.text == 'Whitelist Request From LDR':
                    getURL = browser.current_url
                    getOwner = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/strong')
                    getEmail = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[1]/p/a')
                    getCompany = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[2]/p')
                    getCampaignSource = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[3]/p')
                    getMQLorLEADID = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[4]/p')
                    getRemarks = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div[4]/section[1]/div/section/div[1]/div[2]/div[2]/div[1]/div[3]/div/section/div[2]/span/div/div[1]/div[1]/div[5]/p')
                    Email = getEmail.text
                    Company = getCompany.text
                    CampaignSource = getCampaignSource.text
                    MQLorLEADID = getMQLorLEADID.text
                    Remarks = getRemarks.text
                    Owner = getOwner.text
                    Link = getURL

                    f_csv.writerow(('LDR', Owner, Email, Company, CampaignSource, MQLorLEADID, Remarks, Link)) #LDR团队提交的sim的格式

                    Info = ('\nRegistration Email Address'
                            + '\n' + Email
                            + '\n'
                            + '\nCompany Name'
                            + '\n' + Company
                            + '\n'
                            + '\nCampaign Source'
                            + '\n' + CampaignSource
                            + '\n'
                            + '\nMQL ID or LEAD ID'
                            + '\n' + MQLorLEADID
                            + '\n'
                            + '\nRemarks'
                            + '\n' + Remarks
                            )
                    print(Info)

                browser.switch_to.window(input_handle)
                while n == 0:
                    browser.find_element_by_xpath('//*[@id="EmailAddress"]/div[1]/input').send_keys(Email)
                    time.sleep(3)
                    browser.find_element_by_xpath('//*[@id="AddressInfo"]/div[2]/span/button').click()
                    time.sleep(8)
                    InputError = browser.find_element_by_xpath('//*[@id="EmailAddress"]/div[1]/span')
                    #InputFailed = browser.find_element_by_xpath('//*[@id="ErrorDiv"]/div')
                    InputSuccess = browser.find_element_by_xpath('//*[@id="InfoComplete"]/h3')
                    if browser.find_element_by_xpath('//*[@id="InfoComplete"]/h3').text == 'Registration Complete':
                        print('test pass: input successful')
                        browser.refresh()  # 刷新录入界面 refresh
                        time.sleep(5)
                        print('test pass: refresh successful')
                        break
                    if InputError.text == 'E-mail address must contain @':#当email地址不含有@时会报出此类错误。此处会跳出弹窗，记录到ErrorRecord并退出程序
                        print('format error: E-mail address must contain @')
                        tkinter.messagebox.showerror('error', 'format error: E-mail address must contain @')
                        with open('ErrorRecord.csv', 'a+', encoding='utf-8') as r:  # 打开文件
                            r_csv = csv.writer(r)
                            r_csv.writerow((Owner, Email, Company, Remarks, Link))#record中的文件格式，可根据link track到相关sim并人工解决
                            r.close()
                        exit()
                    if browser.find_element_by_xpath('/html/body/div[2]/div[1]/div'):#当email地址含有@，但不符合邮箱格式的其他基本规则时会报出failed错误此处会跳出弹窗，记录到ErrorRecord并退出程序
                        print('Input error: Invalid Email Address')
                        tkinter.messagebox.showerror('error', 'Input error: Invalid Email Address')
                        with open('ErrorRecord.csv', 'a+', encoding='utf-8') as r:  # 打开文件
                            r_csv = csv.writer(r)
                            r_csv.writerow((Owner, Email, Company, Remarks, Link))#record中的文件格式，可根据link track到相关sim并人工解决
                            r.close()
                        exit()
                    else:#网络不稳定的情况下会出现无法录入成功的情况，此处为重新刷新页面
                        browser.refresh()  # 刷新录入界面 refresh
                        time.sleep(5)
                        print('网络不佳，页面重新加载')


                # 切换回list窗口
                browser.switch_to.window(list_handle)
                browser.find_element_by_xpath('//*[@id="issue-conversation"]').send_keys('Hi team,'
                                                                                         + '\n'
                                                                                         + '\n客户注册邮箱白名单已完成，请您通知客户参考http://cet-bucket.s3.cn-north-1.amazonaws.com.cn/Process/Onboarding/Customer%20Account%20Registration.pdf  进行账号申请。'
                                                                                         + '\n'
                                                                                         + '\n如果客户注册中断导致账号信息未上传成功，建议客户通过以下链接，输入Account ID和第一次注册填写时相同的IAM用户名，IAM用户的密码，系统会自动进入上次中断的位置，客户继续完成注册即可。请参考以下链接： https://signup.amazonaws.cn/billing/signup?type=resubscribe'
                                                                                         + '\n'
                                                                                         + '\n*如果遇到客户注册批量账号，为提高客户体验，建议先提交一个账号，待该账号通过核验之后，再提交其他账号。以减少客户修改信息次数。'
                                                                                         + '\n'
                                                                                         + '\nThe registration email of customer has been whitelisted. Please inform customer to submit new account application by referring: http://cet-bucket.s3.cn-north-1.amazonaws.com.cn/Process/Onboarding/Customer%20Account%20Registration.pdf '
                                                                                         + '\n'
                                                                                         + '\nIf customers do not finish registration and quit, the information of the account will not be uploaded successfully.  Under such circumstances, they may click the following link and type in account ID and IAM user name ( must be the same with the previous ones they typed). Our system will automatically show the page they left to allow customers to finish account registration. More info in the following link: https://signup.amazonaws.cn/billing/signup?type=resubscribe'
                                                                                         + '\n'
                                                                                         + '\n*If customers apply for several accounts at one time, please suggest that the customer first upload BL/PID for one account. If that account passes validation, then the customer may finish uploading for others accounts. By doing so, we hope to reduce the risk of multiple failures and uploading.'
                                                                                         + '\n'
                                                                                         + '\n---------------------------------------------'
                                                                                         + '\nBD可通过YUNMENG系统https://yunmeng.aka.amazon.com 进行查询新账号申请核验状态'
                                                                                         + '\n操作指导请参见http://cet-bucket.s3.cn-north-1.amazonaws.com.cn/Process/Onboarding/YunMeng%20Validation%20Search%20SOP.pdf , 如果在Yun Meng 系统中通过客户ID 或者注册邮箱未查询到相关申请记录，即客户并没有完成所有页面的信息填写提交 ，可以将链接：https://signup.amazonaws.cn/billing/signup?type=resubscribe#/ 发送给客户， 输入Account ID和第一次注册填写时相同的IAM用户名，IAM用户的密码，系统会自动进入上次中断的位置, 务必请客户完成所有页面的信息，将申请提交成功后再做审核状态的查询。'
                                                                                         + '\n请注意：Yun Meng 系统的权限，需要您申请加入正确的Permission Group: AWSCN-Portal-BD (LDAP Group)，https://permissions.amazon.com/group.mhtml?target=11339481申请审批通过后最多可能需要24小时生效。如果申请审批通过已经超过24小时而您依然无法访问Yun Meng 系统，请您清空浏览器缓存后再重新进行尝试。'
                                                                                         + '\n'
                                                                                         + '\nBD could check new account validation status in YUNMENG system, and find the SOP here. If no result found by customer ID/registration email searching in the validation, it means customer did not submit the account application successfully. please send the link:https://signup.amazonaws.cn/billing/signup?type=resubscribe# to customer for completion.'
                                                                                         + '\n'
                                                                                         + '\nAttention: Please subscribe yourself to correct permission group to get Yun Meng access: AWSCN-Portal-BD (LDAP Group https://permissions.amazon.com/group.mhtml?target=11339481, it will take up  to 24 hours to take effective after your request approved.'
                                                                                         + '\n'
                                                                                         + '\n-------------------------------------------------------------------------------------------------'
                                                                                         + '\n'
                                                                                         + Info
                                                                                         )
                time.sleep(2)
                browser.find_element_by_xpath(
                    '//*[@id="issue-stream-form"]/fieldset/div[2]/div[1]/div[2]/button').click()
                time.sleep(3)
                browser.find_element_by_xpath('// *[ @ id = "resolve-issue-form"] / div / div / div[3] / input').click()
                time.sleep(5)
                try:
                    browser.refresh()  # 刷新list界面 refresh
                    time.sleep(10)
                    print('test pass: refresh successful')
                except Exception as e:
                    print("Exception found", format(e))
                    break

            except Exception as e:
                error = ("Exception found", format(e))
                if error == ('Exception found', 'Message: no such element: Unable to locate element: {"method":"css selector","selector":".queue-item-contents"}\n  (Session info: chrome=83.0.4103.97)\n'):
                    print("白名单已全部清理完成，程序休眠10分钟")
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    tkinter.messagebox.showinfo('info', '白名单已全部清理完成，程序休眠10分钟')
                    time.sleep(600)
                else:
                    print(error)

    f.close()


if __name__ == '__main__':
    main()
    whitelist()
