关于页面布局
===========

传统解决方案
------------
基于盒模型和五种定位方式

新兴解决方案
------------
基于弹性盒模型 (display: flex)。这种布局方式称为“弹性布局”，主要特点在于提供了元素排列方式和缩放的属性，进而可以快速实现页面的布局和自适应；任何一个元素加上"display: flex"属性后就成为flex容器，它的所有子元素自动成为flex项。

a. flex容器的属性

  - flex-direction: row | row-reverse | column | column-reverse;  /* 控制flex容器的轴向（默认为row，即主轴为水平方向） */
  - flex-wrap: nowrap | wrap | wrap-reverse;  /* flex容器中的一行flex项如果排不下，该如何换行（默认为nowrap，即不换行） */
    - flex-flow: <flex-direction> || <flex-wrap>;  /* 前两个属性的缩写 */
  
  - justify-content: flex-start | flex-end | center | space-between | space-around;            /* 控制flex项在水平方向上的对齐方式 */
  - align-content:   flex-start | flex-end | center | space-between | space-around | stretch;  /* 控制多行flex项在垂直方向上的对齐方式 */
  - align-items:     flex-start | flex-end | center                 | baseline     | stretch;  /* 控制单行flex项在垂直方向上的对齐方式 */

b. flex项的属性

  - flex-grow: <number>;  /* 存在剩余空间时，flex项对剩余空间的瓜分比例（默认为0，即不瓜分；flex项尺寸 = flex项原本尺寸 + 瓜分尺寸） */
  - flex-shrink: <number>;  /* 存在超出部分时, flex项对超出部分的分摊比例（默认为1，即分摊；flex项尺寸 = flex项原本尺寸 - 分摊尺寸） */
  - flex-basis: <length> | auto;  /* 定义flex项的宽度（默认为auto，即flex项的原本宽度；其会覆盖flex项的width属性）；width始终在水平方向上，flex-basis的方向随flex-direction而定*/ 
    - flex: <flex-grow> <flex-shrink> <flex-basis>;  /* 前三个属性的缩写（默认为0 1 auto）；auto代表(1 1 auto), none代表(0, 0, auto)*/
  
  - align-self: auto | flex-start | flex-end | center | baseline | stretch;  /* 控制单行flex项上的某个flex项在垂直方向上的对齐方式（会覆盖此元素的align-items属性） */
  - order: <integer>;  /* flex项的排列顺序，数值越小，排列越靠前（默认为0） */