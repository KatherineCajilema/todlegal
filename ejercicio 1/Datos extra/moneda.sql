/*==============================================================*/
/* DBMS name:      MySQL 4.0                                    */
/* Created on:     03/08/2022 3:24:41                           */
/*==============================================================*/


drop table if exists MONEDA;

drop index MONEDA2_FK on MONEDA2;

drop index MONEDA_FK on MONEDA2;

drop table if exists MONEDA2;

drop index MONEVALOR_FK on VALOR;

drop table if exists VALOR;

/*==============================================================*/
/* Table: MONEDA                                                */
/*==============================================================*/
create table MONEDA
(
   MO_ID                          int                            not null,
   MO_NOMBRE                      varchar(1024),
   primary key (MO_ID)
)
ENGINE = InnoDB;

/*==============================================================*/
/* Table: MONEDA2                                               */
/*==============================================================*/
create table MONEDA2
(
   MON_MO_ID                      int                            not null,
   MO_ID                          int                            not null,
   primary key (MON_MO_ID, MO_ID)
)
ENGINE = InnoDB;

/*==============================================================*/
/* Index: MONEDA_FK                                             */
/*==============================================================*/
create index MONEDA_FK on MONEDA2
(
   MON_MO_ID
);

/*==============================================================*/
/* Index: MONEDA2_FK                                            */
/*==============================================================*/
create index MONEDA2_FK on MONEDA2
(
   MO_ID
);

/*==============================================================*/
/* Table: VALOR                                                 */
/*==============================================================*/
create table VALOR
(
   VA_ID                          int                            not null,
   MO_ID                          int,
   VA_MONEDA_VALOR                float(8,2),
   VA_FECHA                       date,
   primary key (VA_ID)
)
ENGINE = InnoDB;

/*==============================================================*/
/* Index: MONEVALOR_FK                                          */
/*==============================================================*/
create index MONEVALOR_FK on VALOR
(
   MO_ID
);

alter table MONEDA2 add constraint FK_MONEDA foreign key (MON_MO_ID)
      references MONEDA (MO_ID) on delete restrict on update restrict;

alter table MONEDA2 add constraint FK_MONEDA2 foreign key (MO_ID)
      references MONEDA (MO_ID) on delete restrict on update restrict;

alter table VALOR add constraint FK_MONEVALOR foreign key (MO_ID)
      references MONEDA (MO_ID) on delete restrict on update restrict;

