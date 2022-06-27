import json
import requests
import os


from app.admin.views import admin_login_req
from flask import render_template, make_response, session, jsonify, request, flash, Response

from app.apps import db
from app.stock import stocks




# 首页
from app.stockModels import StockBasicInfo, StockDetail, MeiTanExtend, DazongUrls, Article

os.environ['NO_PROXY'] = 'stock.xueqiu.com'
cookie = 'device_id=f151c5de00dec3c0f2a3201d7f0276c7; remember=1; xq_is_login=1; u=2607199115; Hm_lvt_1db88642e346389874251b5a1eded6e3=1654867631,1655122160,1655282728,1655456667; xq_a_token=efe4b6fd1b31b1d36307ea45891fa7adb0bd84b1; xqat=efe4b6fd1b31b1d36307ea45891fa7adb0bd84b1; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjI2MDcxOTkxMTUsImlzcyI6InVjIiwiZXhwIjoxNjU4MDU5ODQ4LCJjdG0iOjE2NTU0Njc4NDgxMzcsImNpZCI6ImQ5ZDBuNEFadXAifQ.cvzQAkVTrbJARP-zDOGwy57ogVfQHdJtCSXBeXGkUZ_5o_i5bUZtG--EEHQGS_BUlNuWHENlmyK8cvdr0TtRKLppT3vb0mJnTaqvhzVmiDWs-fk12NxWw9eWX9A46nCLH6rPTH-4Xoqg_gUHEGsN-WZ4LRB9xqMb_5qjrgs3lOjkSsCzXBynwQsh3JHreJlIXirpTYWkAc3zPoyyyYlkCR02eeCHdhOmnTG2BtcbJvbAWzRCFzI0noAo4IlcnWhR7LKk8b2XYecoEhqRp_CYX2ftIcWuCty47ZNaOaAI2Ex0_VlWn6L_TjyKcSc3o2_Ki9j57CVKueSzvgHtES86-g; xq_r_token=d22456c31b20a468aeb03305447f991a27b3da53; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1655467849'

@stocks.route("/")
@admin_login_req
def index():
    return render_template("stock/index.html",name=session["admin"])

#跳转页——煤炭板块页
@stocks.route("/stockBasicInfo/",methods=["GET"])
@admin_login_req
def stockBasicInfo():
    bankuai = request.args.get('bankuai')
    print(bankuai)
    if bankuai == 'meitan':
        return render_template("stock/meitanbankuai.html",bankuai = bankuai)
    else :
        return render_template("stock/stander.html",bankuai = bankuai)

#AJAX--煤炭板块页——股票信息
@stocks.route("/stockInfos/<bankuai>",methods=["GET","POST"])
@admin_login_req
def stockInfos(bankuai):

    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    start = str((page - 1) * limit)
    limit = str(limit)
    count = 0;

    countsql = "select count(*) as count from sa_stockbasicinfo a left join sa_maitan_extend b on  a.code=b.code where enable = 1 and bankuai = " + "'" + bankuai +"'";
    print(countsql)
    ret0 = db.session.execute(countsql);
    for l in ret0:
        count = l[0]

    sql ="select a.code,a.name,a.price,a.pe,a.pb,b.chanliang,b.channeng from sa_stockbasicinfo a left join sa_maitan_extend b on  a.code=b.code where enable = 1 and bankuai = '" + bankuai +"'" +"limit " + start + "," + limit ;
    ret = db.session.execute(sql);
    print(ret)
    datalist = [];
    for ll in list(ret):
        datalist.append({
            'name': ll[1],
            'code':ll[0],
            'price':ll[2],
            'pe':ll[3],
            'pb':ll[4],
            'chanliang':ll[5],
            'channeng':ll[6]
        })
    # page_data = StockBasicInfo.query.filter_by(enable = 1)
    # for item in page_data :

    data = json.dumps({"data":datalist,"count":count,"code":0,"msg":""})

    return data




# 表单：添加股票   ajax接口
@stocks.route("/addStock/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def addStock():
    code = request.form.get('code');
    name = request.form.get('name');
    bankuai = request.form.get('bankuai');

    if code.startswith("6"):
        code = "SH" + code
    else:
        code = "SZ" + code



    stock = StockBasicInfo.query.filter_by(code=code).first();
    if stock is None:
        stock = StockBasicInfo(
            name=name,
            code=code,
            bankuai=bankuai
        )
    stock.enable=1
    db.session.add(stock)
    db.session.commit()
    return json.dumps({"status":"ok"})

@stocks.route("/deleteStock/",methods=["POST"],strict_slashes=False)
@admin_login_req
def deleteStock():
    # data = request.get_data(as_text=True)
    # aaa = StockInfo.query.filter_by(code = code).first();
    # print(aaa.name)
    code  = request.form.get('code')
    StockBasicInfo.query.filter_by(code = code).update({'enable':0});
    db.session.commit();
    return json.dumps({"status":"ok"})


@stocks.route("/updateStock/",methods=["POST"],strict_slashes=False)
@admin_login_req
def updateStock():
    code = request.form.get('code');
    pe = request.form.get('pe');
    price = request.form.get('price');
    name = request.form.get('name');
    pb = request.form.get('pb');
    chanliang = request.form.get('chanliang');
    channeng = request.form.get('channeng');
    if chanliang is None or len(chanliang)==0:
        chanliang = 0
    if channeng is None or len(channeng) == 0:
        channeng = 0

    stock = StockBasicInfo.query.filter_by(code=code).first();
    stock.pe = pe;
    stock.pb = pb;
    stock.name = name;
    stock.price = price;
    stock.code = code;

    extend = MeiTanExtend.query.filter_by(code=code).first();
    if extend is not None :
        extend.chanliang = chanliang;
        extend.channeng = channeng;
    else :
        extend = MeiTanExtend(
            code=code,
            chanliang=chanliang,
            channeng=channeng
        )

    db.session.add(stock);
    db.session.add(extend);
    db.session.commit();
    return json.dumps({"status":"ok"})


@stocks.route("/stockDetail/<code>/<name>",methods=["GET"])
@admin_login_req
def stockDetail(code,name):
    stocks = StockDetail.query.filter_by(code = code).all();
    s = StockBasicInfo.query.filter_by(code = code).first();
    nextseq = len(stocks) + 1
    return render_template("stock/stockDetail.html",stocks=stocks,code=code,name=name,nextseq=nextseq,relatedStocks=s.relatedStock)


@stocks.route("/stockContentEdit/<code>/<name>/<seq>",methods=["GET"])
@admin_login_req
def stockDetailContentEdit(code,name,seq):
    stockDetail = StockDetail.query.filter_by(code=code,seq=seq).first();
    if stockDetail is not None:
        title = stockDetail.title;
        content = stockDetail.content;
    if stockDetail is None:
        title = "请输入标题"
        content = "请输入内容"
    return render_template("stock/stockContentEdit.html", title=title,code=code,name=name,seq=seq,content=content)


#返回 股票文章ajax接口
@stocks.route("/stockContent/<code>/<seq>",methods=["GET"])
@admin_login_req
def stockContent(code,seq):
    detail = StockDetail.query.filter_by(code = code,seq=seq).first();
    if(detail is None):
        return json.dumps({"status": "none"});
    else:
        return json.dumps({"status": "ok","content":detail.content,"title":detail.title});


@stocks.route("/stockform/",methods=["GET"])
@admin_login_req
def stockform():
    return render_template("stock/form.html")




# 添加 编辑股票文章  ajax接口
@stocks.route("/addStockContent/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def addStockContent():
    code = request.form.get('code');
    name = request.form.get('name');
    content = request.form.get('content');
    title = request.form.get('title');
    seq = request.form.get('seq');
    stock = StockDetail.query.filter_by(code=code,seq=seq).first()
    if stock is None :
        stock = StockDetail(
            name=name,
            code=code,
            content=content,
            title=title,
            seq=seq,
        )
    stock.content = content
    stock.title = title
    db.session.add(stock)
    db.session.commit()
    return json.dumps({"status":"ok"})



@stocks.route("/stockAutoCompletes/",methods=["GET","POST"])
@admin_login_req
def stockAutoCompletes():

    keyword = request.form.get('search')
    print(keyword)

    sql = "select a.name,a.code from sa_stockbasicinfo a  where name like '%" + keyword + "%'";
    print(sql)
    ret = db.session.execute(sql);

    datalist = [];
    for ll in list(ret):
        datalist.append({
            'name':ll[1] ,
            'code':ll[0]
        })

    print(datalist)
    data = json.dumps({"data":datalist,"code":200})

    return data

@stocks.route("/addRelatedStock/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def addRelatedStock():

    name = request.form.get('name')#关联股票的名称
    code = request.form.get('code')#原来股票的code
    #跟进股票名称查询关联股票的code
    relatedStock = StockBasicInfo.query.filter_by(name=name).first()
    if relatedStock is None :
        return json.dumps({"status":"error"});
    else:
        stock = StockBasicInfo.query.filter_by(code=code).first()
        rstock = name + '-' + relatedStock.code;
        if stock.relatedStock is None or len(stock.relatedStock) == 0:
            stock.relatedStock = rstock
        else:
            stock.relatedStock = stock.relatedStock + "," + rstock
        db.session.add(stock)
        db.session.commit()
        return json.dumps({"status": "ok","code":relatedStock.code});

@stocks.route("/delRelatedStock/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def delRelatedStock():

    name = request.form.get('name')#关联股票的名称
    code = request.form.get('code')#关联股票的code
    orgcode = request.form.get('orgcode')#原来股票的code

    stock = StockBasicInfo.query.filter_by(code=orgcode).first() #原来股票的信息
    rstock = name + '-' + code;

    relatedStockList = stock.relatedStock.split(",")
    print(relatedStockList)
    print(len(relatedStockList))

    for i in range(0, len(relatedStockList)):
        if relatedStockList[i] == rstock:
            del relatedStockList[i]
            break
    stock.relatedStock=','.join(relatedStockList)

    db.session.add(stock)
    db.session.commit()
    return json.dumps({"status": "ok"});


#获取关联股票
@stocks.route("/getRelatedStocks/<code>",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def getRelatedStocks(code):

    #先获取该股票的信息
    stock = StockBasicInfo.query.filter_by(code=code).first()

    datalist = [];
    datalist1 = [];
    if stock.relatedStock is not None and len(stock.relatedStock) != 0:
        stocks = stock.relatedStock
        ss = stocks.split(",")
        for ll in ss :
            info = ll.split("-")
            datalist1.append({
                info[1]
            })
        stocks1 = StockBasicInfo.query.filter(StockBasicInfo.code.in_(datalist1)).all()
        for s in stocks1:
            datalist.append({
                'name': s.name,
                'code': s.code,
                'price': s.price,
                'pe': s.pe,
                'pb': s.pb
            })

    print(datalist)
    return json.dumps({"code": 0,"data":datalist});


@stocks.route("/updateCaiwu/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def updateCaiWu():

    #bankuai = request.form.get('bankuai')
    stocks = StockBasicInfo.query.filter_by().all()

    for stock in stocks:
        code = stock.code
        print(code)
        headers = {"upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
        headers['cookie'] = cookie
        headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        headers['accept-encoding'] = 'gzip, deflate, br'
        headers['cache-control'] = 'max-age=0'
        headers['Connection'] = 'keep-alive'
        headers['upgrade-insecure-requests'] = '1'

        url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=" + code + "&extend=detail"
        r1 = requests.get(url=url, headers=headers)
        if r1 is not None:
            print(r1.text)
            result = json.loads(r1.text)
            current = result['data']['quote']['current']
            pe_ttm = result['data']['quote']['pe_ttm']
            pb = result['data']['quote']['pb']

            stock.pb=pb
            stock.pe=pe_ttm
            stock.price=current

            db.session.add(stock)
            db.session.commit()


    return json.dumps({"status": "ok"});
















#大宗
#跳转页——煤炭板块页
@stocks.route("/dazongindex/",methods=["GET"])
@admin_login_req
def dazongindex():
    return render_template("stock/dazongindex.html")


@stocks.route("/dazongUrls",methods=["GET"])
@admin_login_req
def dazongUrls():
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    start = str((page - 1) * limit)
    limit = str(limit)
    count = 0;

    countsql = "select count(*) as count from sa_dazong_urls a  where enable = 1 ";
    ret0 = db.session.execute(countsql);
    for l in ret0:
        count = l[0]

    sql = "select a.title,a.url,a.remarks from sa_dazong_urls a  where enable = 1 "  + " limit " + start + "," + limit;
    ret = db.session.execute(sql);
    print(ret)
    datalist = [];
    for ll in list(ret):
        datalist.append({
            'title': ll[0],
            'url': ll[1],
            'remark': ll[2]
        })


    data = json.dumps({"data": datalist, "count": count, "code": 0, "msg": ""})

    return data

@stocks.route("/addDazongUrl/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def addDazongUrl():
    title = request.form.get('title');
    url = request.form.get('url');
    remarks = request.form.get('remarks');

    dazongurl = DazongUrls.query.filter_by(url=url).first();
    if dazongurl is None:
        dazongurl = DazongUrls(
            title=title,
            url=url,
            remarks=remarks
        )
    dazongurl.enable=1
    db.session.add(dazongurl)
    db.session.commit()
    return json.dumps({"status":"ok"})

@stocks.route("/deleteDazongUrl/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def deleteDazongUrl():
    url = request.form.get('url');
    dazongurl = DazongUrls.query.filter_by(url=url).first();
    print(dazongurl)
    db.session.delete(dazongurl)
    db.session.commit()
    return json.dumps({"status":"ok"})



@stocks.route("/addArticle/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def addArticle():
    title = request.form.get('title');
    bankuai = request.form.get('bankuai');
    remarks = request.form.get('remarks');
    content = request.form.get('content');
    relatedStocks = request.form.get('relatedStocks');
    id = request.form.get('id');

    article = Article.query.filter_by(id=id).first();

    #第一次添加
    if article is None:
        article = Article(
            title=title,
            bankuai=bankuai
        )

    #更新内容
    if content is not None and len(content) != 0 and title is not None and len(title) != 0 and article is not None:
        article.title=title
        article.content=content

    #更新其他字段
    if article is not None and content is None:
        article.title = title
        article.remarks = remarks
        article.relatedStocks = relatedStocks

    db.session.add(article)
    db.session.commit()
    return json.dumps({"status":"ok"})


#AJAX--煤炭板块页——股票信息
@stocks.route("/articles/<bankuai>",methods=["GET","POST"])
@admin_login_req
def articles(bankuai):

    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    start = str((page - 1) * limit)
    limit = str(limit)
    count = 0;

    countsql = "select count(*) as count from sa_bankuai_article a where  bankuai = " + "'" + bankuai +"'";
    print(countsql)
    ret0 = db.session.execute(countsql);
    for l in ret0:
        count = l[0]

    sql ="select a.title,a.remarks,a.relatedStocks ,a.id from sa_bankuai_article a  where bankuai = '" + bankuai +"'" +"limit " + start + "," + limit ;
    ret = db.session.execute(sql);
    print(ret)
    datalist = [];
    for ll in list(ret):
        datalist.append({
            'title': ll[0],
            'remarks':ll[1],
            'relatedStocks':ll[2],
            'id':ll[3]
        })

    data = json.dumps({"data":datalist,"count":count,"code":0,"msg":""})

    return data

@stocks.route("/deleteArticle/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def deleteArticle():
    title = request.form.get('title');
    article = Article.query.filter_by(title=title).first();
    print(article)
    db.session.delete(article)
    db.session.commit()
    return json.dumps({"status":"ok"})


@stocks.route("/articleContentEdit/<title>",methods=["GET"])
@admin_login_req
def articleContentEdit(title):
    article = Article.query.filter_by(title=title).first();
    return render_template("stock/articleContentEdit.html", id=article.id,title=article.title,content=article.content)


@stocks.route("/articleContent/<title>",methods=["GET"])
@admin_login_req
def articleContent(title):
    article = Article.query.filter_by(title=title).first();
    return render_template("stock/articleContent.html", article=article)