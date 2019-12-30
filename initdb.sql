CREATE TABLE `season_statistic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seasonId` int(11) NOT NULL DEFAULT '0',
  `tag` varchar(64) NOT NULL DEFAULT '',
  `name` varchar(64) NOT NULL DEFAULT '',
  `role` varchar(16) NOT NULL DEFAULT '',
  `expLevel` int(10) unsigned NOT NULL DEFAULT '0',
  `league` varchar(4048) NOT NULL DEFAULT '{}',
  `trophies` int(10) unsigned NOT NULL DEFAULT '0',
  `versusTrophies` int(10) unsigned NOT NULL DEFAULT '0',
  `clanRank` int(10) unsigned NOT NULL DEFAULT '0',
  `previousClanRank` int(10) unsigned NOT NULL DEFAULT '0',
  `attackWins` int(10) NOT NULL DEFAULT '0',
  `donations` int(10) unsigned NOT NULL DEFAULT '0',
  `donationsReceived` int(10) unsigned NOT NULL DEFAULT '0',
  `createAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updateAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_seasonId` (`seasonId`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;


CREATE TABLE `season` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `status` int(11) NOT NULL DEFAULT '0',
  `createAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updateAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `unq_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


CREATE TABLE `flowing_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(15) NOT NULL DEFAULT '',
  `expLevel` int(10) unsigned NOT NULL DEFAULT '0',
  `trophies` int(10) unsigned NOT NULL DEFAULT '0',
  `versusTrophies` int(10) unsigned NOT NULL DEFAULT '0',
  `attackWins` int(10) unsigned NOT NULL DEFAULT '0',
  `donations` int(10) unsigned NOT NULL DEFAULT '0',
  `donationsReceived` int(10) unsigned NOT NULL DEFAULT '0',
  `gold` int(10) unsigned NOT NULL DEFAULT '0',
  `elixir` int(10) unsigned NOT NULL DEFAULT '0',
  `darkElixir` int(10) unsigned NOT NULL DEFAULT '0',
  `dateTimeTag` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updateAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_dateTimeTag` (`dateTimeTag`),
  KEY `idx_tag` (`tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;