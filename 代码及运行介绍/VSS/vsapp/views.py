from django.shortcuts import render,redirect
import pymysql
import xlrd#处理excle表格导入数据用的
#pymysql.install_as_MySQLdb()

def basic(request):
    return render(request, 'vssapp/basic.html')
def find(request):
    return render(request, 'vssapp/find.html')
def show(request):
    if request.method == 'POST':
        xuehao = request.POST.get('xuehao', '')  # 学号
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
        cursor = conn.cursor()
        # 定义数据库语句
        sql = "select id,grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary from vsapp_student where number = %s"
        cursor.execute(sql,(xuehao))
        m_data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return render(request, 'vssapp/show.html', {'students': m_data})
    else:
        return render(request, 'vssapp/find.html')
def list(request):#列出数据
    # 数据库的操作
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    cursor = conn.cursor()
    # 定义数据库语句
    sql = "select id,grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary from vsapp_student order by id DESC LIMIT 7"
    # 插入一条语句
    cursor.execute(sql)
    m_data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render(request, 'vssapp/list.html', {'students':m_data})
#手工编辑页面
def edit(request):
    if request.method == 'POST':
        key = request.POST.get('id','')
        grade = request.POST.get('grade', '') #年级
        number = request.POST.get('number', '')  # 学号
        name = request.POST.get('name', '')  # 名字
        sex = request.POST.get('sex', '')  # 性别
        major = request.POST.get('major', '')  # 专业
        target = request.POST.get('target', '')  # 就业情况：工作、考研、考公或事业单位、参军、其他
        situation = request.POST.get('situation', '')  # 就业结果：成功或失败，0/1
        later = request.POST.get('later', '')  # 接下来的就业计划：工作、考研、考公或事业单位、其他
        position = request.POST.get('position', '')  # 工作岗位
        province = request.POST.get('pro', '')  # 毕业后去往的省份
        city = request.POST.get('city', '')  # 毕业后去往的城市
        AnnualSalary = request.POST.get('AnnualSalary', '')  # 工作年薪
        #数据库的操作
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
        cursor = conn.cursor()
        # 定义数据库语句
        cursor.execute("update vsapp_student set grade=%s,number=%s,name=%s,sex=%s,major=%s,target=%s,situation=%s,later=%s,position=%s,province=%s,city=%s,AnnualSalary=%s where id=%s",[grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary,key])
        # 提交语句到数据库
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('../editSuccessful')
    else:
        xuehao = request.GET.get('id', '')  # 学号
        # 数据库的操作
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
        cursor = conn.cursor()
        # 定义数据库语句
        sql = "select id,grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary from vsapp_student where number = %s"
        # 插入一条语句
        cursor.execute(sql, (xuehao))
        m_data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return render(request, 'vssapp/edit.html', {'students': m_data})
def editSuccessful(request):
    return render(request, 'vssapp/editSuccessful.html')
#添加数据页面
def add(request):
    if request.method == 'POST':
        grade = request.POST.get('grade', '') #年级
        number = request.POST.get('number', '')  # 学号
        name = request.POST.get('name', '')  # 名字
        sex = request.POST.get('sex', '')  # 性别
        major = request.POST.get('major', '')  # 专业
        target = request.POST.get('target', '')  # 就业情况：工作、考研、考公或事业单位、参军、其他
        situation = request.POST.get('situation', '')  # 就业结果：成功或失败，0/1
        later = request.POST.get('later', '')  # 接下来的就业计划：工作、考研、考公或事业单位、其他
        position = request.POST.get('position', '')  # 工作岗位
        province = request.POST.get('pro', '')  # 毕业后去往的省份
        city = request.POST.get('city', '')  # 毕业后去往的城市
        AnnualSalary = request.POST.get('AnnualSalary', '')  # 工作年薪
        #数据库的操作
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
        cursor = conn.cursor()
        # 定义数据库语句
        sql = "insert into vsapp_student(grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #插入一条语句
        cursor.execute(sql,(grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/AddSuccessful')
    else:
        return render(request, 'vssapp/add.html')
#添加数据成功的提示页面
def AddSuccessful(request):
    return render(request, 'vssapp/AddSuccessful.html')
def delete(request):
    xuehao = request.GET.get('id', '')  # 学号
    # 数据库的操作
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    cursor = conn.cursor()
    # 定义数据库语句
    sql = "DELETE FROM vsapp_student WHERE number=%s"
    # 插入一条语句
    cursor.execute(sql, (xuehao))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('deleteSuccessful')#redirect重定向到某目录，最后还是要去urls去找的，所以不能用return redirect('vssapp/deleteSuccessful')
def deleteSuccessful(request):
    return render(request, 'vssapp/deleteSuccessful.html')
def deleteAll(request):
    # 数据库的操作
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    cursor = conn.cursor()
    # 定义数据库语句
    sql = "DELETE FROM vsapp_student "
    # 插入一条语句
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return render(request, 'vssapp/deleteAllSuccessful.html')
def deleteAllSuccessful(request):
    return render(request, 'vssapp/deleteAllSuccessful.html')
#excle表格导入并批量写入数据到mysql的功能
def upload(request):
    if request.method == 'POST':
        fn = request.FILES['file']
        filename=str(fn)#我们只需要文件名，所以要将fn转化为str类型,需要注意的是fn = request.FILES.get('filename')这个是错误的写法，无法通过他获得文件名
        book = xlrd.open_workbook(filename)# 打开数据所在的工作簿，以及选择存有数据的工作表
        sheet = book.sheet_by_name("Sheet1")
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students') # 建立一个MySQL连接
        cursor = conn.cursor()
        sql = "insert into vsapp_student(grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" # 创建插入SQL语句
        for r in range(1, sheet.nrows):# 创建一个for循环迭代读取xls文件每行数据的, 从1开始计数是要跳过标题行和序号行
            grade = sheet.cell(r, 1).value
            number = sheet.cell(r, 2).value
            name = sheet.cell(r, 3).value
            sex = sheet.cell(r, 4).value
            major = sheet.cell(r, 5).value
            target = sheet.cell(r, 6).value
            situation = sheet.cell(r, 7).value
            later = sheet.cell(r, 8).value
            position = sheet.cell(r, 9).value
            province = sheet.cell(r, 10).value
            city = sheet.cell(r, 11).value
            AnnualSalary = sheet.cell(r, 12).value
            values = (grade,number,name,sex,major,target,situation,later,position,province,city,AnnualSalary)
            cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        rows = int(sheet.nrows)#统计共有多少行，以便在导入成功页面进行展示
        m_rows=rows-1#减去标题那一栏
        return render(request, 'vssapp/importExcel.html', {'rows': m_rows})
    else:
         return render(request, 'vssapp/upload.html')
def importExcel(request):
    return render(request, 'vssapp/importExcel.html')
#首页
def index(request):
    return render(request, 'vssapp/index.html')








