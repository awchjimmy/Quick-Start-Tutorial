# Maple Handbook Dumper

### 說明
從楓之谷學XML檔案處理

### 提示
* XML 格式
* 字串處理

### 輸入
一個 XML 檔案 “Mob.img.xml”
```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<imgdir name="Mob.img">
    <imgdir name="100000">
        <string name="name" value="Snail"/>
	</imgdir>
    <imgdir name="100001">
        <string name="name" value="Blue Snail"/>
    </imgdir>
    <imgdir name="100002">
	    <string name="name" value="Red Snail"/>
    </imgdir>
    <imgdir name="100003">
	    <string name="name" value="Spore"/>
    </imgdir>
	...(略)...
	<imgdir name="9410194">
        <string name="name" value="Ika"/>
    </imgdir>
</imgdir>
```

### 輸出
取出所有 怪物ID 及 怪物名稱，以 "ID - 名稱" 格式，一筆資料一列，輸出到螢幕
```
100000 - Snail
100001 - Blue Snail
100002 - Red Snail
100003 - Spore
...(略)...
9410194 - Ika
```
