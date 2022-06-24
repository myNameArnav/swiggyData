from parse import parse
import json

def jsonMaker(html):
    rName, rPlace, oNumber, oDateTime, dDateTime, orders, totalAmount = parse(html+".html")
    main = []

    for i in range(len(rName)):
        data = {}
        infoDic = {}
        dateTimeDic = {}

        name = rName[i]
        place = rPlace[i]
        orderNumber = oNumber[i]
        orderDT = oDateTime[i]
        isDelivered = dDateTime[i][0]
        delDT = dDateTime[i][1]
        orderItems = orders[i]
        total = totalAmount[i]

        dateTimeDic["orderDateTime"] = str(orderDT)
        dateTimeDic["deliveryDateTime"] = str(delDT)

        infoDic["isDelivered"] = isDelivered
        infoDic["orderNumber"] = orderNumber
        infoDic["name"] = name
        infoDic["place"] = place
        infoDic["dateTime"] = dateTimeDic
        infoDic["items"] = orderItems
        infoDic["totalAmount"] = total

        data["id"] = i+1
        data["info"] = infoDic

        main.append(data)

    jsonMaker = json.dumps(main)

    with open(html+".json", "w+") as f:
        f.write(jsonMaker)

