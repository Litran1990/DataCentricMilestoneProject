{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":103,"column":46},"end":{"row":103,"column":47},"action":"remove","lines":["\""],"id":1529}],[{"start":{"row":103,"column":46},"end":{"row":103,"column":47},"action":"insert","lines":["'"],"id":1530}],[{"start":{"row":103,"column":42},"end":{"row":103,"column":43},"action":"remove","lines":["\""],"id":1531}],[{"start":{"row":103,"column":42},"end":{"row":103,"column":43},"action":"insert","lines":["'"],"id":1532}],[{"start":{"row":104,"column":40},"end":{"row":104,"column":41},"action":"remove","lines":["\""],"id":1533}],[{"start":{"row":104,"column":40},"end":{"row":104,"column":41},"action":"insert","lines":["'"],"id":1534}],[{"start":{"row":104,"column":44},"end":{"row":104,"column":45},"action":"remove","lines":["\""],"id":1535}],[{"start":{"row":104,"column":44},"end":{"row":104,"column":45},"action":"insert","lines":["'"],"id":1536}],[{"start":{"row":104,"column":68},"end":{"row":104,"column":69},"action":"remove","lines":["\""],"id":1537}],[{"start":{"row":104,"column":68},"end":{"row":104,"column":69},"action":"insert","lines":["'"],"id":1538}],[{"start":{"row":104,"column":74},"end":{"row":104,"column":75},"action":"remove","lines":["\""],"id":1539}],[{"start":{"row":104,"column":74},"end":{"row":104,"column":75},"action":"insert","lines":["'"],"id":1540}],[{"start":{"row":103,"column":72},"end":{"row":103,"column":73},"action":"remove","lines":["\""],"id":1541}],[{"start":{"row":103,"column":72},"end":{"row":103,"column":73},"action":"insert","lines":["'"],"id":1542}],[{"start":{"row":103,"column":78},"end":{"row":103,"column":79},"action":"remove","lines":["\""],"id":1543}],[{"start":{"row":103,"column":78},"end":{"row":103,"column":79},"action":"insert","lines":["'"],"id":1544}],[{"start":{"row":91,"column":4},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":1546},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":108,"column":73},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":1547},{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":110,"column":0},"end":{"row":119,"column":61},"action":"insert","lines":["@app.route('/likes/<item_id>')","def likes(item_id):","    \"\"\"","    Another dynamic route utilised for liking recipes.  Allows","    users to see popularity of recipes.","    \"\"\"","    coll.find_one_and_update(","        {'_id': ObjectId(item_id)},","        {'$inc': {'likes': 1}})","    return redirect(url_for('instructions', item_id=item_id))"],"id":1548}],[{"start":{"row":119,"column":61},"end":{"row":120,"column":0},"action":"insert","lines":["",""],"id":1549},{"start":{"row":120,"column":0},"end":{"row":120,"column":4},"action":"insert","lines":["    "]},{"start":{"row":120,"column":4},"end":{"row":121,"column":0},"action":"insert","lines":["",""]},{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"remove","lines":["    "],"id":1550}],[{"start":{"row":121,"column":0},"end":{"row":121,"column":73},"action":"insert","lines":["#=======================================================================#"],"id":1551}],[{"start":{"row":111,"column":8},"end":{"row":111,"column":9},"action":"remove","lines":["s"],"id":1552}],[{"start":{"row":110,"column":19},"end":{"row":110,"column":28},"action":"remove","lines":["<item_id>"],"id":1553},{"start":{"row":110,"column":19},"end":{"row":110,"column":30},"action":"insert","lines":["<recipe_id>"]}],[{"start":{"row":111,"column":9},"end":{"row":111,"column":16},"action":"remove","lines":["item_id"],"id":1554},{"start":{"row":111,"column":9},"end":{"row":111,"column":10},"action":"insert","lines":["r"]},{"start":{"row":111,"column":10},"end":{"row":111,"column":11},"action":"insert","lines":["e"]},{"start":{"row":111,"column":11},"end":{"row":111,"column":12},"action":"insert","lines":["c"]},{"start":{"row":111,"column":12},"end":{"row":111,"column":13},"action":"insert","lines":["p"]}],[{"start":{"row":111,"column":12},"end":{"row":111,"column":13},"action":"remove","lines":["p"],"id":1555}],[{"start":{"row":111,"column":9},"end":{"row":111,"column":12},"action":"remove","lines":["rec"],"id":1556},{"start":{"row":111,"column":9},"end":{"row":111,"column":18},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":111,"column":4},"end":{"row":111,"column":5},"action":"insert","lines":["a"],"id":1557},{"start":{"row":111,"column":5},"end":{"row":111,"column":6},"action":"insert","lines":["d"]},{"start":{"row":111,"column":6},"end":{"row":111,"column":7},"action":"insert","lines":["d"]},{"start":{"row":111,"column":7},"end":{"row":111,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":113,"column":4},"end":{"row":114,"column":38},"action":"remove","lines":["Another dynamic route utilised for liking recipes.  Allows","    users to see popularity of recipes"],"id":1558},{"start":{"row":113,"column":4},"end":{"row":113,"column":5},"action":"insert","lines":["A"]},{"start":{"row":113,"column":5},"end":{"row":113,"column":6},"action":"insert","lines":["d"]},{"start":{"row":113,"column":6},"end":{"row":113,"column":7},"action":"insert","lines":["d"]}],[{"start":{"row":113,"column":7},"end":{"row":113,"column":8},"action":"insert","lines":[" "],"id":1559},{"start":{"row":113,"column":8},"end":{"row":113,"column":9},"action":"insert","lines":["a"]}],[{"start":{"row":113,"column":9},"end":{"row":113,"column":10},"action":"insert","lines":[" "],"id":1560},{"start":{"row":113,"column":10},"end":{"row":113,"column":11},"action":"insert","lines":["l"]},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["i"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["e"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["k"]}],[{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"remove","lines":["k"],"id":1561},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"remove","lines":["e"]}],[{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["k"],"id":1562},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":113,"column":14},"end":{"row":113,"column":15},"action":"insert","lines":[" "],"id":1563},{"start":{"row":113,"column":15},"end":{"row":113,"column":16},"action":"insert","lines":["t"]},{"start":{"row":113,"column":16},"end":{"row":113,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":113,"column":17},"end":{"row":113,"column":18},"action":"insert","lines":[" "],"id":1564},{"start":{"row":113,"column":18},"end":{"row":113,"column":19},"action":"insert","lines":["t"]},{"start":{"row":113,"column":19},"end":{"row":113,"column":20},"action":"insert","lines":["h"]},{"start":{"row":113,"column":20},"end":{"row":113,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":113,"column":21},"end":{"row":113,"column":22},"action":"insert","lines":[" "],"id":1565},{"start":{"row":113,"column":22},"end":{"row":113,"column":23},"action":"insert","lines":["r"]},{"start":{"row":113,"column":23},"end":{"row":113,"column":24},"action":"insert","lines":["e"]},{"start":{"row":113,"column":24},"end":{"row":113,"column":25},"action":"insert","lines":["c"]},{"start":{"row":113,"column":25},"end":{"row":113,"column":26},"action":"insert","lines":["i"]},{"start":{"row":113,"column":26},"end":{"row":113,"column":27},"action":"insert","lines":["p"]},{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"remove","lines":["."],"id":1566}],[{"start":{"row":112,"column":4},"end":{"row":113,"column":0},"action":"insert","lines":["",""],"id":1567},{"start":{"row":113,"column":0},"end":{"row":113,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":114,"column":0},"end":{"row":114,"column":4},"action":"remove","lines":["    "],"id":1568},{"start":{"row":113,"column":7},"end":{"row":114,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":114,"column":0},"end":{"row":114,"column":4},"action":"remove","lines":["    "],"id":1569},{"start":{"row":113,"column":31},"end":{"row":114,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":113,"column":34},"end":{"row":114,"column":0},"action":"insert","lines":["",""],"id":1570},{"start":{"row":114,"column":0},"end":{"row":114,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":115,"column":4},"end":{"row":115,"column":8},"action":"remove","lines":["coll"],"id":1571},{"start":{"row":115,"column":4},"end":{"row":115,"column":20},"action":"insert","lines":["mongo.db.recipes"]}],[{"start":{"row":116,"column":25},"end":{"row":116,"column":32},"action":"remove","lines":["item_id"],"id":1572},{"start":{"row":116,"column":25},"end":{"row":116,"column":26},"action":"insert","lines":["r"]},{"start":{"row":116,"column":26},"end":{"row":116,"column":27},"action":"insert","lines":["e"]},{"start":{"row":116,"column":27},"end":{"row":116,"column":28},"action":"insert","lines":["c"]},{"start":{"row":116,"column":28},"end":{"row":116,"column":29},"action":"insert","lines":["i"]}],[{"start":{"row":116,"column":25},"end":{"row":116,"column":29},"action":"remove","lines":["reci"],"id":1573},{"start":{"row":116,"column":25},"end":{"row":116,"column":34},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":118,"column":47},"end":{"row":118,"column":48},"action":"remove","lines":["m"],"id":1574},{"start":{"row":118,"column":46},"end":{"row":118,"column":47},"action":"remove","lines":["e"]},{"start":{"row":118,"column":45},"end":{"row":118,"column":46},"action":"remove","lines":["t"]},{"start":{"row":118,"column":44},"end":{"row":118,"column":45},"action":"remove","lines":["i"]}],[{"start":{"row":118,"column":44},"end":{"row":118,"column":45},"action":"insert","lines":["z"],"id":1576}],[{"start":{"row":118,"column":44},"end":{"row":118,"column":45},"action":"remove","lines":["z"],"id":1577},{"start":{"row":118,"column":44},"end":{"row":118,"column":45},"action":"insert","lines":["r"]},{"start":{"row":118,"column":45},"end":{"row":118,"column":46},"action":"insert","lines":["e"]},{"start":{"row":118,"column":46},"end":{"row":118,"column":47},"action":"insert","lines":["c"]},{"start":{"row":118,"column":47},"end":{"row":118,"column":48},"action":"insert","lines":["i"]},{"start":{"row":118,"column":48},"end":{"row":118,"column":49},"action":"insert","lines":["p"]},{"start":{"row":118,"column":49},"end":{"row":118,"column":50},"action":"insert","lines":["e"]}],[{"start":{"row":118,"column":54},"end":{"row":118,"column":61},"action":"remove","lines":["item_id"],"id":1578},{"start":{"row":118,"column":54},"end":{"row":118,"column":55},"action":"insert","lines":["r"]},{"start":{"row":118,"column":55},"end":{"row":118,"column":56},"action":"insert","lines":["e"]},{"start":{"row":118,"column":56},"end":{"row":118,"column":57},"action":"insert","lines":["c"]},{"start":{"row":118,"column":57},"end":{"row":118,"column":58},"action":"insert","lines":["i"]},{"start":{"row":118,"column":58},"end":{"row":118,"column":59},"action":"insert","lines":["p"]},{"start":{"row":118,"column":59},"end":{"row":118,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":118,"column":54},"end":{"row":118,"column":60},"action":"remove","lines":["recipe"],"id":1579},{"start":{"row":118,"column":54},"end":{"row":118,"column":63},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":110,"column":13},"end":{"row":110,"column":18},"action":"remove","lines":["likes"],"id":1580},{"start":{"row":110,"column":13},"end":{"row":110,"column":14},"action":"insert","lines":["a"]},{"start":{"row":110,"column":14},"end":{"row":110,"column":15},"action":"insert","lines":["d"]},{"start":{"row":110,"column":15},"end":{"row":110,"column":16},"action":"insert","lines":["d"]},{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":110,"column":17},"end":{"row":110,"column":18},"action":"insert","lines":["l"],"id":1581},{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"insert","lines":["i"]},{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"remove","lines":["e"],"id":1582}],[{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["k"],"id":1583},{"start":{"row":110,"column":20},"end":{"row":110,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":118,"column":29},"end":{"row":118,"column":41},"action":"remove","lines":["instructions"],"id":1584},{"start":{"row":118,"column":29},"end":{"row":118,"column":30},"action":"insert","lines":["v"]},{"start":{"row":118,"column":30},"end":{"row":118,"column":31},"action":"insert","lines":["i"]},{"start":{"row":118,"column":31},"end":{"row":118,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":118,"column":29},"end":{"row":118,"column":32},"action":"remove","lines":["vie"],"id":1585},{"start":{"row":118,"column":29},"end":{"row":118,"column":40},"action":"insert","lines":["view_recipe"]}],[{"start":{"row":117,"column":19},"end":{"row":117,"column":20},"action":"insert","lines":["r"],"id":1586},{"start":{"row":117,"column":20},"end":{"row":117,"column":21},"action":"insert","lines":["e"]},{"start":{"row":117,"column":21},"end":{"row":117,"column":22},"action":"insert","lines":["c"]},{"start":{"row":117,"column":22},"end":{"row":117,"column":23},"action":"insert","lines":["i"]},{"start":{"row":117,"column":23},"end":{"row":117,"column":24},"action":"insert","lines":["p"]},{"start":{"row":117,"column":24},"end":{"row":117,"column":25},"action":"insert","lines":["e"]},{"start":{"row":117,"column":25},"end":{"row":117,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":120,"column":73},"end":{"row":121,"column":0},"action":"insert","lines":["",""],"id":1587},{"start":{"row":121,"column":0},"end":{"row":122,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":122,"column":0},"end":{"row":130,"column":64},"action":"insert","lines":["@app.route('/add_like/<recipe_id>')","def add_like(recipe_id):","    ","    \"\"\"Add a like to the recipe\"\"\"","    ","    mongo.db.recipes.find_one_and_update(","        {'_id': ObjectId(recipe_id)},","        {'$inc': {'recipe_likes': 1}})","    return redirect(url_for('view_recipe', recipe_id=recipe_id))"],"id":1588}],[{"start":{"row":130,"column":64},"end":{"row":131,"column":0},"action":"insert","lines":["",""],"id":1589},{"start":{"row":131,"column":0},"end":{"row":131,"column":4},"action":"insert","lines":["    "]},{"start":{"row":131,"column":4},"end":{"row":132,"column":0},"action":"insert","lines":["",""]},{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"remove","lines":["    "],"id":1590},{"start":{"row":131,"column":4},"end":{"row":132,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":131,"column":4},"end":{"row":132,"column":0},"action":"insert","lines":["",""],"id":1591},{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"remove","lines":["    "],"id":1592}],[{"start":{"row":132,"column":0},"end":{"row":132,"column":73},"action":"insert","lines":["#=======================================================================#"],"id":1593}],[{"start":{"row":123,"column":8},"end":{"row":123,"column":9},"action":"insert","lines":["d"],"id":1594},{"start":{"row":123,"column":9},"end":{"row":123,"column":10},"action":"insert","lines":["i"]},{"start":{"row":123,"column":10},"end":{"row":123,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":122,"column":17},"end":{"row":122,"column":18},"action":"insert","lines":["d"],"id":1595},{"start":{"row":122,"column":18},"end":{"row":122,"column":19},"action":"insert","lines":["i"]},{"start":{"row":122,"column":19},"end":{"row":122,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":129,"column":34},"end":{"row":129,"column":35},"action":"insert","lines":["-"],"id":1596}],[{"start":{"row":129,"column":34},"end":{"row":129,"column":35},"action":"remove","lines":["-"],"id":1597}],[{"start":{"row":129,"column":26},"end":{"row":129,"column":27},"action":"insert","lines":["d"],"id":1598},{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"remove","lines":["s"],"id":1599}],[{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"insert","lines":["i"],"id":1600},{"start":{"row":129,"column":28},"end":{"row":129,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":125,"column":13},"end":{"row":125,"column":14},"action":"insert","lines":["d"],"id":1601},{"start":{"row":125,"column":14},"end":{"row":125,"column":15},"action":"insert","lines":["i"]},{"start":{"row":125,"column":15},"end":{"row":125,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":102,"column":5},"end":{"row":102,"column":41},"action":"remove","lines":["omment = { request.form['comment'] }"],"id":1602},{"start":{"row":102,"column":4},"end":{"row":102,"column":5},"action":"remove","lines":["c"]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"remove","lines":["    "]},{"start":{"row":101,"column":4},"end":{"row":102,"column":0},"action":"remove","lines":["",""]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"remove","lines":["    "]},{"start":{"row":100,"column":58},"end":{"row":101,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":97,"column":13},"end":{"row":97,"column":24},"action":"remove","lines":["view_recipe"],"id":1603},{"start":{"row":97,"column":13},"end":{"row":97,"column":14},"action":"insert","lines":["a"]},{"start":{"row":97,"column":14},"end":{"row":97,"column":15},"action":"insert","lines":["d"]},{"start":{"row":97,"column":15},"end":{"row":97,"column":16},"action":"insert","lines":["d"]}],[{"start":{"row":97,"column":13},"end":{"row":97,"column":16},"action":"remove","lines":["add"],"id":1604},{"start":{"row":97,"column":13},"end":{"row":97,"column":24},"action":"insert","lines":["add_comment"]}],[{"start":{"row":97,"column":39},"end":{"row":97,"column":55},"action":"remove","lines":["methods=['POST']"],"id":1605},{"start":{"row":97,"column":38},"end":{"row":97,"column":39},"action":"remove","lines":[" "]},{"start":{"row":97,"column":37},"end":{"row":97,"column":38},"action":"remove","lines":[","]}],[{"start":{"row":102,"column":4},"end":{"row":104,"column":43},"action":"remove","lines":["mongo.db.recipes.find_one_and_update({'_id': ObjectId(recipe_id)}, {'$push': {'comments': comment}})","    mongo.db.users.find_one_and_update({'_id': ObjectId(user_id)}, {'$push': {'comments': comment}})","    return redirect(url_for('view_recipe'))"],"id":1606},{"start":{"row":102,"column":4},"end":{"row":105,"column":64},"action":"insert","lines":["mongo.db.recipes.find_one_and_update(","        {'_id': ObjectId(recipe_id)},","        {'$inc': {'recipe_likes': 1}})","    return redirect(url_for('view_recipe', recipe_id=recipe_id))"]}],[{"start":{"row":104,"column":13},"end":{"row":104,"column":14},"action":"remove","lines":["c"],"id":1608},{"start":{"row":104,"column":12},"end":{"row":104,"column":13},"action":"remove","lines":["n"]},{"start":{"row":104,"column":11},"end":{"row":104,"column":12},"action":"remove","lines":["i"]}],[{"start":{"row":104,"column":11},"end":{"row":104,"column":12},"action":"insert","lines":["p"],"id":1609},{"start":{"row":104,"column":12},"end":{"row":104,"column":13},"action":"insert","lines":["u"]},{"start":{"row":104,"column":13},"end":{"row":104,"column":14},"action":"insert","lines":["s"]},{"start":{"row":104,"column":14},"end":{"row":104,"column":15},"action":"insert","lines":["h"]}],[{"start":{"row":104,"column":20},"end":{"row":104,"column":32},"action":"remove","lines":["recipe_likes"],"id":1610},{"start":{"row":104,"column":20},"end":{"row":104,"column":21},"action":"insert","lines":["c"]},{"start":{"row":104,"column":21},"end":{"row":104,"column":22},"action":"insert","lines":["o"]},{"start":{"row":104,"column":22},"end":{"row":104,"column":23},"action":"insert","lines":["m"]},{"start":{"row":104,"column":23},"end":{"row":104,"column":24},"action":"insert","lines":["m"]},{"start":{"row":104,"column":24},"end":{"row":104,"column":25},"action":"insert","lines":["e"]},{"start":{"row":104,"column":25},"end":{"row":104,"column":26},"action":"insert","lines":["n"]},{"start":{"row":104,"column":26},"end":{"row":104,"column":27},"action":"insert","lines":["t"]},{"start":{"row":104,"column":27},"end":{"row":104,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":104,"column":31},"end":{"row":104,"column":32},"action":"remove","lines":["1"],"id":1611}],[{"start":{"row":104,"column":31},"end":{"row":104,"column":32},"action":"insert","lines":["c"],"id":1612},{"start":{"row":104,"column":32},"end":{"row":104,"column":33},"action":"insert","lines":["o"]},{"start":{"row":104,"column":33},"end":{"row":104,"column":34},"action":"insert","lines":["m"]},{"start":{"row":104,"column":34},"end":{"row":104,"column":35},"action":"insert","lines":["m"]},{"start":{"row":104,"column":35},"end":{"row":104,"column":36},"action":"insert","lines":["e"]},{"start":{"row":104,"column":36},"end":{"row":104,"column":37},"action":"insert","lines":["n"]},{"start":{"row":104,"column":37},"end":{"row":104,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":97,"column":37},"end":{"row":97,"column":38},"action":"insert","lines":[","],"id":1613}],[{"start":{"row":97,"column":38},"end":{"row":97,"column":39},"action":"insert","lines":[" "],"id":1614},{"start":{"row":97,"column":39},"end":{"row":97,"column":40},"action":"insert","lines":["M"]},{"start":{"row":97,"column":40},"end":{"row":97,"column":41},"action":"insert","lines":["E"]},{"start":{"row":97,"column":41},"end":{"row":97,"column":42},"action":"insert","lines":["T"]},{"start":{"row":97,"column":42},"end":{"row":97,"column":43},"action":"insert","lines":["H"]},{"start":{"row":97,"column":43},"end":{"row":97,"column":44},"action":"insert","lines":["O"]}],[{"start":{"row":97,"column":44},"end":{"row":97,"column":45},"action":"insert","lines":["D"],"id":1615}],[{"start":{"row":97,"column":40},"end":{"row":97,"column":44},"action":"remove","lines":["ETHO"],"id":1616}],[{"start":{"row":97,"column":40},"end":{"row":97,"column":41},"action":"remove","lines":["D"],"id":1617},{"start":{"row":97,"column":39},"end":{"row":97,"column":40},"action":"remove","lines":["M"]}],[{"start":{"row":97,"column":39},"end":{"row":97,"column":62},"action":"insert","lines":["methods=['POST', 'GET']"],"id":1618}],[{"start":{"row":97,"column":60},"end":{"row":97,"column":61},"action":"remove","lines":["'"],"id":1619},{"start":{"row":97,"column":59},"end":{"row":97,"column":60},"action":"remove","lines":["T"]},{"start":{"row":97,"column":58},"end":{"row":97,"column":59},"action":"remove","lines":["E"]},{"start":{"row":97,"column":57},"end":{"row":97,"column":58},"action":"remove","lines":["G"]},{"start":{"row":97,"column":56},"end":{"row":97,"column":57},"action":"remove","lines":["'"]},{"start":{"row":97,"column":55},"end":{"row":97,"column":56},"action":"remove","lines":[" "]},{"start":{"row":97,"column":54},"end":{"row":97,"column":55},"action":"remove","lines":[","]}],[{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"remove","lines":["s"],"id":1620}],[{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"insert","lines":["s"],"id":1621}],[{"start":{"row":104,"column":20},"end":{"row":104,"column":21},"action":"insert","lines":["r"],"id":1622},{"start":{"row":104,"column":21},"end":{"row":104,"column":22},"action":"insert","lines":["e"]},{"start":{"row":104,"column":22},"end":{"row":104,"column":23},"action":"insert","lines":["c"]},{"start":{"row":104,"column":23},"end":{"row":104,"column":24},"action":"insert","lines":["i"]},{"start":{"row":104,"column":24},"end":{"row":104,"column":25},"action":"insert","lines":["p"]},{"start":{"row":104,"column":25},"end":{"row":104,"column":26},"action":"insert","lines":["e"]},{"start":{"row":104,"column":26},"end":{"row":104,"column":27},"action":"insert","lines":["_"]}],[{"start":{"row":102,"column":4},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":1623},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":4},"end":{"row":104,"column":0},"action":"insert","lines":["",""]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":102,"column":4},"end":{"row":102,"column":5},"action":"insert","lines":["c"],"id":1624},{"start":{"row":102,"column":5},"end":{"row":102,"column":6},"action":"insert","lines":["o"]},{"start":{"row":102,"column":6},"end":{"row":102,"column":7},"action":"insert","lines":["m"]},{"start":{"row":102,"column":7},"end":{"row":102,"column":8},"action":"insert","lines":["m"]},{"start":{"row":102,"column":8},"end":{"row":102,"column":9},"action":"insert","lines":["e"]},{"start":{"row":102,"column":9},"end":{"row":102,"column":10},"action":"insert","lines":["n"]},{"start":{"row":102,"column":10},"end":{"row":102,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":102,"column":11},"end":{"row":102,"column":12},"action":"insert","lines":[" "],"id":1625},{"start":{"row":102,"column":12},"end":{"row":102,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":102,"column":13},"end":{"row":102,"column":14},"action":"insert","lines":[" "],"id":1626}],[{"start":{"row":102,"column":14},"end":{"row":102,"column":15},"action":"insert","lines":["r"],"id":1627},{"start":{"row":102,"column":15},"end":{"row":102,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":102,"column":15},"end":{"row":102,"column":16},"action":"remove","lines":["e"],"id":1628},{"start":{"row":102,"column":14},"end":{"row":102,"column":15},"action":"remove","lines":["r"]}],[{"start":{"row":102,"column":14},"end":{"row":102,"column":38},"action":"insert","lines":["request.form['username']"],"id":1629}],[{"start":{"row":102,"column":28},"end":{"row":102,"column":36},"action":"remove","lines":["username"],"id":1630},{"start":{"row":102,"column":28},"end":{"row":102,"column":29},"action":"insert","lines":["c"]},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"insert","lines":["o"]},{"start":{"row":102,"column":30},"end":{"row":102,"column":31},"action":"insert","lines":["m"]},{"start":{"row":102,"column":31},"end":{"row":102,"column":32},"action":"insert","lines":["m"]},{"start":{"row":102,"column":32},"end":{"row":102,"column":33},"action":"insert","lines":["e"]},{"start":{"row":102,"column":33},"end":{"row":102,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":102,"column":33},"end":{"row":102,"column":34},"action":"remove","lines":["t"],"id":1631}],[{"start":{"row":102,"column":33},"end":{"row":102,"column":34},"action":"insert","lines":["n"],"id":1632},{"start":{"row":102,"column":34},"end":{"row":102,"column":35},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":1553,"scrollleft":0,"selection":{"start":{"row":102,"column":35},"end":{"row":102,"column":35},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":51,"state":"start","mode":"ace/mode/python"}},"timestamp":1563875376992,"hash":"e572cffaaa1ee38d9486ef05f18620fb1aae12ad"}