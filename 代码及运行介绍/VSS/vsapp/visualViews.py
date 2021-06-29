from django.shortcuts import render
from pyecharts.charts import Bar
import pymysql
#条形统计图
def bar_is_selected(request):
    return render(request, 'visual/bar_is_selected.html')
def barVisval(request):
    b=bar()
    return render(request, 'visual/barVisval.html')
def bar():
    majorName=["网络工程","物联网工程","软件工程","数字媒体技术",]
    targetName=["就业","升学","考编","从军",]
    a = [0,1,2,3]
    b = [0,1,2,3]
    c = [0,1,2,3]
    d = [0,1,2,3]
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    for i in majorName:#专业
        for j in targetName:#目标
            # 数据库的操作
            cursor = conn.cursor()
            sql = "SELECT count(*) FROM vsapp_student where major=%s and target=%s"
            cursor.execute(sql, (i,j))
            data = cursor.fetchone()#返回单个元组
            data_list=data[0]#取元组中索引为0的数
            #cursor.fetchall()#返回多个元组
            conn.commit()
            cursor.close()
            #data_list = exc_sql(query_sql,(majorName[j],targetName[i]))
            if i=='网络工程':
                n = 0
            if i =='物联网工程':
                n = 1
            if i =='软件工程':
                n = 2
            if i =='数字媒体技术':
                n = 3
            if j=='就业':
                a[n] = data_list
            if j=='升学':
                b[n] = data_list
            if j =='考编':
                c[n] = data_list
            if j == '从军':
                d[n] = data_list
    conn.close()
    c = (
        Bar()
        .add_xaxis(
            ["网络工程","物联网工程","软件工程","数字媒体技术",]
        )
        .add_yaxis("企业就业", a)
        .add_yaxis("升学", b)
        .add_yaxis("考编", c)
        .add_yaxis("从军", d)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="人数", subtitle="各目标人数"),
        )
        .render(r'C:\Users\Administrator\Desktop\VSS\vsapp\templates\visual\bar_is_selected.html')
    )

# 目标完成情况扇形统计图
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode

def target_pie_label(request):
    return render(request, 'visual/target_pie_label.html')
def targetVisval(request):
    target=targetPie()
    return render(request, 'visual/targetVisval.html')

fn = """
    function(params) {
        if(params.name == '暂未成功')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """

def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")
def targetPie():
    targetName = ["就业","升学","考编","从军",]
    target_s = [0,1,2,3]# success,目标成功依次代表"就业","升学","考编","从军",
    target_f = [0,1,2,3]  # fales,目标暂未成功依次代表"就业","升学","考编","从军",
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    for j in targetName:  # 目标
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM vsapp_student where  target=%s and situation='成功'"
        cursor.execute(sql,j)
        data = cursor.fetchone()  # 返回单个元组
        target_data= data[0]  # 取元组中索引为0的数
        conn.commit()
        cursor.close()
        if j == '就业':
            target_s[0] = target_data
        if j == '升学':
            target_s[1] = target_data
        if j == '考编':
            target_s[2] = target_data
        if j == '从军':
            target_s[3] = target_data
    for j in targetName:  # 目标
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM vsapp_student where  target=%s and situation='暂未成功'"
        cursor.execute(sql,j)
        data = cursor.fetchone()  # 返回单个元组
        target_data= data[0]  # 取元组中索引为0的数
        conn.commit()
        cursor.close()
        if j == '就业':
            target_f[0] = target_data
        if j == '升学':
            target_f[1] = target_data
        if j == '考编':
            target_f[2] = target_data
        if j == '从军':
            target_f[3] = target_data
    conn.close()
#计算部分
    #就业比例计算,#取第一个字的拼音表示成功的部分，第二个字的拼音表示失败的部分，下方其他计算也相同
    target_jiu=target_s[0]
    target_ye = target_f[0]
    taret_jiuye=float(target_jiu+target_ye)
    jiu=(float(target_jiu) / taret_jiuye)*100
    jiu=round(jiu)
    ye =(float(target_ye) / taret_jiuye) * 100
    ye=round(ye)
    # 升学比例计算
    target_sheng=target_s[1]
    target_xue = target_f[1]
    taret_shengxue=float(target_sheng+target_xue)
    sheng=(float(target_sheng) / taret_shengxue)*100
    sheng=round(sheng)
    xue =(float(target_xue) / taret_shengxue) * 100
    xue=round(xue)
    # 考编比例计算
    target_kao=target_s[2]
    target_bian = target_f[2]
    taret_kaobian=float(target_kao+target_bian)
    kao=(float(target_kao) / taret_kaobian)*100
    kao=round(kao)
    bian =(float(target_bian) / taret_kaobian) * 100
    bian=round(bian)
    # 从军比例计算
    target_cong=target_s[3]
    target_jun = target_f[3]
    taret_congjun=float(target_cong+target_jun)
    cong=(float(target_cong) / taret_congjun)*100
    cong=round(cong)
    jun =(float(target_jun) / taret_congjun) * 100
    jun=round(jun)
    c = (
        Pie()
            .add(
            "",
            #取第一个字的拼音表示成功的部分，第二个字的拼音表示失败的部分
            [list(z) for z in zip(["企业就业", "暂未成功"], [jiu, ye])],#方括号里的是百分数，只是省略了百分数的符号
            center=["20%", "30%"],
            radius=[60, 80],
            label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(["升学", "暂未成功"], [sheng, xue])],
            center=["55%", "30%"],
            radius=[60, 80],
            label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(["考编", "暂未成功"], [kao, bian])],
            center=["20%", "70%"],
            radius=[60, 80],
            label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(["从军", "暂未成功"], [cong, jun])],
            center=["55%", "70%"],
            radius=[60, 80],
            label_opts=new_label_opts(),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="毕业生目标完成情况"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
            ),
        )
            .render(r'C:\Users\Administrator\Desktop\VSS\vsapp\templates\visual\target_pie_label.html')
        )



#工作职位类别扇形统计图
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

def pie_rich_label(request):
    return render(request, 'visual/pie_rich_label.html')
def jobVisval(request):
    job=jobPie()
    return render(request, 'visual/jobVisval.html')

def jobPie():
    values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]#共14项
    positionName = ["办事人员和有关人员", "工程技术人员", "公务员", "教学人员", "金融业务人员", "经济业务人员", "军人", "科学研究人员", "其他人员", "其他专业技术人员", "商业和服务业人员", "卫生专业技术人员", "文学艺术工作人员", "新闻出版和文化工作人员"]
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    for j in positionName:
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM vsapp_student where position=%s"
        cursor.execute(sql,j)
        data = cursor.fetchone()  # 返回单个元组
        conn.commit()
        cursor.close()
        if j == '办事人员和有关人员':
            values[0] = data[0]
        if j == '工程技术人员':
            values[1] = data[0]
        if j == '公务员':
            values[2] = data[0]
        if j == '教学人员':
            values[3] = data[0]
        if j == '金融业务人员':
            values[4] = data[0]
        if j == '经济业务人员':
            values[5] = data[0]
        if j == '军人':
            values[6] = data[0]
        if j == '科学研究人员':
            values[7] = data[0]
        if j == '其他人员':
            values[8] = data[0]
        if j == '其他专业技术人员':
            values[9] = data[0]
        if j == '商业和服务业人员':
            values[10] = data[0]
        if j == '卫生专业技术人员':
            values[11] = data[0]
        if j == '文学艺术工作人员':
            values[12] = data[0]
        if j == '新闻出版和文化工作人员':
            values[13] = data[0]
    conn.close()
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "",  # 系列名称
            # 系列数据项，格式为 [(key1, value1), (key2, value2)]
            [list(z)
             for z in
             zip( ["办事人员和有关人员", "工程技术人员", "公务员", "教学人员", "金融业务人员", "经济业务人员", "军人", "科学研究人员", "其他人员", "其他专业技术人员", "商务和服务业人员", "卫生专业技术人员", "文学艺术工作人员", "新闻出版和文化工作人员"], values )
             ],
            radius=["40%", "55%"],# 饼图的半径，数组的第一项是内半径，第二项是外半径
            # 标签配置项
            label_opts=opts.LabelOpts(
                # position 标签的位置
                position="outside",
                # 回调函数，回调函数格式：
                # (params: Object|Array) => string
                # 设置标签的显示样式
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",# 背景颜色
                border_color="#aaa", # 边框颜色
                border_width=1,# 边框宽度
                border_radius=4,# 边框四角弧度
                rich={
                    "a": {"color": "#999","lineHeight": 22,"align": "center"},  # 对齐方式
                    "abg": {"backgroundColor": "#e3e3e3","width": "100%", "align": "right", "height": 22, "borderRadius": [4, 4, 0, 0], },
                    "hr": { "borderColor": "#aaa", "width": "100%","borderWidth": 0.5,"height": 0, },
                    "b": {"fontSize": 16,"lineHeight": 33 },
                    # 百分比
                    "per": { "color": "#eee","padding": [2, 4],"borderRadius": 2,},  # 字体颜色 "backgroundColor": "#334455",  # 背景颜色

                },
            ),
        ) # .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .render(r'C:\Users\Administrator\Desktop\VSS\vsapp\templates\visual\pie_rich_label.html')
    )




#目标城市分布情况
#from pyecharts import Geo, Page, Style
#import pandas as pd
#import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

def city_label(request):
    return render(request, 'visual/city_label.html')
def cityVisval(request):
    city=create_charts()
    return render(request, 'visual/cityVisval.html')


def create_charts():
    #page = Page()
    #共190个城市
    cityName = [
            "海门", "鄂尔多斯", "招远","舟山","齐齐哈尔", "盐城", "赤峰", "青岛", "乳山","金昌","泉州","莱西", "日照","胶南", "南通","拉萨", "云浮", "梅州", "文登", "上海",#20
            "攀枝花","威海","承德", "厦门","汕尾", "潮州", "丹东","太仓","曲靖", "烟台","福州", "瓦房店","即墨", "抚顺", "玉溪", "张家口", "阳泉","莱州", "湖州", "汕头",#20
            "昆山","宁波", "湛江","揭阳", "荣成","连云港", "葫芦岛", "常熟","东莞", "河源", "淮安", "泰州", "南宁", "营口", "惠州", "江阴", "蓬莱","韶关", "嘉峪关", "广州", #20
            "延安", "太原","清远", "中山", "昆明", "寿光", "盘锦","长治", "深圳", "珠海", "宿迁","咸阳", "铜川","平度", "佛山", "海口","江门", "章丘","肇庆","大连",#20
            "临汾", "吴江","石嘴山","沈阳", "苏州", "茂名","嘉兴","长春","胶州","银川","张家港","三门峡","锦州","南昌","柳州","三亚","自贡","吉林","阳江","泸州",#20
            "西宁", "宜宾","呼和浩特","成都","大同","镇江","桂林","张家界","宜兴", "北海","西安", "金坛", "东营","牡丹江","遵义","绍兴","扬州","常州","潍坊","重庆",#20
            "台州", "南京","滨州","贵阳", "无锡","本溪", "克拉玛依","渭南","马鞍山","宝鸡","焦作", "句容","北京","徐州","衡水","包头","绵阳","乌鲁木齐","枣庄","杭州",#20
            "淄博", "鞍山","溧阳","库尔勒","安阳","开封","济南","德阳", "温州","九江", "邯郸","临安","兰州", "沧州","临沂","南充","天津","富阳","泰安","诸暨", #20
            "郑州", "哈尔滨", "聊城","芜湖","唐山","平顶山","邢台","德州","济宁","荆州", "宜昌","义乌", "丽水", "洛阳","秦皇岛","株洲", "石家庄","莱芜", "常德", "保定",#20
            "湘潭", "金华", "岳阳", "长沙", "衢州","廊坊", "菏泽","合肥", "武汉","大庆", #10
    ]

    city_value=[0]*190 #定义这个列表的长度为190
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='students')
    for n in range(0,189):
        city_name=cityName[n]
        cursor = conn.cursor()
        sql = "SELECT count(*) FROM vsapp_student where  city=%s"
        cursor.execute(sql,city_name)
        data = cursor.fetchone()  # 返回单个元组
        city_value[n] = data[0] # 取元组中索引为0的数
        #city_value[n] = value
        conn.commit()
        cursor.close()
    conn.close()

    data = [
        ("海门", city_value[0]), ("鄂尔多斯", city_value[1]), ("招远", city_value[2]), ("舟山", city_value[3]),
        ("齐齐哈尔", city_value[4]), ("盐城",  city_value[5]), ("赤峰", city_value[6]), ("青岛", city_value[7]),
        ("乳山", city_value[8]), ("金昌", city_value[9]), ("泉州", city_value[10]), ("莱西", city_value[11]),
        ("日照", city_value[12]), ("胶南", city_value[13]), ("南通", city_value[14]), ("拉萨", city_value[15]),
        ("云浮", city_value[16]), ("梅州", city_value[17]), ("文登", city_value[18]), ("上海", city_value[19]),
        ("攀枝花", city_value[20]), ("威海", city_value[21]), ("承德", city_value[22]), ("厦门", city_value[23]),
        ("汕尾", city_value[24]), ("潮州", city_value[25]), ("丹东", city_value[26]), ("太仓", city_value[27]),
        ("曲靖", city_value[28]), ("烟台", city_value[29]), ("福州", city_value[30]), ("瓦房店", city_value[31]),
        ("即墨", city_value[32]), ("抚顺", city_value[33]), ("玉溪", city_value[34]), ("张家口", city_value[35]),
        ("阳泉", city_value[36]), ("莱州", city_value[37]), ("湖州", city_value[38]), ("汕头", city_value[39]),
        ("昆山", city_value[40]), ("宁波", city_value[41]), ("湛江", city_value[42]), ("揭阳", city_value[43]),
        ("荣成", city_value[44]), ("连云港", city_value[45]), ("葫芦岛", city_value[46]), ("常熟", city_value[47]),
        ("东莞", city_value[48]), ("河源", city_value[49]), ("淮安", city_value[50]), ("泰州", city_value[51]),
        ("南宁", city_value[52]), ("营口", city_value[53]), ("惠州", city_value[54]), ("江阴", city_value[45]),
        ("蓬莱", city_value[56]), ("韶关", city_value[57]), ("嘉峪关", city_value[58]), ("广州", city_value[59]),
        ("延安", city_value[60]), ("太原", city_value[61]), ("清远", city_value[62]), ("中山", city_value[63]),
        ("昆明", city_value[64]), ("寿光", city_value[65]), ("盘锦", city_value[66]), ("长治", city_value[67]),
        ("深圳", city_value[68]), ("珠海", city_value[69]), ("宿迁", city_value[70]), ("咸阳", city_value[71]),
        ("铜川", city_value[72]), ("平度", city_value[73]), ("佛山", city_value[74]), ("海口", city_value[75]),
        ("江门", city_value[76]), ("章丘", city_value[77]), ("肇庆", city_value[78]), ("大连", city_value[79]),
        ("临汾", city_value[80]), ("吴江", city_value[81]), ("石嘴山", city_value[82]), ("沈阳", city_value[83]),
        ("苏州", city_value[84]), ("茂名", city_value[85]), ("嘉兴", city_value[86]), ("长春", city_value[87]),
        ("胶州", city_value[88]), ("银川", city_value[89]), ("张家港", city_value[90]), ("三门峡", city_value[91]),
        ("锦州", city_value[92]), ("南昌", city_value[93]), ("柳州", city_value[94]), ("三亚", city_value[95]),
        ("自贡", city_value[96]), ("吉林", city_value[97]), ("阳江", city_value[98]), ("泸州", city_value[99]),
        ("西宁", city_value[100]), ("宜宾", city_value[101]), ("呼和浩特", city_value[102]), ("成都", city_value[103]),
        ("大同", city_value[104]), ("镇江", city_value[105]), ("桂林", city_value[106]), ("张家界", city_value[107]),
        ("宜兴", city_value[108]), ("北海", city_value[109]), ("西安", city_value[110]), ("金坛", city_value[111]),
        ("东营", city_value[112]), ("牡丹江", city_value[113]), ("遵义",city_value[114]), ("绍兴", city_value[115]),
        ("扬州", city_value[116]), ("常州",city_value[117]), ("潍坊", city_value[118]), ("重庆", city_value[119]),
        ("台州", city_value[120]), ("南京", city_value[121]), ("滨州", city_value[122]), ("贵阳", city_value[123]),
        ("无锡", city_value[124]), ("本溪", city_value[125]), ("克拉玛依", city_value[126]), ("渭南", city_value[127]),
        ("马鞍山",city_value[128]), ("宝鸡", city_value[129]), ("焦作", city_value[130]), ("句容", city_value[131]),
        ("北京", city_value[132]), ("徐州", city_value[133]), ("衡水", city_value[134]), ("包头",city_value[135]),
        ("绵阳", city_value[136]), ("乌鲁木齐", city_value[137]), ("枣庄", city_value[138]), ("杭州", city_value[139]),
        ("淄博", city_value[140]), ("鞍山", city_value[141]), ("溧阳",city_value[142]), ("库尔勒", city_value[143]),
        ("安阳", city_value[144]), ("开封",city_value[145]), ("济南", city_value[146]), ("德阳", city_value[147]),
        ("温州", city_value[148]), ("九江", city_value[149]), ("邯郸", city_value[150]), ("临安", city_value[151]),
        ("兰州", city_value[152]), ("沧州", city_value[153]), ("临沂", city_value[154]), ("南充", city_value[155]),
        ("天津", city_value[156]), ("富阳", city_value[157]), ("泰安", city_value[158]), ("诸暨", city_value[159]),
        ("郑州", city_value[160]), ("哈尔滨", city_value[161]), ("聊城", city_value[162]), ("芜湖", city_value[163]),
        ("唐山", city_value[164]), ("平顶山", city_value[165]), ("邢台", city_value[166]), ("德州", city_value[167]),
        ("济宁", city_value[168]), ("荆州", city_value[169]), ("宜昌", city_value[170]), ("义乌", city_value[171]),
        ("丽水", city_value[172]), ("洛阳", city_value[173]), ("秦皇岛", city_value[174]), ("株洲", city_value[175]),
        ("石家庄", city_value[176]), ("莱芜", city_value[177]), ("常德", city_value[178]), ("保定", city_value[179]),
        ("湘潭", city_value[180]), ("金华", city_value[181]), ("岳阳", city_value[182]), ("长沙", city_value[183]),
        ("衢州", city_value[184]), ("廊坊",city_value[185]), ("菏泽", city_value[186]), ("合肥", city_value[187]),
        ("武汉", city_value[188]), ("大庆", city_value[189])
    ]

    c = (
        Geo(init_opts=opts.InitOpts(width="1400px", height="700px", theme='dark'))  # 图表大小, 主题风格
            .add_schema(maptype="china",  # 地图
                        itemstyle_opts=opts.ItemStyleOpts(color="#28527a",  # 背景颜色
                                                  border_color="#9ba4b4"))  # 边框颜色, 可在 https://colorhunt.co/选择颜色
            .add(
            "",  # 系列名称, 可不设置
            [(i, j) for i, j in data],  # 数据
            type_=ChartType.EFFECT_SCATTER,  # 涟漪散点
            effect_opts=opts.EffectOpts(symbol_size=2), )  # 标记大小

            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 不显示标签
            .set_global_opts(title_opts=opts.TitleOpts(title="毕业生去向城市分布情况",  # 图表标题
                                                       pos_left='center',  # 标题位置
                                                       #subtitle='更新日期:2021-4-27',  # 副标题
                                                       #subtitle_link='http://tianqi.2345.com/air-rank.html' # 副标题链接
                                                       ),
                                                       visualmap_opts=opts.VisualMapOpts(max_=200,
                                                                                         range_text=['密度指数', ''],
                                                                                         # 上下的名称
                                                                                         split_number=4,
                                                                                         # 如果是连续数据, 分成几段
                                                                                         pos_left='20%',  # pos_right
                                                                                         pos_top='70%',  # pos_bottom
                                                                                         is_piecewise=True,  # 是否为分段显示
                                                                                         pieces=[{"min": 0, "max": 1,"color": "#32e0c4",'label': '少'},
                                                                                                 {"min": 2, "max": 5, "color": "#b8de6f",'label': '中'},
                                                                                                 {"min": 6,"max": 9, "color": "#fd8c04", 'label': '多'},
                                                                                                 {"min": 10,"max": 50,"color": "#ec5858",'label': '超多'}]                                                                                         )
                             )
            .render(r'C:\Users\Administrator\Desktop\VSS\vsapp\templates\visual\city_label.html')
    )




