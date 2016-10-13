# Struts2 Quick Start

### Tutorials > BootStrap > Hello World (Workflow)
* browser
```
GET http://localhost:8080/example/HelloWorld.action
```

* struts.xml
```
<include file="example.xml"/>
```

* example.xml
```
<struts>
	<package name="example" namespace="/example" extends="struts-default">
		<action name="HelloWorld" class="com.mycompany.mysystem.example.HelloWorld">
            <result>/WEB-INF/example/HelloWorld.jsp</result>
        </action>
    </package>
</struts>
```

* HelloWorld.java
```
execute();
```

* HelloWorld.jsp
```
<%@ taglib prefix="s" uri="/struts-tags" %>
 
<html>
	...
</html>
```
