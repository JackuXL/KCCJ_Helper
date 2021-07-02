# KCCJ_Helper

调用微信小程序 快查成绩 API，对该平台的成绩进行查询，解决查询限制问题，批量查询支持生成排序

核心代码：（获取数据）

```python
requests.get(f"http://www.sales1.top/score/interface/search_exam_all_score.jsp?student_name={name}&student_num={uid}&course=全部")
```

使用 Fiddler 抓包获取 API。

仅供学习参考。

部分功能（如批量获取）需要修改入口函数。
