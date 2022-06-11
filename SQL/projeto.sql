CREATE TABLE usuario(
    id              bigserial NOT NULL PRIMARY KEY,
    nome            varchar(200),
    fone            varchar(20),
    criado_em       timestamp not null default CURRENT_TIMESTAMP,
    alterado_em     timestamp
);
