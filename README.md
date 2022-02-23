# Entrega 16 - Leads 🍏 - Doc  
Endpoints

Method   | Example value
--------- | ------
POST | /leads
DELETE | /leads
GET |  /leads
PATCH| /leads



# POST /leads 
<p>Esta rota é para a criação de novas leads</p>
<p>Corpo da requisição obrigatoriamente apenas com name, email e phone, sendo todos os campos do tipo string.</p>
Modelo de requisição:

```
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
}
``` 

Modelo de resposta

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


# GET /leads
<p>Rota para listar todos os leads armazenados no banco</p>


# PATCH /leads
<p>
    Esta rota é para a atualização do campo "visits". É necessário passar o email através do corpo da requisição. A cada patch o campo "visits" do usuário irá ser incrementado. Obrigatoriamente só irá aceitar o campo email
</p>
Modelo de requisição:

```
{
 "email": "johnaa1@eamail.com"
}
```


# DELETE /leads
<p>
   Esta rota é para a deletar o lead. Para deletar é necessário passar o email no campo da requisição. Obrigatoriamente só irá aceitar o campo email
</p>
Modelo de requisição:

```
{
 "email": "johnaa1@eamail.com"
}
```
