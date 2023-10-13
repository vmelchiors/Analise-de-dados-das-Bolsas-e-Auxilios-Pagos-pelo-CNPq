import basedosdados as bd

df = bd.read_table(dataset_id='br_cnpq_bolsas',
                   table_id='microdados',
                   billing_project_id="mvp-base-de-dados")

df.shape()
df.head(5)
df.dropna()
df.to_csv("Database.csv", index=False)
df[["area_conhecimento", "subarea_conhecimento", "valor", "modalidade", "ano"]].to_csv("Database_filter.csv", index=False)
