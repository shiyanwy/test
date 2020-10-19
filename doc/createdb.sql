--创建单词表
CREATE TABLE `words` (
	`wuuid` INT(10) NOT NULL AUTO_INCREMENT COMMENT '唯一索引',
	`wbook` VARCHAR(50) NULL DEFAULT NULL COMMENT '书籍' COLLATE 'utf8_general_ci',
	`wunit` VARCHAR(50) NULL DEFAULT NULL COMMENT '单元' COLLATE 'utf8_general_ci',
	`wno` VARCHAR(50) NULL DEFAULT NULL COMMENT '单词序号' COLLATE 'utf8_general_ci',
	`wname` VARCHAR(50) NULL DEFAULT NULL COMMENT '单词' COLLATE 'utf8_general_ci',
	`wphonetic` VARCHAR(50) NULL DEFAULT NULL COMMENT '音标',
	`wpartofspeech` VARCHAR(50) NULL DEFAULT NULL COMMENT '词性\r\nn. 名词 \r\nv. 动词 \r\npron. 代词\r\nadj. 形容词 \r\nadv. 副词 \r\nnum.数词\r\nart. 冠词 \r\nprep. 介词 \r\nconj. 连词\r\ninterj. 感叹词',
	`wsection` VARCHAR(50) NULL DEFAULT NULL COMMENT '章节' COLLATE 'utf8_general_ci',
	`wparagraph` VARCHAR(50) NULL DEFAULT NULL COMMENT '段落' COLLATE 'utf8_general_ci',
	`wannotation` VARCHAR(2000) NULL DEFAULT NULL COMMENT '释义' COLLATE 'utf8_general_ci',
	`wexample` VARCHAR(2000) NULL DEFAULT NULL COMMENT '例句' COLLATE 'utf8_general_ci',
	PRIMARY KEY (`wuuid`) USING BTREE
)
COMMENT='单词表'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
