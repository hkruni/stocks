import json

from app.admin.views import admin_login_req
from flask import render_template, make_response, session, jsonify, request, flash

from app.apps import db
from app.stock import stocks




# 首页
from app.stock.forms import AddStockForm
from app.stockModels import StockBasicInfo, StockDetail, MeiTanExtend


@stocks.route("/")
@admin_login_req
def index():
    return render_template("stock/index.html",name=session["admin"])

#跳转页——煤炭板块页
@stocks.route("/stockBasicInfo/",methods=["GET","POST"])
@admin_login_req
def stockBasicInfo():
    return render_template("stock/meitanbankuai.html")


#AJAX--煤炭板块页——股票信息
@stocks.route("/stockInfos/",methods=["GET","POST"])
@admin_login_req
def stockInfos():

    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    start = str((page - 1) * limit)
    limit = str(limit)

    count = 0;

    countsql = "select count(*) as count from sa_stockbasicinfo a left join sa_maitan_extend b on  a.code=b.code where enable = 1";
    ret0 = db.session.execute(countsql);
    for l in ret0:
        count = l[0]

    sql ="select a.code,a.name,a.price,a.pe,a.pb,b.chanliang,b.channeng from sa_stockbasicinfo a left join sa_maitan_extend b on  a.code=b.code where enable = 1 limit " + start + "," + limit ;
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
    nextseq = len(stocks) + 1
    return render_template("stock/stockDetail.html",stocks=stocks,code=code,name=name,nextseq=nextseq)


@stocks.route("/stockContentEdit/<code>/<name>/<seq>",methods=["GET"])
@admin_login_req
def stockDetailContentEdit(code,name,seq):
    return render_template("stock/stockContentEdit.html", code=code,name=name,seq=seq)


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


# 表单：添加股票   ajax接口
@stocks.route("/addStock/",methods=["GET","POST"],strict_slashes=False)
@admin_login_req
def addStock():
    code = request.form.get('code');
    name = request.form.get('name');
    stock = StockBasicInfo(
        name=name,
        code=code,
        enable=1
    )
    db.session.add(stock)
    db.session.commit()
    return json.dumps({"status":"ok"})


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



