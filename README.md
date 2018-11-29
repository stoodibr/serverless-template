# serverless-boilerplate

## Uso

```
serverless create \
    --template-url https://github.com/serverless/serverless/tree/master/lib/plugins/create/templates/aws-python3
    --path my-new-project
```

## TODO

- Dockerizar
- Usar ideias de organização em <https://dev.to/egrajeda/my-python-serverless-setup-ca1>
- Configurar para `python -m unittest` deve rodar a suite de testes completa
- Usar ideias de APM em <https://hk.saowen.com/a/f390df2115e49bd7928503e60a189234b09f56ea305934cd39821d0a1327652f>
- Adicionar plugins, desligáveis por stage
- Opção de CLI para retorno em texto or JSON
- Atualizar a URL de template neste README
- CircleCI CLI <https://circleci.com/docs/2.0/local-cli/>