create table if not exists `members` (
  `id` varchar (15) not null default '' primary key,
  `name` varchar (64) not null default '',
  `role` varchar (16) not null default '',
  `expLevel` integer unsigned not null default 0,
  `league` varchar (4048) not null default '',
  `trophies` integer unsigned not null default 0,
  `versusTrophies` integer unsigned not null default 0,
  `clanRank` integer unsigned not null default 0,
  `previousClanRank` integer unsigned not null default 0,
  `donations` integer unsigned not null default 0,
  `donationsReceived` integer unsigned not null default 0
) engine=innodb default charset=utf8;


create table if not exists `flowing_data` (
  `id` integer auto_increment primary key,
  `tag` varchar (15) not null default '',
  `expLevel` integer unsigned not null default 0,
  `trophies` integer unsigned not null default 0,
  `versusTrophies` integer unsigned not null default 0,
  `attackWins` integer unsigned not null default 0,
  `donations` integer unsigned not null default 0,
  `donationsReceived` integer unsigned not null default 0,
  `gold` integer unsigned not null default 0,
  `elixir` integer unsigned not null default 0,
  `darkElixir` integer unsigned not null default 0,
  `dateTimeTag` datetime not null default current_timestamp,
  `createAt` datetime not null default current_timestamp,
  `updateAt` datetime not null default current_timestamp on update current_timestamp,
  key `idx_dateTimeTag` (`dateTimeTag`),
  key `idx_tag` (`tag`)
) engine=innodb default charset=utf8;
