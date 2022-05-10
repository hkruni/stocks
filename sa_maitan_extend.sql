/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : sale

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2022-05-10 23:01:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sa_maitan_extend
-- ----------------------------
DROP TABLE IF EXISTS `sa_maitan_extend`;
CREATE TABLE `sa_maitan_extend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` char(8) DEFAULT NULL,
  `chanliang` int(11) DEFAULT NULL,
  `channeng` int(11) DEFAULT NULL,
  `beizhu` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of sa_maitan_extend
-- ----------------------------
INSERT INTO `sa_maitan_extend` VALUES ('1', '000001', '45', '78', null);

-- ----------------------------
-- Table structure for sa_stockbasicinfo
-- ----------------------------
DROP TABLE IF EXISTS `sa_stockbasicinfo`;
CREATE TABLE `sa_stockbasicinfo` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `code` char(8) NOT NULL,
  `name` char(6) NOT NULL,
  `price` char(6) DEFAULT NULL,
  `pe` char(6) DEFAULT NULL,
  `pb` char(6) DEFAULT NULL,
  `enable` int(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of sa_stockbasicinfo
-- ----------------------------
INSERT INTO `sa_stockbasicinfo` VALUES ('1', '000001', '中国平安', '55.8', '12', '3.5', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('2', '000002', '中国神华', '30.05', '25', '2.5', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('3', '000003', '贵州茅台', '35.00', '12.9', '25', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('4', '000004', '五粮液', '100.35', '26.8', '3.6', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('5', '000005', '宁德时代', '400.28', '26', '21', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('6', '000006', '招商银行', '35', '23', '12.12', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('7', '000007', '万华化学', '46', '17', '3', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('8', '000008', '工商银行', '4.78', '5.1', '3', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('9', '000009', '比亚迪', '256', '345.9', '5.8', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('10', '000010', '格力电器', '29.89', '23', '3.8', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('11', '000011', '隆基股份', '78', '45', '3.9', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('12', '300000', '阳光电源', '56', '100.98', '6.1', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('13', '300001', '金风科技', '15.01', '11', '3', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('14', '000035', '潍柴动力', '11.87', '13.1', '1.8', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('15', '000335', '三一重工', '13.1', '11.1', '2.5', '1');
INSERT INTO `sa_stockbasicinfo` VALUES ('16', '600000', '中国银行', '16.7', '5', '0.8', '1');

-- ----------------------------
-- Table structure for sa_stockdetail
-- ----------------------------
DROP TABLE IF EXISTS `sa_stockdetail`;
CREATE TABLE `sa_stockdetail` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `code` char(6) NOT NULL,
  `name` char(6) NOT NULL,
  `content` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of sa_stockdetail
-- ----------------------------
INSERT INTO `sa_stockdetail` VALUES ('1', '000001', '000001', '<p>55555555555555</p><p>22222222222222222222222</p><p><b>临近空间空间链接<img src=\"http://localhost:5050/static/lib/layui/images/face/14.gif\" alt=\"[亲亲]\"></b></p><p><span>也许你会觉得LayEdit的功能实在有点少吧，尤其是跟百度的UE这些重量级编辑器相比。是的，LayEdit的工具Bar还并不多，这主要是受制于Layui第一个版本的发布时间，一个功能丰富的编辑器需要较长时间的打磨，而Layui 1.0显然等不及。但我们会在后续版本视情况针对LayEdit进行功能升级，其中会包括：</span><em>HTML源代码编辑、字体颜色、字体大小、字体格式、插入表格、插入列表、插入引用块、插入代码、插入附件、分割线、预览、二次开发工具Bar的接口支持等等</em><span>。</span></p><p><span><br></span></p><p><span><br></span></p><p><span><br></span></p><p>layui富文本官方文档：<a href=\"https://www.layui.com/doc/modules/layedit.html\">https://www.layui.com/doc/modules/layedit.html</a></p><h3>1、创建一个layui富文本编辑器</h3><pre><div><code class=\"language-html\"><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">1</span><span class=\"token\">&lt;</span><span class=\"token\">form</span><span class=\"token\">&gt;</span><span>\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">2</span><span>    </span><span class=\"token\">&lt;</span><span class=\"token\">textarea</span><span class=\"token\"> </span><span class=\"token\">id</span><span class=\"token attr-equals\">=</span><span class=\"token\">\"</span><span class=\"token\">content</span><span class=\"token\">\"</span><span class=\"token\"> </span><span class=\"token\">name</span><span class=\"token attr-equals\">=</span><span class=\"token\">\"</span><span class=\"token\">content</span><span class=\"token\">\"</span><span class=\"token\"> </span><span class=\"token style-attr\">style</span><span class=\"token style-attr attr-equals\">=</span><span class=\"token style-attr\">\"</span><span class=\"token style-attr style language-css\">display</span><span class=\"token style-attr style language-css\">:</span><span class=\"token style-attr style language-css\"> none</span><span class=\"token style-attr style language-css\">;</span><span class=\"token style-attr\">\"</span><span class=\"token\">&gt;</span><span class=\"token\">&lt;/</span><span class=\"token\">textarea</span><span class=\"token\">&gt;</span><span>\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">3</span><span></span><span class=\"token\">&lt;/</span><span class=\"token\">form</span><span class=\"token\">&gt;</span><span>\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">4</span><span></span><span class=\"token\">&lt;</span><span class=\"token\">script</span><span class=\"token\">&gt;</span><span class=\"token script language-javascript\">\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">5</span><span class=\"token script language-javascript\">layui</span><span class=\"token script language-javascript\">.</span><span class=\"token script language-javascript method property-access\">use</span><span class=\"token script language-javascript\">(</span><span class=\"token script language-javascript\">\'layedit\'</span><span class=\"token script language-javascript\">,</span><span class=\"token script language-javascript\"> </span><span class=\"token script language-javascript\">function</span><span class=\"token script language-javascript\">(</span><span class=\"token script language-javascript\">)</span><span class=\"token script language-javascript\">{</span><span class=\"token script language-javascript\">\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">6</span><span class=\"token script language-javascript\">  </span><span class=\"token script language-javascript\">var</span><span class=\"token script language-javascript\"> layedit </span><span class=\"token script language-javascript\">=</span><span class=\"token script language-javascript\"> layui</span><span class=\"token script language-javascript\">.</span><span class=\"token script language-javascript property-access\">layedit</span><span class=\"token script language-javascript\">;</span><span class=\"token script language-javascript\">\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">7</span><span class=\"token script language-javascript\">  layedit</span><span class=\"token script language-javascript\">.</span><span class=\"token script language-javascript method property-access\">build</span><span class=\"token script language-javascript\">(</span><span class=\"token script language-javascript\">\'content\'</span><span class=\"token script language-javascript\">)</span><span class=\"token script language-javascript\">;</span><span class=\"token script language-javascript\"> </span><span class=\"token script language-javascript\">//建立编辑器</span><span class=\"token script language-javascript\">\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">8</span><span class=\"token script language-javascript\"></span><span class=\"token script language-javascript\">}</span><span class=\"token script language-javascript\">)</span><span class=\"token script language-javascript\">;</span><span class=\"token script language-javascript\">\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">9</span><span class=\"token script language-javascript\"></span><span class=\"token\">&lt;/</span><span class=\"token\">script</span><span class=\"token\">&gt;</span><span>\n</span></span><span><span class=\"linenumber react-syntax-highlighter-line-number\" style=\"text-align: right;\">10</span>\n</span></code></div></pre><p>实际上我们写到页面上的是一个隐藏的textarea控件（文本域，我们给这个文本域添加name属性，便于表单提交），layui在这个textarea下面为我们创建了富文本。所以， 我们在富文本中填写的内容并没有直接填写到textarea中，</p><ul><li>表单提交（异步）时，我们需要将富文本内容同步到textarea；</li><li>数据回显时，我们需要将textarea的内容同步到富文本；</li></ul><h3>2、新增页面，保存提交时将富文本内容同步到textarea，保证form提交正常获取数据</h3><p>以下是layui官网提供的方法：</p><blockquote><p>LayEdit提供了相当精简的方法，如下：</p><p>var index = layedit.build(id, options) 用于建立编辑器的核心方法 index：即该方法返回的索引 参数 id： 实例元素（一般为textarea）的id值 参数 options：编辑器的可配置项，下文会做进一步介绍 layedit.sync(index) 用于同步编辑器内容到textarea（一般用于异步提交） 参数 index： 同上</p></blockquote><p>更多方法参考官方文档：<a href=\"https://www.layui.com/doc/modules/layedit.html%5C#base\">https://www.layui.com/doc/modules/layedit.html\\#base</a></p><p>其中的layedit.sync(index)方法用于同步， 但是直接摆到js文件对于form表单提交获取值没什么用</p><p>可用的使用方式： 利用表单提交时需要表单验证的特性，我们自定义对textarea的验证，在验证时进行同步操作，然后获取表单内容时，就能够取到富文本的值了</p><p><ins class=\"adsbygoogle\" data-ad-layout=\"in-article\" data-ad-format=\"fluid\" data-ad-client=\"ca-pub-2563223522166395\" data-ad-slot=\"7045404516\" style=\"text-align: center;\"></ins><span></span></p><p>代码片段</p><p><span><br></span></p>');
