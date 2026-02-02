# fastapi-demo

**Run app**
```console
python main.py
```

**Call root endpoint**
```console
curl http://localhost:8200/
```

**Call items endpoints**
List all items:
```console
curl http://localhost:8200/items/
```

Get single item:
```console
curl http://localhost:8200/items/item-a
```

Create new item:
```console
curl -X POST http://localhost:8200/items/ -H 'Content-Type: application/json' -d '{"name":"item-c","price":0.99}'
```