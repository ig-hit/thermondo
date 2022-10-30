# Thermondo Backend Coding Challenge

## Application:

* Users can add, delete and modify their notes
* Users can see a list of all their notes
* Users can filter their notes via tags
* Users must be logged in, in order to view/add/delete/etc. their notes

## Install

`make install`

Before creating and accessing notes, <br/>
authorize with the Admin user and add non-staff user:
```shell
curl --location --request POST 'http://0.0.0.0:3601/auth/tokens' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "jane.doe",
    "password": "mNjYaXp$0#6"
}
'
```

```shell
curl --location --request POST 'http://0.0.0.0:3601/auth/users/' \
--header 'Authorization: Bearer <<token>>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "john.doe",
    "password": "mNjYaXp$0#6",
    "password2": "mNjYaXp$0#6"
}
'
```

or use **Postman** resources from below.


## Postman

API endpoints are accessible with [Postman](./resources/Thermondo.postman_collection.json)
