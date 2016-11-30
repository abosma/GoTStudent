pragma foreign_keys=ON;
begin transaction;
create table Karakter(Naam text primary key);

insert into "Karakter" values('Piet');
commit;
