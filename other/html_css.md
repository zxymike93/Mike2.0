# HTML 与 CSS

## HTML 与 CSS 基本

```html
<!DOCTYPE html>
css 两个主要功能:
1, 布局
2, 美化页面

布局主要的知识点是
1, 盒模型 box model / margin / padding
2, inline / block 样式
3, float 布局
4, flex 布局

<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>css部分内容</title>
  <style>
  /*
  让所有 div 都显示线框
  style 是显示的样式 dashed 是短横线
  width 是线宽
  color 是线的颜色
  */
  div {
  outline-style: dashed;
  outline-width: 1px;
  outline-color: red;
  }

  .box {
  margin: 10px;
  padding: 10px;
  color: blue;
  background: yellow;
  border-width: 10px;
  border-color: purple;
  border-style: solid;
  }

  .container {
  /* flex 可以让它里面的元素(这里是 content 和 sidebar)使用 flex 布局 */
  display: flex;
  /* 高度 100 像素 */
  height: 100px;
  /* 宽度 80% */
  width: 80%;
  /* margin: 0 auto 用来居中这个东西 */
  margin: 0 auto;
  }

  /* content 占了 3 份 */
  .content {
  flex-grow: 3;
  }

  /* sidebar 占了 1 份 */
  .sidebar {
  flex-grow: 1;
  }

  /*
  浮动布局
  */

  .float-left {
  float: left;
  background: cyan;
  }

  .float-right {
  float: right;
  }

  .clearfix::after {
  content: '';
  display: block;
  clear: both;
  }

  .space {
  height: 100px;
  background: green;
  }
  </style>
</head>
<body>
  <div class='box'>
  盒模型
  </div>
  <div class='nav'>
  导航栏
  </div>
  <div class='container'>
  <div class='content'>
  内容
  </div>
  <div class='sidebar'>
  侧边栏
  </div>
  </div>
  <div class='footer'>
  底栏
  </div>

  <div class='float-container clearfix'>
  <div class='float-left'>
  左边
  </div>
  <div class='float-right'>
  右边
  </div>
  </div>
  <div class='space'>
  空行
  </div>
</body>
</html>
```

## CSS 大草原

```css
简单分类

盒模型相关的 CSS

border
  border-width
  border-style
  border-color

border-top
  border-top-width
  border-top-style
  border-top-color

border-right
  border-right-width
  border-right-style
  border-right-color

border-bottom
  border-bottom-width
  border-bottom-style
  border-bottom-color

border-left
  border-left-width
  border-left-style
  border-left-color

margin
  margin-top
  margin-right
  margin-bottom
  margin-left

padding
  padding-top
  padding-right
  padding-bottom
  padding-left

三种缩写, 分别对应有 4 2 3 个值的时候的解释, padding 同理
margin: top right bottom left
margin: (top/bottom) (right/left)
margin: top (right/left) bottom

border-radius 左上角为 top, 右下角为 bottom

background 相关属性和缩写

background-color: #233;
background-image: url(bg.png);
background-repeat: no-repeat;
background-attachment: fixed; /* 背景图片随滚动轴的移动方式 */
background-position: top right; /* 这个属性的取值非常掏粪但是用得很少, 只在特殊的情况下有用 */

background: #233 url(bg.png) no-repeat top right;

list 属性和缩写

list-style-type: circle;
list-style-position: inside;
list-style-image: url(list.png);

list-style: circle inside url(list.png);

font 设置

font-style: italic;
font-variant: small-caps;
font-weight: bold;
font-size: 20px;
line-height: 1.5em;
font-family: Arial, sans-serif;

font:italic small-caps bold 20px/1.5em Arial, sans-serif;

显示相关的属性

visibility: visible;
  hidden; /* 不影响子元素 */

overflow: visible;
  hidden;
  scroll;
  auto;

display: block | inline | inline-block
position: static | relative | absolute | fixed | sticky
当 position 不为 static 的时候, 元素就是 positioned element
此时会开启下面 5 个秘密属性
  top
  right
  bottom
  left
  z-index

特殊属性
float
clear

非 inline 元素可以设置盒子尺寸
width
height
min-width
min-height
max-width
max-height

杂七杂八的垃圾

/* 可以叠加效果 */
text-decoration: underline overline line-through blink(这个值已经废弃了);

text-align: left | right | center | justify
vertical-align 偶尔有用
text-transform: none | capitalize | uppercase | lowercase
text-indent: 100px;

纯垃圾属性
unicode-bidi
direction

查文档
搜索 mdn 属性值
```
