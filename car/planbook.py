#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd


x = [{'name':'abjiankangjiaren','com':1},
{'name':'abjiankangkangyingerhao','com':1},
{'name':'abjiankangzhijiadingqi','com':1},
{'name':'abjiankangzhijiazhongshen','com':1},
{'name':'abjiankangzhixiang','com':1},
{'name':'abjiankangzhixing','com':1},
{'name':'abjiankangzhizundingqi','com':1},
{'name':'abjiankangzhizunzhongshen','com':1},
{'name':'anbangGroup_1','com':1},
{'name':'abrsjiujiufangai','com':1},
{'name':'anbangrsGroup_1','com':1},
{'name':'abylbanganda','com':1},
{'name':'anbangylGroup_1','com':1},
{'name':'bhrslulubao','com':1},
{'name':'bohairsGroup_1','com':1},
{'name':'changshengrsGroup_1','com':1},
{'name':'csrsailibaoexingzhongliu','com':1},
{'name':'fdsmkangjianwuyoua','com':1},
{'name':'fdsmkangjianwuyoub','com':1},
{'name':'fudeshengmingGroup_1','com':1},
{'name':'gongyinanshengGroup_1','com':1},
{'name':'gyasbaiwanbaojia','com':1},
{'name':'glgerenyiwaishanghai','com':1},
{'name':'guolianGroup_1','com':1},
{'name':'fangaixian','com':1},
{'name':'gsjincaimingtiana','com':1},
{'name':'gsjincaimingtianb','com':1},
{'name':'gskangningbaobei','com':1},
{'name':'gskangningdingqi2013','com':1},
{'name':'gskangningdingqi2013b','com':1},
{'name':'gskangningdingqi433','com':1},
{'name':'gskangningzhongshen432','com':1},
{'name':'gsxiangruizhongshen','com':1},
{'name':'gsxiangyuedingqi','com':1},
{'name':'gsxinliangquana','com':1},
{'name':'gsxinliangquanb','com':1},
{'name':'gsxinliangquanc','com':1},
{'name':'gsxinliangquand','com':1},
{'name':'guoshouGroup_1','com':1},
{'name':'ruixin2013','com':1},
{'name':'ruixinDC','com':1},
{'name':'ruyisuixing','com':1},
{'name':'xinfuyishengv2','com':1},
{'name':'halaonianfangaixian','com':1},
{'name':'henganbzGroup_1','com':1},
{'name':'hdhengjiujiankang','com':1},
{'name':'hdxinfunianjin','com':1},
{'name':'hengdaGroup_1','com':1},
{'name':'hhjjjiankangzhixiang','com':1},
{'name':'honghaojjGroup_1','com':1},
{'name':'hkrsjiankangyishenga','com':1},
{'name':'hongkangrsGroup_1','com':1},
{'name':'hhhuikangchengxiang','com':1},
{'name':'huahuirsGroup_1','com':1},
{'name':'huaxiaGroup_1','com':1},
{'name':'hxfulinmen','com':1},
{'name':'jiaoyinklGroup_1','com':1},
{'name':'jyklyuedongrensheng','com':1},
{'name':'jixiangrsGroup_1','com':1},
{'name':'jxmeimanankang','com':1},
{'name':'jkrsjiaotongyiwaic','com':1},
{'name':'junkangrsGroup_1','com':1},
{'name':'kljkchangshoubao','com':1},
{'name':'kunlunjkGroup_1','com':1},
{'name':'larsanhaoyisheng','com':1},
{'name':'lianrsGroup_1','com':1},
{'name':'paanxingbao','com':1},
{'name':'pabeixiangfu','com':1},
{'name':'pachuangketie','com':1},
{'name':'pajinxinli','com':1},
{'name':'pajinxinsheng','com':1},
{'name':'papinganfuv5','com':1},
{'name':'paxinliv3','com':1},
{'name':'paxinxiangv3','com':1},
{'name':'pinganGroup_1','com':1},
{'name':'qhrsxiaoxinbao','com':1},
{'name':'qianhairsGroup_1','com':1},
{'name':'rbjkbeizhongfangaib','com':1},
{'name':'rbjkfuzeyisheng','com':1},
{'name':'renbaojkGroup_1','com':1},
{'name':'rbsbaiwanshenjia','com':1},
{'name':'rbsjinsetongnian','com':1},
{'name':'rbsxinxiangzhizun','com':1},
{'name':'renbaoshouGroup_1','com':1},
{'name':'rtkangtaijinsheng','com':1},
{'name':'ruitairsGroup_1','com':1},
{'name':'taikangGroup_1','com':1},
{'name':'tkquannengbaobeia','com':1},
{'name':'tkquannengbaobeibaozhangjihua','com':1},
{'name':'tkrseshengjiankang','com':1},
{'name':'taipingGroup_1','com':1},
{'name':'tpanyingtaiping','com':1},
{'name':'tpebaobei','com':1},
{'name':'tpfulubeizhidingqi','com':1},
{'name':'tpfulubeizhizhongshen','com':1},
{'name':'tpjinwuyou_fulubeizhi','com':1},
{'name':'tpquanwuyouv2','com':1},
{'name':'tpxiaoxinbao','com':1},
{'name':'kuaileCZB','com':1},
{'name':'taipingyangGroup_1','com':1},
{'name':'tpyaiwuyouv2','com':1},
{'name':'tpyanxingbao2','com':1},
{'name':'tpyjinyourensheng','com':1},
{'name':'tpyjinyourenshengdiancang','com':1},
{'name':'tpylexiangankanga','com':1},
{'name':'tpymantanghong','com':1},
{'name':'tpyshouhuankanga','com':1},
{'name':'tpyxinanyi','com':1},
{'name':'tpyzhuangyuanhongzxb','com':1},
{'name':'xhchangxingwuyou2015','com':1},
{'name':'xinhuaGroup_1','com':1},
{'name':'baiwanrensheng','com':1},
{'name':'qianwanchuancheng','com':1},
{'name':'xintaiGroup_1','com':1},
{'name':'xthengtaizhongji','com':1},
{'name':'muyingjibingbx','com':1},
{'name':'ydanxiangtaihe','com':1},
{'name':'yingdaGroup_1','com':1},
{'name':'ybjinyouhuixuan','com':1},
{'name':'youbangGroup_1','com':1},
{'name':'zhonghuaGroup_1','com':1},
{'name':'zhrsankang','com':1},
{'name':'zhongrongGroup_1','com':1},
{'name':'zrbaobeiwuyou','com':1},
{'name':'zhongyiGroup_1','com':1},
{'name':'zyiyishengbao','com':1},
{'name':'aixiangsui','com':1},
{'name':'aixiangsuizxb','com':1},
{'name':'zhongyingGroup_1','com':1},
{'name':'zyshouhuyisheng','com':1},
{'name':'zyshouhuyishengzxb','com':1},
{'name':'zyxinxiangnianhua','com':1},
{'name':'zhongyoursGroup_1','com':1},
{'name':'zyrsniannianhaobaibeibao','com':1}]

y=[{"typeId":1,"name": "xinruyi"},
 {"typeId":2,"name": "xinkangning"},
 {"typeId":3,"name": "fangaixian"},
 {"typeId":4,"name": "ruixin"},
 {"typeId":44,"name": "daruixin"},
 {"typeId":378,"name": "ruixindiancangban"},
 {"typeId":5,"name": "hongyunshaoer"},
 {"typeId":7,"name": "fuluxinzun"},
 {"typeId":8,"name": "fuxinshaoer"},
 {"typeId":15,"name": "jinyourensheng"},
 {"typeId":33,"name": "yingcaishaoer"},
 {"typeId":36,"name": "fulujinzun"},
 {"typeId":40,"name": "songheyinian"},
 {"typeId":9,"name": "zunyurensheng"},
 {"typeId":10,"name": "pinganfu"},
 {"typeId":100,"name": "pinganfu_v2"},
 {"typeId":115,"name": "pinganfu_v2r2"},
 {"typeId":167,"name": "pinganfu_v3"},
 {"typeId":190,"name": "pinganfu_v4"},
 {"typeId":168,"name": "ruyisuixing"},
 {"typeId":34,"name": "fulushuangxi"},
 {"typeId":35,"name": "xiaosamingtian"},
 {"typeId":23,"name": "fushouniannian"},
 {"typeId":29,"name": "fulumantang"},
 {"typeId":30,"name": "yangyanghong"},
 {"typeId":218,"name": "newyangyanghong"},
 {"typeId":38,"name": "xinliliangquan"},
 {"typeId":171,"name": "xinliliangquanv2"},
 {"typeId":37,"name": "shijixinguang"},
 {"typeId":42,"name": "xinsheng"},
 {"typeId":101,"name": "xinsheng_v2"},
 {"typeId":182,"name": "xinsheng_v3"},
 {"typeId":43,"name": "jinruyi"},
 {"typeId":16,"name": "laolaifu"},
 {"typeId":17,"name": "shaonianzhi"},
 {"typeId":18,"name": "zhuoyueyouxiang"},
 {"typeId":19,"name": "fuyoujinsheng"},
 {"typeId":24,"name": "kanglerensheng"},
 {"typeId":25,"name": "ruyijinkang"},
 {"typeId":31,"name": "kangai"},
 {"typeId":26,"name": "quanyouyisheng"},
 {"typeId":12,"name": "jincai"},
 {"typeId":13,"name": "jiankangfuxing"},
 {"typeId":14,"name": "kangji"},
 {"typeId":20,"name": "kangyirenshen"},
 {"typeId":210,"name": "quanshunbao"},
 {"typeId":21,"name": "changyinrenshen"},
 {"typeId":27,"name": "fuguihuakai"},
 {"typeId":28,"name": "shengshiniannian"},
 {"typeId":46,"name": "yinfaankang"},
 {"typeId":47,"name": "fuyouankang"},
 {"typeId":50,"name": "kangjianchangqing"},
 {"typeId":53,"name": "quannengbao"},
 {"typeId":11,"name": "shouhuxing"},
 {"typeId":102,"name": "shouhuxing_v2"},
 {"typeId":120,"name": "chuangfuyihao"},
 {"typeId":22,"name": "fulinmen"},
 {"typeId":6,"name": "fumanyisheng"},
 {"typeId":169,"name": "changxingwuyounew"},
 {"typeId":48,"name": "changxingwuyou"},
 {"typeId":49,"name": "anxingbao"},
 {"typeId":41,"name": "zhihuixing"},
 {"typeId":45,"name": "jixiangka"},
 {"typeId":51,"name": "zhishengrensheng"},
 {"typeId":32,"name": "aijiabao"},
 {"typeId":54,"name": "kangshouchangle"},
 {"typeId":55,"name": "bojinxinruyi"},
 {"typeId":39,"name": "hushenfu"},
 {"typeId":56,"name": "quanwuyou"},
 {"typeId":57,"name": "yuexiangjinsheng"},
 {"typeId":60,"name": "changbaofuxing"},
 {"typeId":61,"name": "changbaoankang"},
 {"typeId":59,"name": "anjiabao"},
 {"typeId":58,"name": "xhshenshiyingjia"},
 {"typeId":62,"name": "tpshengshiyingjia"},
 {"typeId":65,"name": "baiwanjianianhua"},
 {"typeId":70,"name": "baiwancaifu"},
 {"typeId":63,"name": "xinanyi"},
 {"typeId":76,"name": "gsfulumantang"},
 {"typeId":66,"name": "jinseqiancheng"},
 {"typeId":347,"name": "jinseqianchengv2"},
 {"typeId":75,"name": "xianghewanjia"},
 {"typeId":64,"name": "kangyijinsheng"},
 {"typeId":68,"name": "shouhuyisheng"},
 {"typeId":77,"name": "anxingwuyou"},
 {"typeId":74,"name": "xinxiangrensheng"},
 {"typeId":85,"name": "zunyangwuyou"},
 {"typeId":86,"name": "fuxiangsui"},
 {"typeId":83,"name": "kangjianhuarui"},
 {"typeId":94,"name": "jiankangfuxiang"},
 {"typeId":95,"name": "furudonghaia"},
 {"typeId":96,"name": "furudonghai"},
 {"typeId":71,"name": "baiwankangtai"},
 {"typeId":67,"name": "yangguangtianshi"},
 {"typeId":78,"name": "fulubaobao"},
 {"typeId":79,"name": "kangningdingqi"},
 {"typeId":80,"name": "kangheng"},
 {"typeId":81,"name": "changqingshu"},
 {"typeId":82,"name": "fuguixinyu"},
 {"typeId":87,"name": "anxinwuyou"},
 {"typeId":437,"name": "gsanxinwuyou"},
 {"typeId":98,"name": "aisuixing"},
 {"typeId":128,"name": "aisuixingb"},
 {"typeId":97,"name": "xiaoshunbao"},
 {"typeId":99,"name": "huiminfushou"},
 {"typeId":104,"name": "zhinengxin"},
{"typeId":241,"name": "zhinengxinv2"},
 {"typeId":103,"name": "zunxiangrensheng"},
 {"typeId":106,"name": "xinhuahuikang"},
 {"typeId":107,"name": "baiwanrenwoxing"},
 {"typeId":114,"name": "fuxiangyisheng"},
 {"typeId":202,"name": "fuxiangyishengv2"},
 {"typeId":113,"name": "fuxiangyishengtp"},
 {"typeId":108,"name": "chengzhangkuaile"},
 {"typeId":110,"name": "zhizunfulinmen"},
 {"typeId":413,"name":"hxfulinmen"},
 {"typeId":117,"name": "quannengbaoc"},
 {"typeId":105,"name": "pazhiyuerensheng"},
 {"typeId":220,"name": "zhiyuerenshengv2"},
 {"typeId":116,"name": "fulijiankangplus"},
 {"typeId":111,"name": "liyingniannian"},
 {"typeId":121,"name": "hxhushenfu"},
 {"typeId":132,"name": "jiankangyisheng"},
 {"typeId":133,"name": "fuludizeng"},
 {"typeId":136,"name": "kangyouyisheng"},
 {"typeId":139,"name": "ankangzhuyuan"},
 {"typeId":147,"name": "anxiangzhuyuan"},
 {"typeId":122,"name": "ydbaiwancaifu"},
 {"typeId":130,"name": "meiliyisheng"},
 {"typeId":142,"name": "baobaoankang"},
 {"typeId":144,"name": "yongyouzhongji"},
 {"typeId":542,"name": "tpylexiangankanga"},
 {"typeId":112,"name": "lexiangankang"},
 {"typeId":118,"name": "xinxiangliangquan"},
 {"typeId":173,"name": "xinxiangliangquanv2"},
 {"typeId":131,"name": "wuyouyisheng"},
 {"typeId":137,"name": "jingxiuqiancheng"},
 {"typeId":140,"name": "dingqishouxian"},
 {"typeId":141,"name": "fuxiangankang"},
 {"typeId":143,"name": "baojiahuhang"},
 {"typeId":148,"name": "baiwananxing"},
 {"typeId":154,"name": "yinfawuyou"},
 {"typeId":156,"name": "jiankangwuyouc"},
 {"typeId":160,"name": "xinyibao"},
 {"typeId":145,"name": "jingcairensheng"},
 {"typeId":134,"name": "jixiangankang"},
 {"typeId":151,"name": "bnchangxingliangquan"},
 {"typeId":150,"name": "xingfudingqi"},
 {"typeId":162,"name": "jiankangwuyou_a"},
{"typeId":163,"name": "jiankangwuyou_b"},
 {"typeId":184,"name": "jiankangwuyoub_v2"},
 {"typeId":153,"name": "lexiangfuv2"},
 {"typeId":304,"name": "lexiangfuv3"},
 {"typeId":152,"name": "hzdayingjia"},
 {"typeId":157,"name": "baiwansuixing"},
 {"typeId":161,"name": "aiwuyou"},
 {"typeId":170,"name": "bjjincaiyisheng"},
 {"typeId":165,"name": "shengshiliannian"},
 {"typeId":174,"name": "tpxinyueyisheng"},
 {"typeId":119,"name": "xingfua"},
 {"typeId":176,"name": "jingxilianlian"},
 {"typeId":186,"name": "jingxilianlian_v2"},
 {"typeId":189,"name": "kangningbaobei"},
 {"typeId":177,"name": "payiwai2013"},
 {"typeId":187,"name": "pashijitianshi"},
 {"typeId":193,"name": "zunhongrensheng"},
 {"typeId":194,"name": "caifuzunyao"},
 {"typeId":195,"name": "kangaiwuyou"},
 {"typeId":196,"name": "huixinbao"},
 {"typeId":198,"name": "xinfuniannian"},
 {"typeId":200,"name": "yuanhongb"},
 {"typeId":179,"name": "jiankangwuyouc_v2"},
 {"typeId":158,"name": "baiwanhehu"},
 {"typeId":180,"name": "fuguimantang"},
 {"typeId":181,"name": "jiankangfuxing_v2"},
 {"typeId":183,"name": "jincaiyisheng_v2"},
 {"typeId":175,"name": "yishiankang"},
 {"typeId":185,"name": "shouhutianshi"},
 {"typeId":197,"name": "lexingwuyou"},
 {"typeId":201,"name": "xingfuxiangban"},
 {"typeId":203,"name": "changxiangshijia"},
 {"typeId":204,"name": "meihaoshenghuo"},
 {"typeId":206,"name": "yingjuyisheng"},
 {"typeId":208,"name": "xingfu2"},
 {"typeId":209,"name": "chuangfurensheng"},
 {"typeId":205,"name": "meihaoshenghuob"},
 {"typeId":207,"name": "jinmanfu"},
 {"typeId":214,"name": "shouhuankang"},
 {"typeId":211,"name": "guanaijiankangfangai"},
 {"typeId":212,"name": "jincainianhua_a"},
 {"typeId":213,"name": "jincainianhua_b"},
 {"typeId":216,"name": "fumanrensheng"},
 {"typeId":219,"name": "meimanyisheng"},
 {"typeId":222,"name": "kangjianyisheng"},
 {"typeId":221,"name": "yishenghehu"},
 {"typeId":223,"name": "yulifangsanhao"},
 {"typeId":227,"name": "ankangfurui"},
 {"typeId":226,"name": "yishengbao"},
 {"typeId":225,"name": "xinxiangshenghuo"},
 {"typeId":228,"name": "xinyuexing"},
 {"typeId":224,"name": "fuguixinsheng"},
 {"typeId":231,"name": "jianlilai"},
 {"typeId":232,"name": "yongtaiyisheng_a"},
{"typeId":233,"name": "yongtaiyisheng_b"},
 {"typeId":229,"name": "fuduoduo"},
 {"typeId":234,"name": "annuofangai"},
 {"typeId":235,"name": "bainiankangshun"},
 {"typeId":236,"name": "shengshijinxiang"},
 {"typeId":230,"name": "hushenfu2015"},
 {"typeId":237,"name": "shenglangkangjian"},
 {"typeId":238,"name": "zhongyingyihao"},
 {"typeId":138,"name": "caifuzunxiang"},
 {"typeId":240,"name": "fangaixianv2"},
 {"typeId":242,"name": "mantanghong"},
 {"typeId":244,"name": "jinshenghengying"},
 {"typeId":243,"name": "zhuangyuanhong"},
 {"typeId":247,"name": "changqingshu2016"},
 {"typeId":245,"name": "aixinsuixing"},
 {"typeId":246,"name": "anxiang"},
 {"typeId":250,"name": "fuxiangyishengtpv2"},
 {"typeId":248,"name": "lexingbao"},
 {"typeId":251,"name": "hushenfuV2"},
 {"typeId":264,"name": "kangyunyisheng"},
 {"typeId":265,"name": "kangshining"},
 {"typeId":262,"name": "leankang"},
 {"typeId":266,"name": "shouhuxingv3"},
 {"typeId":263,"name": "kangshunyisheng"},
 {"typeId":272,"name": "yilupingan"},
 {"typeId":267,"name": "shijixingguangv2"},
 {"typeId":273,"name": "anjubao"},
 {"typeId":292,"name": "nvxingjiankangfangai"},
 {"typeId":298,"name": "zhenaixingfu"},
 {"typeId":299,"name": "xinfuyisheng"},
 {"typeId":380,"name": "xinfuyishengv2"},
 {"typeId":301,"name": "kangyueyiliao"},
 {"typeId":414,"name": "tpkangyueyiliao"},
 {"typeId":302,"name": "fushouankang"},
 {"typeId":303,"name": "shaoerpinganfu"},
 {"typeId":308,"name": "cuicanrensheng"},
 {"typeId":428,"name": "tkcuicanrensheng"},
 {"typeId":309,"name": "aiziyou"},
 {"typeId":315,"name": "deyijinjia"},
 {"typeId":319,"name": "jiankangwuyouyounga"},
 {"typeId":320,"name": "jiankangwuyouyoungb"},
 {"typeId":321,"name": "jiankangwuyouyoungc"},
 {"typeId":323,"name": "lejubao"},
 {"typeId":326,"name": "xiaokangzhijia"},
 {"typeId":327,"name": "caifuwenying"},
{"typeId":412,"name": "tpcaifuwenyingnj"},
 {"typeId":328,"name": "jiankangyijiayi"},
 {"typeId":331,"name": "wenyingrensheng"},
 {"typeId":333,"name": "zunyirensheng"},
 {"typeId":286,"name": "hengyingyisheng"},
 {"typeId":297,"name": "ankangyisheng"},
 {"typeId":316,"name": "caifutong"},
 {"typeId":322,"name": "yiluyangguang"},
 {"typeId":332,"name": "fujiaankang"},
 {"typeId":337,"name": "aibeijia"},
 {"typeId":336,"name": "xingtianxia"},
 {"typeId":345,"name": "zongheyiwai"},
 {"typeId":349,"name": "zijinzhanghuanquan"},
{"typeId":350,"name": "zijinzhanghuanquan"},
 {"typeId":359,"name": "jiankangbaifenbaia"},
{"typeId":360,"name": "jiankangbaifenbaib"},
 {"typeId":361,"name": "jiankangyishengv2"},
 {"typeId":343,"name": "jiankangyibai"},
 {"typeId":344,"name": "baiwanaijia"},
 {"typeId":351,"name": "xintaibaiwanhehu"},
 {"typeId":358,"name": "huaxiazhuangyuanhong"},
  {"typeId":376,"name": "jianxinlongxinglexiang"},
 {"typeId":375,"name": "eaijiayanglaowuyou"},
 {"typeId":381,"name": "zgrskangningwanneng"},
 {"typeId":385,"name": "xtfuguiniannian"},
 {"typeId":388,"name": "tpjinwuyou"},
 {"typeId":389,"name": "tpshengshijinzun"},
 {"typeId":377,"name": "baiwanjiankang"},
 {"typeId":379,"name": "xfrsxingfurensheng"},
 {"typeId":386,"name": "tarsjiankangyuan"},
 {"typeId":387,"name": "xhyishengwuyou"},
 {"typeId":394,"name": "tpbaiwanjianianhuabv2"},
 {"typeId":52,"name": "combinePlanBookGS"},
 {"typeId":395,"name": "combinePlanBookTP"},
 {"typeId":84,"name": "combinePlanBookXH"},
 {"typeId":403,"name": "tpyshaoerchaonengbao"},
 {"typeId":453,"name": "tpyxiangningxingfubao"},
 {"typeId":409,"name": "tatianfuyisheng"},
 {"typeId":422,"name": "ydshaoerzhuyuan"},
 {"typeId":406,"name": "tkxinruirensheng"},
 {"typeId":423,"name": "tkyinianqichaonengbao"},
{"typeId":401,"name": "tkmenzhenzhuyuanxian"},
 {"typeId":411,"name": "tpxinyueyishi"},
 {"typeId":398,"name": "tkyuexiangzhonghua"},
 {"typeId":410,"name": "zyaiwuyou"},
 {"typeId":419,"name": "xhduobeibaoyoung"},
 {"typeId":420,"name": "xhduobeibaoman"},
 {"typeId":431,"name": "gskangningzhongshen"},
 {"typeId":436,"name": "tajingcairensheng"},
 {"typeId":451,"name": "xhjiankangwuyouc"},
 {"typeId":445,"name": "xhchangxingwuyou2015"},
 {"typeId":442,"name": "xhkangjianjishun"},
 {"typeId":441,"name": "gsruixin2013"},
 {"typeId":452,"name": "fangaixian"},
 {"typeId":432,"name": "pajinxinli"},
 {"typeId":433,"name": "pajinxinsheng"},
 {"typeId":507,"name": "paanxingbao"},
 {"typeId":458,"name": "zyyishengbao2016"},
 {"typeId":425,"name": "jxlongxingfugui"},
 {"typeId":461,"name": "xtqianwanchuancheng"},
 {"typeId":459,"name": "tpykuailechengzhangbao"},
 {"typeId":88,"name": "combinePlanBookTPY"},
 {"typeId":496,"name": "tpyjinyourensheng"},
 {"typeId":497,"name": "tpyzhuangyuanhongzxb"},
 {"typeId":498,"name": "tpymantanghong"},
 {"typeId":499,"name": "tpyxinanyi"},
 {"typeId":457,"name": "ruixindiancangban"},
 {"typeId":469,"name": "gsjincaimingtiana"},
 {"typeId":470,"name": "gsjincaimingtianb"},
 {"typeId":460,"name": "ruyisuixing"},
 {"typeId":456,"name": "zyaixiangsui"},
 {"typeId":471,"name": "zyaixiangsuizxb"},
 {"typeId":467,"name": "xtbaiwanrensheng"},
 {"typeId":462,"name": "xthengtaizhongji"},
 {"typeId":465,"name": "ydanxiangtaihe"},
 {"typeId":466,"name": "ydmuyingjibingbx"},
 {"typeId":468,"name": "hdxinfunianjin"},
 {"typeId":472,"name": "zyshouhuyisheng"},
 {"typeId":473,"name": "zyshouhuyishengzxb"},
 {"typeId":475,"name": "zyxinxiangnianhua"},
 {"typeId":487,"name": "gsxiangruizhongshen"},
 {"typeId":485,"name": "tpyanxingbao2"},
 {"typeId":495,"name": "zyiyishengbao"},
 {"typeId":488,"name": "gsxiangyuedingqi"},
 {"typeId":479,"name": "abjiankangjiaren"},
 {"typeId":491,"name": "abjiankangzhixiang"},
 {"typeId":492,"name": "abjiankangzhizundingqi"},
 {"typeId":493,"name": "abjiankangzhizunzhongshen"},
 {"typeId":536,"name": "abjiankangkangyingerhao"},
 {"typeId":481,"name": "gsxinliangquana"},
 {"typeId":482,"name": "gsxinliangquanb"},
 {"typeId":483,"name": "gsxinliangquanc"},
 {"typeId":484,"name": "gsxinliangquand"},
 {"typeId":477,"name": "abjiankangzhijiadingqi"},
 {"typeId":478,"name": "abjiankangzhijiazhongshen"},
 {"typeId":516,"name": "rbjkbeizhongfangaib"},
 {"typeId":510,"name": "hkrsjiankangyishenga"},
 {"typeId":503,"name": "gskangningbaobei"},
 {"typeId":504,"name": "abjiankangzhixing"},
 {"typeId":505,"name": "zhrsankang"},
 {"typeId":511,"name": "hhhuikangchengxiang"},
 {"typeId":490,"name": "kljkchangshoubao"},
 {"typeId":512,"name": "bhrslulubao"},
 {"typeId":513,"name": "abylbanganda"},
 {"typeId":524,"name": "rbsxinxiangzhizun"},
 {"typeId":509,"name": "glgerenyiwaishanghai"},
 {"typeId":519,"name": "tpfulubeizhizhongshen"},
 {"typeId":520,"name": "tpfulubeizhidingqi"},
 {"typeId":515,"name": "pachuangketie"},
 {"typeId":514,"name": "jxmeimanankang"},
 {"typeId":523,"name": "pabeixiangfu"},
 {"typeId":525,"name": "gskangningdingqi2013b"},
 {"typeId":526,"name": "gskangningdingqi2013"},
 {"typeId":527,"name": "tpxiaoxinbao"},
 {"typeId":529,"name": "halaonianfangaixian"},
 {"typeId":384,"name": "rbjkfuzeyisheng"},
 {"typeId":528,"name": "rtkangtaijinsheng"},
 {"typeId":531,"name": "tpjinwuyou_fulubeizhi"},
 {"typeId":543,"name": "tpebaobei"},
 {"typeId":501,"name": "tkrseshengjiankang"},
 {"typeId":532,"name": "gskangningdingqi433"},
 {"typeId":533,"name": "gskangningzhongshen432"},
 {"typeId":538,"name": "ybjinyouhuixuan"},
 {"typeId":541,"name": "abrsjiujiufangai"},
 {"typeId":534,"name": "csrsailibaoexingzhongliu"},
 {"typeId":535,"name": "jyklyuedongrensheng"},
 {"typeId":540,"name": "jkrsjiaotongyiwaic"},
 {"typeId":544,"name": "zrbaobeiwuyou"},
 {"typeId":556,"name": "tpquanwuyouv2"},
 {"typeId":546,"name": "tpyshouhuankanga"},
 {"typeId":548,"name": "tpyjinyourenshengdiancang"},
 {"typeId":549,"name": "rbsbaiwanshenjia"},
 {"typeId":561,"name": "rbsjinsetongnian"},
 {"typeId":562,"name": "fdsmkangjianwuyoua"},
 {"typeId":563,"name": "fdsmkangjianwuyoub"},
 {"typeId":550,"name": "tkquannengbaobeia"},
 {"typeId":553,"name": "qhrsxiaoxinbao"},
 {"typeId":551,"name": "tkquannengbaobeibaozhangjihua"},
 {"typeId":552,"name": "hdhengjiujiankang"},
 {"typeId":554,"name": "zyrsniannianhaobaibeibao"},
 {"typeId":555,"name": "larsanhaoyisheng"},
{"typeId":558,"name": "hhjjjiankangzhixiang"},
 {"typeId":557,"name": "paxinliv3"},
 {"typeId":566,"name": "tpanyingtaiping"},
 {"typeId":565,"name": "tpyaiwuyouv2"},
 {"typeId":559,"name": "papinganfuv5"}]

if __name__ == '__main__':


    px = pd.DataFrame(data=x,columns=['name','com'])



    py = pd.DataFrame(data=y,columns=['typeId','name'])


    result = py.merge(px,left_on='name', right_on='name',how='left',sort='typeId')
    result = result.fillna({'com': 0})

    result.to_csv("typeid.csv")

    # d = py.merge(px,left_on='name',how='left')
    # d = py.merge(px,left_on='c',how='left')
    # df = d[d['d'].str.contains(r'^甘.$')].sort(column='d')
    # print result


