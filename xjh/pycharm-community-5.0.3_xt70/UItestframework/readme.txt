UItestframework��ĿĿǰ�������¹��ܣ�
��ʵ�ٶ�UI�Զ������Կ�ܣ�������ܶ���ص���Ϣ��������û���ҵ�����Ŀ�ģ��޷�����ʹ�õģ������������д��һ���򵥣���������������������Ŀ�п���ʹ�õĲ��Կ�ܡ�
��Ŀ�ĵ�ַ��https://github.com/xiaoshitoutester/UItestframework
������ȫ�Ǹɻ����м��漰���ܶ�֪ʶ�㣬�������ص�����Ȼ���޸�����Ŀ��ַ����д���������Ϳ���ִ���ˣ���־������ʲô�Ķ��У�
������־��ӡ�����¼ӵģ����Զ��������У��������ָ�����ֵ����⣬���²��ö�λ���⣬�����ҽ�webdriver�ĸ��ֲ�����������־��������ui�������ⶨλ���а�����������Ǳ����С�log�ļ�����־��¼��ͼ��

1����webdriver�����˵ڶ��εļ򵥷�װ��ʹ�ø��ӷ��� public/common/pyselenium.py
(ps��������ڳ�ʦ��pyse�������˴�ӡ��־����,�ο���https://github.com/defnngj/pyse)
2�����Զ�excel��������ݶ�ȡ�������������:public/common/datainfo.py
3�����д�ӡ��־�Ĺ��ܣ���ӡ�ڿ���̨���ļ��У�public/common/log.py,��־������report/log/Ŀ¼��
4����ȡ�����ļ�(.ini�ļ�):public/common/readconfig.py
5�����з��ʼ��Ĺ���:public/common/sendmail.py
6�����ɲ��Ա��棺html���Ա����·����report/testreport/Ŀ¼��
7��ʹ����PageObjectģʽ����д���Խű�

������Ŀ��Ŀ¼�ṹ:
����config �����ļ���Ŀ¼
��  ��  config.ini   ��������ļ�
��  ��  globalparam.py  ��Ҫ��ȫ�ֲ�������log��report��·�����õ�
��  ��  __init__.py
��  ��
��
����data   ��������
��  ����formaldata # ��ʽ������������
��  ����testdata  # ���Ի���������
��          searKey.xlsx
��
����public  �������ļ���
��  ��  __init__.py
��  ��
��  ����common  ��װ�Ĺ�������
��  ��  ��  basepage.py
��  ��  ��  datainfo.py
��  ��  ��  log.py
��  ��  ��  mytest.py
��  ��  ��  publicfunction.py
��  ��  ��  pyselenium.py
��  ��  ��  pyselenium20161107.py
��  ��  ��  readconfig.py
��  ��  ��  sendmail.py
��  ��  ��  __init__.py
��  ��  ��
��  ��
��  ����pages ʹ��pageobjectģʽ��д���Խű������page��Ŀ¼
��  ��  ��  baiduIndexPage.py
��  ��  ��  __init__.py
��
����report ���Ա���
��  ����image ��ͼĿ¼
��  ����log ��־Ŀ¼
��  ��      2016-11-07.log
��  ��
��  ����testreport  html���Ա���Ŀ¼
��          TestResult2016-11-07_16_15_51.html
��
����testcase ��Ų�������
    ��  test_baidu.py

ʹ��˵��:
��װ��Ӧ�Ŀ�: pip install xlrd,selenium,configparser
1����config.ini��������Ŀ·����project_path
2���������ݷ���dataĿ¼����
3��ʹ��pageobject��дpageҳ�棬�ڲ�������������÷���public/pagesĿ¼��
4����testcaseĿ¼���棬��д�������������Է�ģ���д������Ӧ��Ŀ¼
5��ִ��run.py,�Ϳ���ִ�����еĲ�������
6����report/log����鿴��־
7����report/testreport����鿴html���Ա���

����pyselenium��ʹ��:
��py�ļ��Ǹ��ݳ�ʦ��pyse�ĵģ�����һ����־�������Լ�����Ҫ���˼�������
���Բο���ʦ��pyse,github��ַ:https://github.com/defnngj/pyse
��ʦ�Ĳ���԰��ַ��https://github.com/defnngj/pyse

����PySlenium�ļ�
import PySelenium
1�������������
�����ȸ������
dr = PySelenium.PySelenium('chrom')
����Զ�����������ʹ��gridʩ�зֲ�ʽִ��
dr = PySelenium.PySelenium(RChrome','127.0.0.1:8080')
2���ڵ�ַ��������ַ��
dr.open('http://www.baidu.com')
3���������
dr.max_window()
4������������Ĵ��ڵĴ�С
dr.set_window(800,500)
5��������ı��������ֱ������ֵ(����˵�������ļ��ϴ�ʱ���ϴ��ļ���·�����������ͻᱨ��)��
dr.type('id->su','Сʯͷtester')
6��������ı�������ݣ�Ȼ��������ֵ���õúࣩܶ��
dr.clear_type('name->su','��ʦ')
7��ֱ�ӵ��Ԫ��
dr.click('css->#kw')
8���Ҽ����Ԫ�أ�
dr.right_click('id->kw')
9��������ƶ���һ��Ԫ����
dr.move_to_element('clas->btn1.btn-green.btn-search')
10��˫��Ԫ��
dr.double_click("id->kw")
11����һ��Ԫ����ק������һ��Ԫ����
dr.drag_and_drop('id->kw1','id->kw2')
12���������ӵ�text�����(<a href="http://www.baidu.com">�ٶ�</a>)
dr.click_text('�ٶ�')
13���رմ��ڣ�driver
dr.quit()
14��ִ��js�ű�
dr.js('script')
15����ȡԪ�ص�����
dr.get_attribute("id->su","href")
16����ȡԪ�ص��ı���Ϣtext
dr.get_text('id->su')
17�����ص�ǰҳ���title
dr.get_title()
18�����ص�ǰҳ���url
dr.get_url()
20������frame
dr.switch_to_frame('id->kw')
21���˳�frame
dr.switch_to_frame_out()
22���ж�Ԫ���Ƿ����
dr.element_exist('id->kw')
23����ͼ
dr.take_screenshot('file_path')
24���������µ�table
dr.into_new_window()
25���������ݲ��һس�
dr.type_and_enter('id->kw')
26��ʹ��js�����ĳ��Ԫ��
dr.js_click('id->kw')
27������ԭ����webdriver�����и��Ի�����
dr.origin_driver()