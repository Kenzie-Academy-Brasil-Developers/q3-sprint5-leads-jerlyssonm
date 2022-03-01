## entrega 19 

## API Leads, um crud simples com deploy no heroku

 URL_BASE = https://e-19.herokuapp.com

## ROTAS e EXEMPLOS

* POST
  /leads
* Entrada
```
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
}

```
* Saida
```
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
}
```

* GET /leads

retorda todos os leads
.

* PATCH /leads
```
{
    "email": "john@email.com"
}
```
sem retorno

*DELETE /leads
```
{
    "email": "john@email.com"
}
```
sem retorno