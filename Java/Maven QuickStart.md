# Maven QuickStart

To create a blank Struts2 2.3.30 project
```
mvn archetype:generate -B -DgroupId=com.mycompany.mysystem \
                            -DartifactId=myWebApp \
                            -DarchetypeGroupId=org.apache.struts \
                            -DarchetypeArtifactId=struts2-archetype-blank \
                            -DarchetypeVersion=2.3.30 \
                            -DremoteRepositories=http://struts.apache.org
```

```mvn install``` - To Build  
```mvn test``` - To run test cases  
```mvn clean``` - To clean up (removes generated artifacts)  
```mvn eclipse:eclipse -Dwtpversion=1.5``` - To create Eclipse project files  
```mvn package``` - To package (creates a WAR file)  
```mvn jetty:run``` - To run it with Jetty  
