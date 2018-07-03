# orm
OR Mapper test codes

seup
```
pip install -t lib -r requirements.txt
```

```
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_tags_on_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into users set id=1, name='tanaka';
insert into users set id=2, name='suzuki';
insert into users set id=3, name='takahashi';
````
