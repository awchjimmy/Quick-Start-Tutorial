# [Java QS] 使用NIO讀取文字檔案

### File Content
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
```

### Python Code

```
lines = open('/etc/passwd').readlines()

for line in lines:
	data = line.split(':') # data = ['root', 'x', '0', ..., '/bin/bash']
	...
```

### Equivalent Java Code
```
List<String> lines = null;
try {
	lines = Files.readAllLines(Paths.get("/etc/passwd"), StandardCharsets.UTF_8);
} catch (IOException e) {
	e.printStackTrace();
}

for (String line : lines) {
	String[] data = line.split(":");
	...
}
```
