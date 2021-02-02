names = []
a = {
    "data" : [
        { "from": { "name" : "xxx", "age": "12" }, "message" : "yyy" },
        { "from": { "name" : "yyy", "age": "15" }, "message" : "sdfsd "},
        { "from": { "name" : "zzz", "age": "17" }, "message" : "sdfsdf "}
    ]
}
for i in a['data']:
    names.append(i['from']['name'])
print(names)