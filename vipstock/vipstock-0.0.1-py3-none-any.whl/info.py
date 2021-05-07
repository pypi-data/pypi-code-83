#coding=utf-8

import re
# import logging
# logging.basicConfig(filename='logging.log',
#                     format='%(asctime)s %(message)s',
#                     filemode="w", level=logging.DEBUG)



loginParam={
    # 投资参考
    "inve": {
        "s_i": None,
        "s_a": None,
        "s_c": None,
        "s_t": None,
        "s_z": None,
        "symbol": None,
        "bdate": "2021-02-01",
        "edate": "2021-05-19",
        "jjnum": None,  # 限售解禁-解禁数量
        "order": None,
        "num": 600,
        "p": 1,
    },
    # 机构荐股池
    "rate": {
        "last": 10,
        "order": None,
        "num": 600,
        "p": 1,
    },
    # 龙虎榜
    "lhb": {
        "symbol": None,
        "bdate": "2021-02-01",
        "edate": "2021-05-19",
        "last": 10,
        "order": None,
        "num": 600,
        "p": 1,

    },
    # 市场表现
    "stat": {
        "node": "adr_hk",
        "asc": 1,
        "sort": "symbol",
        "num": 50,
        "page": 1,
    },
    # 财务分析
    "fina": {
        "s_i": "",
        "s_a": "",
        "s_c": "",
        "reportdate": 2020,
        "quarter": 4,
        "order": "roe|2",
        "num": 600,
        "p": 1,

    },
    # 业绩预测
    "pred": {
        "symbol": "sh600519",
        "orgname": "中金公司",
        "author": None,
        "order": "eps_p3|2",
        "num": 600,
        "p": 1,
    },
    # 机构持股
    "hold": {
        "symbol": "%D6%A4%C8%AF%BC%F2%B3%C6%BB%F2%B4%FA%C2%EB",
        "reportdate": 2021,
        "quarter": 1,
        "order": "num|2",        #  [num, numBalance, stockPercent, stockPercentBalance, currentStockPercent, currentPercentBalance]|[1, 2]
        "num": 600,
        "p": 1,
    },
    "detail": {
        "jgcg": {
            "symbol": "000521",
            "quarter": "20184",
        },
        "jjzc": {
            "orgtype": "fund",
            "symbol": "000521",
            "quarter": "20184",
        },
        "sbzc": {
            "orgtype": "socialSecurity",
            "symbol": "000521",
            "quarter": "20184",
        },
        "qfii": {
            "orgtype": "qfii",
            "symbol": "000521",
            "quarter": "20184",
        },
    },
    # 分析师排名
    "anal": {
        "year": 2020,
        "quarter": 1,
        "analyst": None,
        "industry": None,
        "period": None,
        "order": None,
        "num": 600,
        "p": 1,
    },
    # 投资评级选股
    "cust": {
        "market": "sh",
        "industry": "sw2_110300",
        "concept": "chgn_700004",
        "zone": "diyu_110000",
        "sr_p": 60,
        "rating": 10,
        "srating": 5,
        "sprice": 1,
        "order": None,
        "num": 600,
        "p": 1,
    },

    # 研报搜索
    "repo": {
        "symbol": None,
        "orgname": None,
        "industry": None,
        "analysts": None,
        "title": None,
        "pubdate": None,
        "t1": 1,
        "order": None,
        "num": 600,
        "p": 1,
    },

}

loginUrls =  {
    'proxyWeb': 'https://www.xicidaili.com/nn/',
    'proxies': {
        # "http": 'http://127.0.0.1:1080',
        "https": 'https://127.0.0.1:1080'
    },
    'host':'http://stock.finance.sina.com.cn',
    'url':'http://stock.finance.sina.com.cn',

    # 投资参考
    "inve": {
        "base": "http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/{}/index.phtml?",
        "交易提示": "jyts",
        "融资融券": "rzrq",
        "大宗交易": "dzjy",
        "内部交易": "nbjy",
        "限售解禁": "xsjj",
        "千股千评": "qgqp",
        "打新收益": "dxsy",
        "历史分红": "lsfh",
    },
    # 机构荐股池
    "rate": {
        "base": "http://stock.finance.sina.com.cn/stock/go.php/{}/index.phtml?",
        "最新投资评级": "vIR_RatingNewest",
        "上调评级股票": "vIR_RatingUp",
        "下调评级股票": "vIR_RatingDown",
        "股票综合评级": "vIR_SumRating",
        "首次评级股票": "vIR_RatingFirst",
        "目标涨幅排名": "vIR_SumPrice",
        "机构关注度": "vIR_OrgCare",
        "行业关注度": "vIR_IndustryCare",
        "投资评级选股": "vIR_CustomSearch",
        "个股投资评级": "vIR_StockSearch",
    },
    # 龙虎榜
    "lhb": {
        "base": "http://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/{}/index.phtml?",
        "每日详情": "lhb",
        "个股上榜统计": "ggtj",
        "营业部上榜统计": "yytj",
        "机构席位追踪": "jgzz",
        "机构席位成交明细": "jgmx",
    },
    # 市场表现
    "stat": {
        "base": "http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList/{}?",
        "阶段最高最低": "StatisticsService.getPeriodList",
        "盘中创新高个股": "StatisticsService.getNewHighList",
        "盘中创新低个股": "StatisticsService.getNewLowList",
        "成交骤增个股": "StatisticsService.getVolumeRiseList",
        "成交骤减个股": "StatisticsService.getVolumeReduceList",
        "连续放量个股": "StatisticsService.getVolumeRiseConList",
        "连续缩量个股": "StatisticsService.getVolumeReduceConList",
        "连续上涨个股": "StatisticsService.getStockRiseConList",
        "连续下跌个股": "StatisticsService.getStockReduceConList",
        "周涨跌排名": "StatisticsService.getSummaryWeekList",
        "一周强势股": "StatisticsService.getRiseWeekList",
        "月涨跌排名": "StatisticsService.getSummaryMonthList",
        "一月强势股": "StatisticsService.getRiseMonthList",
        "流通市值排行": "Market_Center.getHQNodeDataNew",
        "市盈率排行": "Market_Center.getHQNodeDataNew",
        "市净率排行": "Market_Center.getHQNodeDataNew",
    },
    # 财务分析
    "fina": {
        "base": "http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/{}/index.phtml?",
        "盈利能力": "profit",
        "营运能力": "operation",
        "成长能力": "grow",
        "偿债能力": "debtpaying",
        "现金流量": "cashflow",
        "业绩报表": "mainindex",
        "业绩预告": "performance",
        "业绩快报": "news",
        "利润细分": "incomedetail",
    },
    # 业绩预测
    "pred": {
        "base": "http://stock.finance.sina.com.cn/stock/go.php/vPerformancePrediction/kind/{}/index.phtml?",
        "每股收益预测": "eps",
        "营业收入预测": "sales",
        "净利润预测": "np",
        "净资产收益率预测": "roe",
    },
    # 机构持股
    "hold": {
        "base": "http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/{}/index.phtml?",
        "机构持股汇总": "jgcg",
        "基金重仓股": "jjzc",
        "社保重仓股": "sbzc",
        "QFII重仓股": "qfii",
    },
    "detail": {
        'jgcg': 'http://vip.stock.finance.sina.com.cn/q/api/jsonp.php/var%20details=/ComStockHoldService.getJGCGDetail?',
        'jjzc': 'http://vip.stock.finance.sina.com.cn/q/api/jsonp.php/var%20details=/ComStockHoldService.getJGBigHoldDetail?',
        'sbzc': 'http://vip.stock.finance.sina.com.cn/q/api/jsonp.php/var%20details=/ComStockHoldService.getJGBigHoldDetail?',
        'qfii': 'http://vip.stock.finance.sina.com.cn/q/api/jsonp.php/var%20details=/ComStockHoldService.getJGBigHoldDetail?',
    },
    # 分析师排名
    "anal": {
        "base": "http://vip.stock.finance.sina.com.cn/q/go.php/vAnalystRank/kind/{}/index.phtml?",
        "最佳选股分析师": "zjxg",
        "盈利预测最准分析师": "zzyc",
        "券商研究力量排行": "qsph",
    },

    # 投资评级选股
    "cust": {
        "base": "http://stock.finance.sina.com.cn/stock/go.php/{}/index.phtml?",
        "投资评级选股": "vIR_CustomSearch",
        "个股投资评级": "vIR_StockSearch",
    },
    # 个股数据下载
    "down": {
        "base": "http://money.finance.sina.com.cn/corp/go.php/vDOWN_{0}/displaytype/4/stockid/{1}/ctrl/all.phtml",
        "利润表": "ProfitStatement",
        "资产负债表": "BalanceSheet",
        "现金流量表": "CashFlow",
        "财务指标": "FinancialGuideLine",
        # "财务摘要": "FinanceSummary",
    },
    # issue搜索
    "issue": {
        "base": "https://money.finance.sina.com.cn/corp/go.php/{}/stockid/{}/ctrl/{}/displaytype/4.phtml",
        # 发行与分配
        "分红配股": ("vISSUE_ShareBonus", "sharebonus"),
        "增发": ("vISSUE_AddStock", "addStock"),
        "新股发行": ("vISSUE_NewStock", "comInfo"),
        "可转债发行": ("vISSUE_TransferableBond", "TransferableBond"),
        "募资投向": ("vISSUE_CollectFund", "collectFund"),
        "招股说明": ("vISSUE_RaiseExplanation", {'class': re.compile("table2")}),
        "上市公告": ("vISSUE_MarketBulletin", {'class': re.compile("table2")}),

        # 公司资料
        "公司简介": ("vCI_CorpInfo", "comInfo"),
        "公司高管": ("vCI_CorpManager", "comInfo"),
        "公司章程": ("vCI_CorpRule", "comInfo"),
        "相关证券": ("vCI_CorpXiangGuan", "Table"),
        "所属行业": ("vCI_CorpOtherInfo", {'class': re.compile("comInfo")}),
        "所属概念板块": ("vCI_CorpOtherInfo", {'class': re.compile("comInfo")}),
        # 股本股东
        "股本结构": ("vCI_StockStructure", "StockStructureNewTable"),
        "主要股东": ("vCI_StockHolder", "Table"),
        "流通股股东": ("vCI_CirculateStockHolder", "CirculateShareholderTable"),
        "基金持股": ("vCI_FundStockHolder", "FundHoldSharesTable"),
        "股东总数": ("amount", "Table"),
        "平均持股数": ("average", "Table"),
        # 财务数据
        "财务摘要": ("vFD_FinanceSummary", "FundHoldSharesTable"),
        "财务指标": ("vFD_FinancialGuideLine", "BalanceSheetNewTable"),
        "财务附注": ("vFD_FootNotes", "Table"),
        "资产负债表": ("vFD_BalanceSheet", "BalanceSheetNewTable"),
        "现金流量表": ("vFD_CashFlow", "ProfitStatementNewTable"),
        "利润表": ("vFD_ProfitStatement", "ProfitStatementNewTable"),
        "业绩预告": ("vFD_AchievementNotice", "Table1"),
        "股东权益增减": ("vFD_BenifitChange", "BenifitChangeNewTable"),


        # 重大事项
        "股东大会通知": ("vGP_StockHolderMeeting", "collectFund"),
        "违规记录": ("vGP_GetOutOfLine", "collectFund"),
        "诉讼仲裁": ("vGP_Lawsuit", "lawsuit"),
        "对外担保": ("vGP_Assurance", "assurance"),
        "关联交易": ("vGP_RelatedTrade", "collectFund"),
        # 财务附注
        "主要应收账款明细": ("vFD_FinanceSummary", "FundHoldSharesTable"),
        "存货明细": ("vFD_FinancialGuideLine", "BalanceSheetNewTable"),
        "应收账款账龄结构": ("vFD_BalanceSheet", "BalanceSheetNewTable"),
        "税率明细": ("vFD_CashFlow", "ProfitStatementNewTable"),
        "主营业务收入构成": ("vFD_ProfitStatement", "ProfitStatementNewTable"),
        "资产减值准备明细表": ("vFD_AssetDevalue", "BenifitChangeNewTable"),
        "应交增值税明细表": ("vFD_PayTax", "BenifitChangeNewTable"),

        # 资本运作
        "控股参股": ("vCO_HoldingCompany", "holdingcompany"),
        "参股券商": ("vCO_ShareStockbroker", ""),
        "资产托管": ("vCO_CapitalTrusteeship", ""),
        "资产置换": ("vCO_CapitalReplacement", ""),
        "资产交易": ("vCO_CapitalTrade", "collectFund"),
        "资产剥离": ("vCO_CapitalStrip", ""),


        # 资讯与公告
        "个股资讯": ("vCB_AllNewsStock", {'class': re.compile("table2")}),
        "行业资讯": ("stockIndustryNews", {'class': re.compile("table2")}),
        "公司公告": ("vCB_AllBulletin", {'class': re.compile("table2")}),
        "年度报告": ("vCB_Bulletin", ""),
        "中期报告": ("vCB_BulletinZhong", ""),
        "一季度报告": ("vCB_BulletinYi", ""),
        "三季度报告": ("vCB_BulletinSan", ""),
        "理财师解读": ("vCB_FinManDiv", ""),
        "公司号": ("vCB_AllNewsGSH", ""),


    },
    # 研报搜索
    "repo": {
        "base": "http://stock.finance.sina.com.cn/stock/go.php/vReport_List/kind/{}/index.phtml?",
        "研报搜索": "search",
        "公司研究": "company",
        "行业研究": "industry",
        "投资策略": "strategy",
        "宏观研究": "macro",
    },
    # "stat": {
    #     "base": "http://vip.stock.finance.sina.com.cn/datacenter/hqstat.html#{}",
    #     "阶段最高最低": "jdgd",
    #     "盘中创新高个股": "30xg",
    #     "盘中创新低个股": "30xd",
    #     "成交骤增个股": "cjzz",
    #     "成交骤减个股": "cjzj",
    #     "连续放量个股": "lxfl",
    #     "连续缩量个股": "lxsl",
    #     "连续上涨个股": "lxsz",
    #     "连续下跌个股": "lxxd",
    #     "周涨跌排名": "zzd",
    #     "一周强势股": "yzqs",
    #     "月涨跌排名": "yzd",
    #     "一月强势股": "yyqs",
    #     "流通市值排行": "ltsz",
    #     "市盈率排行": "sylv",
    #     "市净率排行": "sjlv",
    # },

}

loginHeaders = {

    "home":{
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "your cookie",
        "Host": "vip.stock.finance.sina.com.cn",
        "Referer": "http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"

    },
    "detail": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "your cookie",
        "Host": "vip.stock.finance.sina.com.cn",
        "Referer": "http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"

    },

}

loginMsg='''

Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: your cookie
Host: vip.stock.finance.sina.com.cn
Referer: http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml?symbol=%D6%A4%C8%AF%BC%F2%B3%C6%BB%F2%B4%FA%C2%EB&reportdate=2018&quarter=4
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36

'''

loginCookie=''
loginLang={'行业': '', '玻璃行业': 'new_blhy', '传媒娱乐': 'new_cmyl', '船舶制造': 'new_cbzz', '电力行业': 'new_dlhy', '电器行业': 'new_dqhy', '电子器件': 'new_dzqj', '电子信息': 'new_dzxx', '发电设备': 'new_fdsb', '纺织机械': 'new_fzjx', '纺织行业': 'new_fzhy', '飞机制造': 'new_fjzz', '服装鞋类': 'new_fzxl', '钢铁行业': 'new_gthy', '公路桥梁': 'new_glql', '供水供气': 'new_gsgq', '化工行业': 'new_hghy', '化纤行业': 'new_hqhy', '环保行业': 'new_hbhy', '机械行业': 'new_jxhy', '家电行业': 'new_jdhy', '家具行业': 'new_jjhy', '建筑建材': 'new_jzjc', '交通运输': 'new_jtys', '酒店旅游': 'new_jdly', '开发区': 'new_kfq', '煤炭行业': 'new_mthy', '摩托车': 'new_mtc', '酿酒行业': 'new_ljhy', '农林牧渔': 'new_nlmy', '农药化肥': 'new_nyhf', '汽车制造': 'new_qczz', '商业百货': 'new_sybh', '食品行业': 'new_sphy', '水泥行业': 'new_snhy', '塑料制品': 'new_slzp', '陶瓷行业': 'new_tchy', '物资外贸': 'new_wzwm', '医疗器械': 'new_ylqx', '仪器仪表': 'new_yqyb', '印刷包装': 'new_ysbz', '造纸行业': 'new_zzhy', '石油行业': 'new_syhy', '综合行业': 'new_zhhy', '金融行业': 'new_jrhy', '房地产': 'new_fdc', '其它行业': 'new_qtxy', '生物制药': 'new_swzz', '有色金属': 'new_ysjs', '地域': '', '新疆维吾尔自治区': 'diyu_650000', '宁夏回族自治区': 'diyu_640000', '青海省': 'diyu_630000', '甘肃省': 'diyu_620000', '陕西省': 'diyu_610000', '西藏自治区': 'diyu_540000', '云南省': 'diyu_530000', '贵州省': 'diyu_520000', '四川省': 'diyu_510000', '重庆市': 'diyu_500000', '海南省': 'diyu_460000', '广西壮族自治区': 'diyu_450000', '广东省': 'diyu_440000', '湖南省': 'diyu_430000', '湖北省': 'diyu_420000', '河南省': 'diyu_410000', '山东省': 'diyu_370000', '江西省': 'diyu_360000', '福建省': 'diyu_350000', '安徽省': 'diyu_340000', '浙江省': 'diyu_330000', '江苏省': 'diyu_320000', '上海市': 'diyu_310000', '黑龙江省': 'diyu_230000', '吉林省': 'diyu_220000', '辽宁省': 'diyu_210000', '内蒙古自治区': 'diyu_150000', '山西省': 'diyu_140000', '河北省': 'diyu_130000', '天津市': 'diyu_120000', '北京市': 'diyu_110000', '概念': '', '碳交易': 'gn_tjy', '科创50': 'gn_kc50', '光伏概念': 'gn_gfgn', '无线耳机': 'gn_wxej', '水产品': 'gn_scp1', '消费电子': 'gn_xfdz', '朝鲜改革': 'gn_cxgg', '垃圾分类': 'gn_ljfl', '含GDR': 'gn_hGDR', '氢能源': 'gn_qny', '华为概念': 'gn_hwgn', '百度概念': 'gn_bdgn', '小米概念': 'gn_xmgn', '仿制药': 'gn_fzy', '国防军工': 'gn_gfjg', '海南自贸': 'gn_hnzm', '腾讯概念': 'gn_txgn', '乡村振兴': 'gn_xczx', '5G概念': 'gn_5Ggn', 'IP变现': 'gn_IPbx', '军民融合': 'gn_jmrh', '可燃冰': 'gn_krb', '免疫治疗': 'gn_myzl', '雄安新区': 'gn_xaxq', '新零售': 'gn_xls', '智能电网': 'gn_zndw', '黄河三角': 'gn_hhsj', '海峡西岸': 'gn_hxxa', '成渝特区': 'gn_cytq', '铁路基建': 'gn_tljj', '物联网': 'gn_wlw', '军工航天': 'gn_jght', '黄金概念': 'gn_hjgn', '创投概念': 'gn_ctgn', 'ST板块': 'gn_stbk', '低碳经济': 'gn_dtjj', '含H股': 'gn_hHg', '含B股': 'gn_hBg', '次新股': 'gn_cxg', '含可转债': 'gn_hkzz', '稀缺资源': 'gn_xqzy', '融资融券': 'gn_rzrq', '三网融合': 'gn_swrh', '武汉规划': 'gn_whgh', '多晶硅': 'gn_djg', '锂电池': 'gn_ldc', '稀土永磁': 'gn_xtyc', '核电核能': 'gn_hdhn', '触摸屏': 'gn_cmp', '水利建设': 'gn_sljs', '长株潭': 'gn_czt', '皖江区域': 'gn_wjqy', '太阳能': 'gn_tyn', '卫星导航': 'gn_wxdh', '云计算': 'gn_yjs', '电子支付': 'gn_dzzf', '新三板': 'gn_xsb', '海工装备': 'gn_hgzb', '保障房': 'gn_bzf', '涉矿概念': 'gn_skgn', '金融改革': 'gn_jrgg', '页岩气': 'gn_yyq', '生物疫苗': 'gn_swym', '文化振兴': 'gn_whzx', '宽带提速': 'gn_kdts', 'IPV6概念': 'gn_IPV6gn', '食品安全': 'gn_spaq', '奢侈品': 'gn_scp', '图们江': 'gn_tmj', '三沙概念': 'gn_ssgn', '3D打印': 'gn_3Ddy', '海水淡化': 'gn_hsdh', '碳纤维': 'gn_txw', '地热能': 'gn_drn', '摘帽概念': 'gn_zmgn', '苹果概念': 'gn_pggn', '重组概念': 'gn_zzgn', '安防服务': 'gn_affw', '建筑节能': 'gn_jzjn', '智能交通': 'gn_znjt', '空气治理': 'gn_kqzl', '充电桩': 'gn_cdz', '4G概念': 'gn_4Ggn', '石墨烯': 'gn_smx', '风沙治理': 'gn_fszl', '土地流转': 'gn_tdlz', '聚氨酯': 'gn_jaz', '生物质能': 'gn_swzn', '东亚自贸': 'gn_dyzm', '丝绸之路': 'gn_sczl', '体育概念': 'gn_tygn', '博彩概念': 'gn_bcgn', 'O2O模式': 'gn_O2Oms', '特斯拉': 'gn_tsl', '生态农业': 'gn_stny', '水域改革': 'gn_sygg', '风能': 'gn_fn', '燃料电池': 'gn_rldc', '草甘膦': 'gn_cgl', '京津冀': 'gn_jjj', '粤港澳': 'gn_yga', '基因概念': 'gn_jygn', '阿里概念': 'gn_algn', '海上丝路': 'gn_hssl', '抗癌': 'gn_ka', '抗流感': 'gn_klg', '维生素': 'gn_wss', '农村金融': 'gn_ncjr', '汽车电子': 'gn_qcdz', '固废处理': 'gn_gfcl', '装饰园林': 'gn_zsyl', '赛马概念': 'gn_smgn', '猪肉': 'gn_zr', '节能': 'gn_jn', '污水处理': 'gn_wscl', '国产软件': 'gn_gcrj', '基因测序': 'gn_jycx', '电商概念': 'gn_dsgn', '基因芯片': 'gn_jyxp', '氢燃料': 'gn_sqrl', '国企改革': 'gn_sgqgg', '超导概念': 'gn_cdgn', '智能家居': 'gn_znjj', '蓝宝石': 'gn_lbs', '智能机器': 'gn_znjq', '机器人概念': 'gn_zjqrgn', '天津自贸': 'gn_mtjzm', '信息安全': 'gn_xxaq', '油气改革': 'gn_yqgg', '民营医院': 'gn_myyy', '养老概念': 'gn_ylgn', '民营银行': 'gn_myyx', '婴童概念': 'gn_ytgn', '广东自贸': 'gn_gzzm', '上海自贸': 'gn_shzm', '互联金融': 'gn_hljr', '网络游戏': 'gn_wlyx', '智能穿戴': 'gn_zncd', '前海概念': 'gn_qhgn', '绿色照明': 'gn_lszm', '风能概念': 'gn_fngn', '生物育种': 'gn_swyz', '内贸规划': 'gn_nmgh', '生物燃料': 'gn_swrl', '准ST股': 'gn_zSTg', '业绩预降': 'gn_yjyj', '业绩预升': 'gn_yjys', '送转潜力': 'gn_szql', '高校背景': 'gn_gxbj', '节能环保': 'gn_jnhb', '陕甘宁': 'gn_sgn', '自贸区': 'gn_zmq', '日韩贸易': 'gn_rhmy', '外资背景': 'gn_wzbj', '整体上市': 'gn_ztss', '本月解禁': 'gn_byjj', '金融参股': 'gn_jrcg', '社保重仓': 'gn_sbzc', '保险重仓': 'gn_bxzc', '信托重仓': 'gn_xtzc', '券商重仓': 'gn_qszc', 'QFII重仓': 'gn_QFIIzc', '精选指数': 'gn_jxzs', '分拆上市': 'gn_fcss', '超级细菌': 'gn_cjxj', '上海本地': 'gn_shbd', '深圳本地': 'gn_szbd', '振兴沈阳': 'gn_zxsy', '沿海发展': 'gn_yhfz', '央企50': 'gn_yq50', '超大盘': 'gn_cdp', '参股金融': 'gn_cgjr', '基金重仓': 'gn_jjzc', '股期概念': 'gn_gqgn', '股权激励': 'gn_gqjl', '甲型流感': 'gn_jxlg', '迪士尼': 'gn_dsn', '出口退税': 'gn_ckts', '新能源': 'gn_xny', '未股改': 'gn_wgg', '循环经济': 'gn_xhjj', '资产注入': 'gn_zczr', '市场': '', '沪市A股': 'sh_a', '沪市B股': 'sh_b', '深市A股': 'sz_a', '深市B股': 'sz_b', '多空建议': '', '买入': 'sz_1', '持有': 'sz_2', '观望': 'sz_3', '卖出': 'sz_4', '其他': 'sz_0'}
# loginLang={' 市场 ': '', '上海': 'sh', '深圳': 'sz', ' 行业 ': '', '种植业': 'sw2_110100', '渔业': 'sw2_110200', '林业': 'sw2_110300', '饲料': 'chgn_700744', '农产品加工': 'sw2_110500', '农业综合': 'sw2_110600', '畜禽养殖': 'sw2_110700', '动物保健': 'sw2_110800', '石油开采': 'sw2_210100', '煤炭开采': 'sw2_210200', '其他采掘': 'sw2_210300', '采掘服务': 'sw2_210400', '石油化工': 'sw2_220100', '化学原料': 'sw2_220200', '化学制品': 'sw2_220300', '化学纤维': 'sw2_220400', '塑料': 'sw2_220500', '橡胶': 'sw2_220600', '钢铁': 'sw2_230100', '金属非金属新材料': 'sw2_240200', '工业金属': 'sw2_240300', '黄金': 'sw2_240400', '稀有金属': 'sw2_240500', '半导体': 'chgn_700458', '元件': 'sw2_270200', '光学光电子': 'sw2_270300', '其他电子': 'sw2_270400', '电子制造': 'sw2_270500', '汽车整车': 'sw2_280100', '汽车零部件': 'chgn_700618', '汽车服务': 'sw2_280300', '其他交运设备': 'sw2_280400', '白色家电': 'sw2_330100', '视听器材': 'sw2_330200', '饮料制造': 'sw2_340300', '食品加工': 'sw2_340400', '纺织制造': 'sw2_350100', '服装家纺': 'sw2_350200', '造纸': 'sw2_360100', '包装印刷': 'sw2_360200', '家用轻工': 'sw2_360300', '其他轻工制造': 'sw2_360400', '化学制药': 'sw2_370100', '中药': 'chgn_700174', '生物制品': 'sw2_370300', '医药商业': 'sw2_370400', '医疗器械': 'chgn_700127', '医疗服务': 'sw2_370600', '电力': 'sw2_410100', '水务': 'sw2_410200', '燃气': 'sw2_410300', '环保工程及服务': 'sw2_410400', '港口': 'sw2_420100', '高速公路': 'sw2_420200', '公交': 'sw2_420300', '航空运输': 'sw2_420400', '机场': 'sw2_420500', '航运': 'sw2_420600', '铁路运输': 'sw2_420700', '物流': 'sw2_420800', '房地产开发': 'sw2_430100', '园区开发': 'chgn_700742', '贸易': 'sw2_450200', '一般零售': 'sw2_450300', '专业零售': 'sw2_450400', '商业物业经营': 'sw2_450500', '景点': 'sw2_460100', '酒店': 'sw2_460200', '旅游综合': 'sw2_460300', '餐饮': 'sw2_460400', '其他休闲服务': 'sw2_460500', '银行': 'sw2_480100', '证券': 'sw2_490100', '保险': 'sw2_490200', '多元金融': 'sw2_490300', '综合': 'sw2_510100', '水泥制造': 'sw2_610100', '玻璃制造': 'sw2_610200', '其他建材': 'sw2_610300', '房屋建设': 'sw2_620100', '装修装饰': 'sw2_620200', '基础建设': 'sw2_620300', '专业工程': 'sw2_620400', '园林工程': 'sw2_620500', '电机': 'sw2_630100', '电气自动化设备': 'sw2_630200', '电源设备': 'sw2_630300', '高低压设备': 'sw2_630400', '通用机械': 'sw2_640100', '专用设备': 'sw2_640200', '仪器仪表': 'sw2_640300', '金属制品': 'sw2_640400', '运输设备': 'sw2_640500', '航天装备': 'sw2_650100', '航空装备': 'sw2_650200', '地面兵装': 'sw2_650300', '船舶制造': 'sw2_650400', '计算机设备': 'sw2_710100', '计算机应用': 'sw2_710200', '文化传媒': 'sw2_720100', '营销传播': 'sw2_720200', '互联网传媒': 'sw2_720300', '通信运营': 'sw2_730100', '通信设备': 'sw2_730200', ' 地域 ': '', '北京市': 'diyu_110000', '天津市': 'diyu_120000', '河北省': 'diyu_130000', '山西省': 'diyu_140000', '内蒙古自治区': 'diyu_150000', '辽宁省': 'diyu_210000', '吉林省': 'diyu_220000', '黑龙江省': 'diyu_230000', '上海市': 'diyu_310000', '江苏省': 'diyu_320000', '浙江省': 'diyu_330000', '安徽省': 'diyu_340000', '福建省': 'diyu_350000', '江西省': 'diyu_360000', '山东省': 'diyu_370000', '河南省': 'diyu_410000', '湖北省': 'diyu_420000', '湖南省': 'diyu_430000', '广东省': 'diyu_440000', '广西壮族自治区': 'diyu_450000', '海南省': 'diyu_460000', '重庆市': 'diyu_500000', '四川省': 'diyu_510000', '贵州省': 'diyu_520000', '云南省': 'diyu_530000', '西藏自治区': 'diyu_540000', '陕西省': 'diyu_610000', '甘肃省': 'diyu_620000', '青海省': 'diyu_630000', '宁夏回族自治区': 'diyu_640000', '新疆维吾尔自治区': 'diyu_650000', ' 概念 ': '', 'H股': 'chgn_700002', '次新股': 'chgn_700004', '新材料': 'chgn_700008', '大盘': 'chgn_700014', '中盘': 'chgn_700015', '小盘': 'chgn_700016', '网络游戏': 'chgn_700021', '预盈预增': 'chgn_700023', '太阳能': 'chgn_700032', '新能源': 'chgn_700033', '铁路基建': 'chgn_700034', '新疆振兴': 'chgn_700050', '节能环保': 'chgn_700068', '物联网': 'chgn_700069', '航天军工': 'chgn_700071', '创投': 'chgn_700077', '电子支付': 'chgn_700080', '稀土永磁': 'chgn_700088', '核电': 'chgn_700089', '云计算': 'chgn_700090', '稀缺资源': 'chgn_700092', '融资融券': 'chgn_700095', 'LED': 'chgn_700096', '锂电池': 'chgn_700097', '水利建设': 'chgn_700098', '水泥': 'chgn_700099', '煤化工': 'chgn_700105', '黄金股': 'chgn_700107', '智能机器': 'chgn_700124', '特斯拉': 'chgn_700125', '抗癌药物': 'chgn_700126', '油气勘探': 'chgn_700128', '小金属': 'chgn_700129', '大数据': 'chgn_700130', '智慧城市': 'chgn_700131', '影视动漫': 'chgn_700132', '手游': 'chgn_700133', '网络安全': 'chgn_700135', '5G': 'chgn_700136', '储能': 'chgn_700137', '苹果三星': 'chgn_700140', '石墨烯': 'chgn_700141', '电子商务': 'chgn_700143', '安防': 'chgn_700145', 'PM2.5': 'chgn_700150', '海工装备': 'chgn_700151', '染料涂料': 'chgn_700154', '沪自贸区': 'chgn_700155', '彩票': 'chgn_700162', '污水处理': 'chgn_700165', '页岩气': 'chgn_700166', '二胎': 'chgn_700168', '通用航空': 'chgn_700170', '冷链物流': 'chgn_700173', '疫苗': 'chgn_700175', '上海国资': 'chgn_700176', '智能家居': 'chgn_700178', '智能汽车': 'chgn_700179', '白酒': 'chgn_700182', '在线教育': 'chgn_700185', '燃料电池': 'chgn_700186', '中石化系': 'chgn_700187', '智能手机': 'chgn_700188', '充电桩': 'chgn_700189', '北斗导航': 'chgn_700199', '央企改革': 'chgn_700200', '体育产业': 'chgn_700206', '互联医疗': 'chgn_700208', '工业4.0': 'chgn_700210', '基因测序': 'chgn_700211', '一带一路': 'chgn_700215', '证金汇金': 'chgn_700216', '虚拟现实': 'chgn_700219', '大飞机': 'chgn_700221', '增强现实': 'chgn_700224', '量子通信': 'chgn_700225', '无人驾驶': 'chgn_700226', '举牌': 'chgn_700227', '人脸识别': 'chgn_700228', '人工智能': 'chgn_700230', '区块链': 'chgn_700231', 'PPP概念': 'chgn_700232', 'OLED': 'chgn_700233', '昨日涨停': 'chgn_700234', '蚂蚁金服概念': 'chgn_700238', '股权转让': 'chgn_700272', '中字头': 'chgn_700274', '军民融合': 'chgn_700292', '京津冀': 'chgn_700294', '混改': 'chgn_700295', '雄安新区': 'chgn_700296', '粤港澳': 'chgn_700303', '电子竞技': 'chgn_700319', '高送转': 'chgn_700327', '国资改革': 'chgn_700338', '海南自贸区': 'chgn_700340', '健康中国': 'chgn_700352', '天然气': 'chgn_700400', '新能源车': 'chgn_700410', '民用航空': 'chgn_700445', '近端次新': 'chgn_700513', '阿里概念': 'chgn_700529', '港口运输': 'chgn_700530', 'MSCI中国': 'chgn_700532', '新零售': 'chgn_700539', '无人零售': 'chgn_700540', '房屋租赁': 'chgn_700544', '芯片概念': 'chgn_700579', '自由贸易港': 'chgn_700583', '家用电器': 'chgn_700592', '乡村振兴': 'chgn_700595', '旅游酒店': 'chgn_700596', '机械': 'chgn_700597', '小米概念': 'chgn_700600', '工业互联网': 'chgn_700602', '深圳国资': 'chgn_700605', '数字中国': 'chgn_700610', 'ST板块': 'chgn_700613', '知识产权': 'chgn_700614', '腾讯概念': 'chgn_700623', '广电系': 'chgn_700643', '期货概念': 'chgn_700644', '华为概念': 'chgn_700649', '设计咨询': 'chgn_700655', '高铁': 'chgn_700656', '油气改革': 'chgn_700657', '土地流转': 'chgn_700660', '特高压': 'chgn_700661', '边缘计算': 'chgn_700663', '新基建': 'chgn_700665', '光刻胶': 'chgn_700670', '柔性电子': 'chgn_700677', '金融科技': 'chgn_700680', '3D打印': 'chgn_700681', '互联金融': 'chgn_700682', '信托概念': 'chgn_700683', '超高清': 'chgn_700684', '长三角一体化': 'chgn_700686', '征信概念': 'chgn_700687', '智能电网': 'chgn_700688', '能源互联': 'chgn_700689', '电力物联网': 'chgn_700690', '数字孪生': 'chgn_700691', '电子烟': 'chgn_700693', '氢能源': 'chgn_700694', '工业大麻': 'chgn_700698', '流媒体': 'chgn_700701', '券商相关': 'chgn_700704', '超级真菌': 'chgn_700707', '富士康概念': 'chgn_700713', '猪肉概念': 'chgn_700716', '人造肉概念': 'chgn_700721', '种业': 'chgn_700722', '养鸡': 'chgn_700723', '草甘膦': 'chgn_700724', '啤酒': 'chgn_700728', '轮胎': 'chgn_700729', '生物农药': 'chgn_700731', '智慧农业': 'chgn_700732', '空客概念': 'chgn_700733', '华为海思': 'chgn_700734', '操作系统': 'chgn_700735', '海底光缆': 'chgn_700736', '集成电路': 'chgn_700737', '动物疫苗': 'chgn_700738', '电子化学品': 'chgn_700739', 'PCB概念': 'chgn_700740', '卫星互联网': 'chgn_700741', '大豆': 'chgn_700745', '休闲食品': 'chgn_700746', '足球概念': 'chgn_700747', '冰雪产业': 'chgn_700748', 'ETC概念': 'chgn_700749', '整车': 'chgn_700753', '国产乳业': 'chgn_700754', '中芯国际概念': 'chgn_700755', '养老产业': 'chgn_700756', '农机': 'chgn_700758', '东北振兴': 'chgn_700759', 'GDR概念': 'chgn_700761', '固废处理': 'chgn_700762', '垃圾发电': 'chgn_700763', '垃圾分类': 'chgn_700764', '壳资源': 'chgn_700766', '激光概念': 'chgn_700768', '氟化工': 'chgn_700769', '远洋运输': 'chgn_700772', '航母产业': 'chgn_700773', '金融机具': 'chgn_700774', '磷化工': 'chgn_700777', '金刚线': 'chgn_700778', '光通信': 'chgn_700779', '汽车电子': 'chgn_700780', '维生素': 'chgn_700781', '高校系': 'chgn_700782', '轨道交通': 'chgn_700783', '装配建筑': 'chgn_700784', '快递概念': 'chgn_700785', '甲醇概念': 'chgn_700786', '无人机': 'chgn_700787', '智能穿戴': 'chgn_700788', '消防概念': 'chgn_700789', '机器视觉': 'chgn_700790', '民爆': 'chgn_700791', '钛白粉': 'chgn_700792', '定制家居': 'chgn_700794', '地下管廊': 'chgn_700795', '智慧医疗': 'chgn_700796', '眼科概念': 'chgn_700797', '医用耗材': 'chgn_700798', '医药电商': 'chgn_700799', '血液制品': 'chgn_700800', '华为鲲鹏': 'chgn_700802', '钴镍': 'chgn_700803', '智慧停车': 'chgn_700804', '西部开发': 'chgn_700805', '地理信息': 'chgn_700806', '可燃冰': 'chgn_700807', '分拆概念': 'chgn_700808', '智慧物流': 'chgn_700809', '车联网': 'chgn_700810', '无线充电': 'chgn_700811', 'IP概念': 'chgn_700816', '数字货币': 'chgn_700817', '智能交通': 'chgn_700818', '手势识别': 'chgn_700819', '全息概念': 'chgn_700821', 'VPN概念': 'chgn_700822', '横琴新区': 'chgn_700823', '智慧政务': 'chgn_700824', '风能': 'chgn_700825', '跨境电商': 'chgn_700826', '腾讯云': 'chgn_700827', '智能音箱': 'chgn_700828', 'MLCC概念': 'chgn_700829', '医疗美容': 'chgn_700831', '网红经济': 'chgn_700832', '无线耳机': 'chgn_700833', '胎压监测': 'chgn_700837', '智能手表': 'chgn_700839', 'IPV6': 'chgn_700841', 'IGBT概念': 'chgn_700842', '应急管理': 'chgn_700843', '油气管网': 'chgn_700844', '光学': 'chgn_700845', '云游戏': 'chgn_700846', '指纹识别': 'chgn_700847', 'MLED': 'chgn_700848', '传感器': 'chgn_700849', '云视频': 'chgn_700851', '生物质能': 'chgn_700852', '转基因': 'chgn_700854', 'HIT电池': 'chgn_700855', '特种玻璃': 'chgn_700861', '大基金概念': 'chgn_700862', '知识付费': 'chgn_700863', '抗流感': 'chgn_700864', '可降解': 'chgn_700865', '口罩概念': 'chgn_700866', '病毒检测': 'chgn_700867', '体外诊断': 'chgn_700868', '在线办公': 'chgn_700869', '消毒概念': 'chgn_700870', '医废处理': 'chgn_700871', '砷化镓': 'chgn_700873', 'WIFI概念': 'chgn_700874', '氮化镓': 'chgn_700875', '生物安全': 'chgn_700876', '磷酸铁锂': 'chgn_700877', '盖板玻璃': 'chgn_700878', '存储器': 'chgn_700879', '蔚来汽车概念': 'chgn_700880', '网络营销': 'chgn_700881', 'IDC概念': 'chgn_700882', '防护服': 'chgn_700883', '呼吸机': 'chgn_700889', 'C2M概念': 'chgn_700891', '原料药': 'chgn_700893', 'RCS概念': 'chgn_700894', '熔喷布': 'chgn_700895', '油气存储': 'chgn_700896', '农村电商': 'chgn_700897', 'REITs概念': 'chgn_700899', '信创概念': 'chgn_700900', '送转填权': 'chgn_700903', '免税概念': 'chgn_700905', 'EDA概念': 'chgn_700906', '尾气处理': 'chgn_700907', '地摊经济': 'chgn_700908', '湖北自贸区': 'chgn_700910', '国六概念': 'chgn_700911', '京东概念': 'chgn_700912', '字节跳动概念': 'chgn_700913', '三板精选概念': 'chgn_700915', '食品检测': 'chgn_700916', '食药追溯': 'chgn_700917', '水产养殖': 'chgn_700918', '爱奇艺概念': 'chgn_700920', '拼多多概念': 'chgn_700921', '光电子': 'chgn_700922', '药用玻璃': 'chgn_700923', '寒武纪概念': 'chgn_700925', '海绵城市': 'chgn_700926', 'NMN概念': 'chgn_700927', '代糖概念': 'chgn_700930', '换电概念': 'chgn_700931', '汽车拆解': 'chgn_700932', '第三代半导体': 'chgn_700934', '宁德时代概念': 'chgn_700935', '光刻机': 'chgn_700936', '快充概念': 'chgn_700940', '快手概念': 'chgn_700941', '恒大汽车概念': 'chgn_700942', '化妆品': 'chgn_700943', '辅助生殖': 'chgn_700944', 'RCEP概念': 'chgn_700945', '有机硅': 'chgn_700946', '社区团购': 'chgn_700948', '疫苗运输': 'chgn_700949', '绿色包装': 'chgn_700950', '碳中和': 'chgn_700951', '中欧班列': 'chgn_700953', '茅概念': 'chgn_700954', '华为汽车': 'chgn_700955', '固态电池': 'chgn_700956', '折叠屏': 'chgn_700957', 'BIPV概念': 'chgn_700958', '特种气体': 'chgn_700959', '百度概念': 'chgn_700960', '生态园林': 'chgn_700961', '烟标': 'chgn_700964', '葡萄酒': 'chgn_700965', '电子车牌': 'chgn_700966', '核废处理': 'chgn_700967', '超大盘': 'chgn_700997', '退市警示': 'chgn_700998', 'ST股板块': 'chgn_700999', '合同能源': 'chgn_730006', '沪警示板': 'chgn_730010', '深ST板': 'chgn_730011', '迪士尼': 'chgn_730014', '土壤修复': 'chgn_730019', '丝绸之路': 'chgn_730025', '百货O2O': 'chgn_730027', '民营医院': 'chgn_730028', '生态农业': 'chgn_730030', '职业教育': 'chgn_730040', '细胞治疗': 'chgn_730043', '债转股': 'chgn_730053', '共享经济': 'chgn_730054', '雄安环保': 'chgn_730056', '雄安地产': 'chgn_730057', '雄安交运': 'chgn_730058', '雄安基建': 'chgn_730059', '雄安能化': 'chgn_730060', '雄安金融': 'chgn_730062', 'NFC概念': 'chgn_730065', '安徽国资': 'chgn_730066', '超级高铁': 'chgn_730069', '成渝城市群': 'chgn_730071', '磁悬浮': 'chgn_730073', '电改': 'chgn_730075', '电子发票': 'chgn_730076', '钒电池': 'chgn_730079', '福建自贸区': 'chgn_730081', '干细胞': 'chgn_730082', '供应链金融': 'chgn_730086', '骨传导概念': 'chgn_730087', '国产软件': 'chgn_730093', '海南国资': 'chgn_730095', '杭州亚运': 'chgn_730097', '航天航空': 'chgn_730098', '湖南国资': 'chgn_730099', '环球影城': 'chgn_730101', '嘉兴地区': 'chgn_730105', '教育产业': 'chgn_730106', '金融IC': 'chgn_730107', '精准医疗': 'chgn_730108', '喀什规划区': 'chgn_730110', '抗癌治癌': 'chgn_730111', '抗震防震': 'chgn_730112', '兰州自贸区': 'chgn_730114', '沥青概念': 'chgn_730116', '纳米概念': 'chgn_730119', '能源纸': 'chgn_730120', '农村电网': 'chgn_730123', '硼墨稀概念': 'chgn_730126', '平潭实验区': 'chgn_730127', '苹果产业链': 'chgn_730128', '汽车后市场': 'chgn_730130', '汽车金融': 'chgn_730131', '青蒿素': 'chgn_730132', '清洁能源': 'chgn_730134', '人脑工程': 'chgn_730135', '商业保理': 'chgn_730137', '生态林业': 'chgn_730138', '生物识别': 'chgn_730139', '生物医药': 'chgn_730141', '食品安全': 'chgn_730144', '水电': 'chgn_730146', '碳纤维': 'chgn_730150', '卫星导航': 'chgn_730155', '无锡国资委': 'chgn_730156', '谐振器': 'chgn_730159', '锌溴概念': 'chgn_730160', '信息安全': 'chgn_730163', '盐化工': 'chgn_730165', '液态金属': 'chgn_730166', '移动支付': 'chgn_730167', '乙肝疫苗': 'chgn_730169', '引力波': 'chgn_730170', '影视传媒': 'chgn_730171', '在线旅游': 'chgn_730174', '中概股回归': 'chgn_730180', '重工装备': 'chgn_730184', '重庆国改': 'chgn_730185', '舟山自贸区': 'chgn_730186', '富勒烯': 'chgn_730189', '超级电容': 'chgn_730190', '超导概念': 'chgn_730191', '锂硫电池': 'chgn_730192', 'SAAS': 'chgn_730195', 'AMC概念': 'chgn_730196', '三元锂电': 'chgn_730200', '电池管理': 'chgn_730203', 'GPU': 'chgn_730206', '陶瓷概念': 'chgn_730208', 'QLED': 'chgn_730209', '电动物流车': 'chgn_730210', '军工电子': 'chgn_730211', '兵装集团': 'chgn_730213', '环境监测': 'chgn_730214', '动力煤': 'chgn_730217', '智能电视': 'chgn_730218', '低碳经济': 'chgn_730220', '汽车轻量化': 'chgn_730223', '支付牌照': 'chgn_730224', '互联网家装': 'chgn_730229', '乙二醇': 'chgn_730236', '多晶硅': 'chgn_730237', '特种钢': 'chgn_730239', '互联网保险': 'chgn_730242', '镁空气电池': 'chgn_730244', '余热发电': 'chgn_730245', '钢铁互联网': 'chgn_730247', '单晶硅': 'chgn_730250', '锌电池': 'chgn_730252', '云印刷': 'chgn_730253', '禽流感药物': 'chgn_730256', '家具卫浴': 'chgn_730257', '单车概念': 'chgn_730258', '共享汽车': 'chgn_730259', '微信概念': 'chgn_730260', '兵工集团': 'chgn_730261', '摘帽概念': 'chgn_730263', '价值品牌': 'chgn_730266', '石家庄': 'chgn_730268', '数字丝绸': 'chgn_730270', '特色小镇': 'chgn_730275', '国机集团': 'chgn_730281', '复兴号': 'chgn_730282', '一线蓝筹': 'chgn_730285', '航天科技集团': 'chgn_730288', '航空工业集团': 'chgn_730289', '航天科工集团': 'chgn_730290', '新疆建设兵团': 'chgn_730294', '中国建材集团': 'chgn_730295', '大唐集团': 'chgn_730296', '中科院系': 'chgn_730297', '天津国资': 'chgn_730299', '针状焦': 'chgn_730300', '船舶重工集团': 'chgn_730301', '中核工业集团': 'chgn_730302', '船舶工业集团': 'chgn_730303', '中粮集团': 'chgn_730304', '江苏国资': 'chgn_730305', '福建国资': 'chgn_730306', '浙江国资': 'chgn_730307', '北京国资': 'chgn_730308', '广西国资': 'chgn_730309', '甘肃国资': 'chgn_730310', '西藏国资': 'chgn_730311', '国电集团': 'chgn_730312', '贵州国资': 'chgn_730313', '融资租赁': 'chgn_730316', '山西国资': 'chgn_730317', '深汕合作区': 'chgn_730318', '全面屏': 'chgn_730319', '金属铝': 'chgn_730320', '盐湖提锂': 'chgn_730321', '价值成长': 'chgn_730325', '360概念': 'chgn_730326', '覆铜板': 'chgn_730327', '工程机械': 'chgn_730332', '网络直播': 'chgn_730333', '6G概念': 'chgn_730337', '无感支付': 'chgn_730340', '仿制药': 'chgn_730341', '赛马概念': 'chgn_730342', '短视频': 'chgn_730343', '青岛': 'chgn_730344', '世界杯': 'chgn_730345', '网易概念': 'chgn_730348', '中化集团': 'chgn_730349', '中国化工集团': 'chgn_730350', '脸书概念': 'chgn_730355', '进博会概念': 'chgn_730356', '谷歌概念': 'chgn_730357', '美团概念': 'chgn_730359', '富时罗素概念': 'chgn_730362', '麻醉概念': 'chgn_730366', '芬太尼概念': 'chgn_730367', '广东国资': 'chgn_730376', '增持回购': 'chgn_730378', '供销社概念': 'chgn_730382', '网络切片': 'chgn_730384', '铌概念': 'chgn_730385', '纳米银线': 'chgn_730387', '华为电视': 'chgn_730388', '天文观测': 'chgn_730392', '央企金控': 'chgn_730394', '内容审核': 'chgn_730395', '透明工厂': 'chgn_730397', '国资入股': 'chgn_730402', '态势感知': 'chgn_730403', '黑龙江自贸区': 'chgn_730404', '零售药店': 'chgn_730405', '超宽带': 'chgn_730409', '阿尔茨海默': 'chgn_730411', 'TOF概念': 'chgn_730412', 'LCP概念': 'chgn_730414', '铰链': 'chgn_730415', '参股新三板': 'chgn_730417', '网格化管理': 'chgn_730418', '独角兽概念': 'chgn_730419', '头盔概念': 'chgn_730423', '盲盒概念': 'chgn_730425', '中国电科集团': 'chgn_730426', '抖音小店': 'chgn_730427', '高送转预期': 'chgn_730429', '京东数科概念': 'chgn_730430', '虚拟电厂': 'chgn_730431', '城市大脑': 'chgn_730432', '风沙治理': 'chgn_730433', '肝素': 'chgn_730434'}