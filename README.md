# Desafio Bemobi 2
O programa recebe de entrada um arquivo de log (`log.txt`) via `stdin`, contendo registros de usuários.

Os dois primeiros dígitos do registro referem-se ao país do usuário, de acordo com o arquivo `codigos.json`

O registro mostra também se o usuário está ativo ou não.

O programa lê o arquivo de registros e escreve um resumo em um outro arquivo (`resultado.txt`), com a quantidade total de usuários por país e a quantidade de usuários ativos no formato:
`País,X,Y`, onde `X` é o número total de usuários do país e Y o número de usuários ativos.

## Uso
O programa pode ser utilizado de duas maneiras:
```
# via stdin
cat <arquivo_de_logs> | python3 verificarLog.py
```
ou
```
# via argumento
python3 verificarLog.py <arquivo_de_log>
```

## Novos códigos
Para adicionar novos códigos, basta alterar o arquivo `codigos.json` no formato:
```
{   
    ...,
    "CODIGO":"PAIS"
}
