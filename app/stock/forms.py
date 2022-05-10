from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired
from app.models import goods, supplier, User, power, client, duty, section, warehouse


class AddStockForm(FlaskForm):
    code = StringField(
        label="股票代码",
        validators=[
            DataRequired()
        ],
        description="股票代码",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入股票代码！",
        }
    )
    name = StringField(
        label="股票名称",
        validators=[
            DataRequired()
        ],
        description="股票名称",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入股票名称！",
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )
